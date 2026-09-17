from config import LEETCODE_USERNAME

from utils import get_json
import json
import urllib.request
import urllib.error
from config import LEETCODE_USERNAME
from utils import log, error

def fetch_leetcode_stats(username=LEETCODE_USERNAME):
    log("Fetching LeetCode Stats...")
    if not username:
        error("LEETCODE_USERNAME is not configured.")
        return None

    # 1. Primary: Official LeetCode GraphQL API (No third-party proxy needed)
    graphql_url = "https://leetcode.com/graphql"
    query = """
    query userProblemsSolved($username: String!) {
        allQuestionsCount {
            difficulty
            count
        }
        matchedUser(username: $username) {
            submitStatsGlobal {
                acSubmissionNum {
                    difficulty
                    count
                }
            }
            profile {
                ranking
            }
        }
    }
    """
    payload = json.dumps({
        "query": query,
        "variables": {"username": username}
    }).encode("utf-8")

    req = urllib.request.Request(
        graphql_url,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
    )

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            matched = data.get("data", {}).get("matchedUser")
            if matched:
                ac_submissions = matched.get("submitStatsGlobal", {}).get("acSubmissionNum", [])
                stats_map = {item["difficulty"]: item["count"] for item in ac_submissions}
                ranking = matched.get("profile", {}).get("ranking", "N/A")

                stats = {
                    "totalSolved": stats_map.get("All", 0),
                    "easySolved": stats_map.get("Easy", 0),
                    "mediumSolved": stats_map.get("Medium", 0),
                    "hardSolved": stats_map.get("Hard", 0),
                    "ranking": ranking
                }
                log(f"LeetCode stats fetched successfully via GraphQL: {stats}")
                return stats
    except Exception as e:
        log(f"GraphQL request failed ({e}), trying fallback proxy...")

    # 2. Fallback: Alfa LeetCode proxy
    try:
        fallback_url = f"https://alfa-leetcode-api.onrender.com/userProfile/{username}"
        req_fallback = urllib.request.Request(
            fallback_url,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req_fallback, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if "totalSolved" in data:
                stats = {
                    "totalSolved": data.get("totalSolved", 0),
                    "easySolved": data.get("easySolved", 0),
                    "mediumSolved": data.get("mediumSolved", 0),
                    "hardSolved": data.get("hardSolved", 0),
                    "ranking": data.get("ranking", "N/A")
                }
                return stats
    except Exception as e:
        error(f"Unable to fetch LeetCode Stats from all sources: {e}")

    return None

from utils import error


def fetch_leetcode_stats(username=LEETCODE_USERNAME):

    log("Fetching LeetCode Stats...")

    url = (
        f"https://leetcode-api-faisalshohag.vercel.app/"
        f"{username}"
    )

    try:

        data = get_json(url)

        stats = {

            "totalSolved": data.get("totalSolved", 0),

            "easySolved": data.get("easySolved", 0),

            "mediumSolved": data.get("mediumSolved", 0),

            "hardSolved": data.get("hardSolved", 0),

            "ranking": data.get("ranking", "N/A")

        }

        return stats

    except Exception as e:

        error(f"Unable to fetch LeetCode Stats: {e}")

        return None
