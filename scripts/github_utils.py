import json
import urllib.request
import urllib.error
import os
from utils import log, error

LEETCODE_USERNAME = os.getenv("LEETCODE_USERNAME", "awadhesh_2906")

def fetch_leetcode_stats(username=LEETCODE_USERNAME):
    log(f"Fetching LeetCode Stats for {username}...")
    if not username:
        error("LEETCODE_USERNAME is not set.")
        return None

    url = "https://leetcode.com/graphql"
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
        url,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw = json.loads(resp.read().decode("utf-8"))
            matched = raw.get("data", {}).get("matchedUser")
            if matched:
                submissions = matched.get("submitStatsGlobal", {}).get("acSubmissionNum", [])
                stats_map = {item["difficulty"]: item["count"] for item in submissions}
                ranking = matched.get("profile", {}).get("ranking", "N/A")

                stats = {
                    "totalSolved": stats_map.get("All", 0),
                    "easySolved": stats_map.get("Easy", 0),
                    "mediumSolved": stats_map.get("Medium", 0),
                    "hardSolved": stats_map.get("Hard", 0),
                    "ranking": ranking
                }
                log(f"LeetCode stats fetched: {stats}")
                return stats
            else:
                error(f"User {username} not found on LeetCode.")
                return None
    except Exception as e:
        error(f"Failed to query LeetCode GraphQL: {e}")
        return None
