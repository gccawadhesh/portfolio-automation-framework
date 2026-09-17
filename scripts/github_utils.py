import json
import urllib.request
import urllib.error
import os
from utils import log, error

LEETCODE_USERNAME = os.getenv("LEETCODE_USERNAME", "awadhesh_2906").strip()

def fetch_leetcode_stats(username=LEETCODE_USERNAME):
    username = (username or "").strip()
    log(f"Fetching LeetCode Stats for {username}...")
    
    if not username:
        error("LEETCODE_USERNAME is empty.")
        return None

    # 1. Primary: LeetCode GraphQL
    try:
        url = "https://leetcode.com/graphql"
        query = """
        query userProblemsSolved($username: String!) {
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
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
                "Referer": "https://leetcode.com"
            }
        )

        with urllib.request.urlopen(req, timeout=12) as resp:
            raw = json.loads(resp.read().decode("utf-8"))
            matched = raw.get("data", {}).get("matchedUser")
            if matched:
                submissions = matched.get("submitStatsGlobal", {}).get("acSubmissionNum", [])
                stats_map = {item["difficulty"].lower(): item["count"] for item in submissions}
                ranking = matched.get("profile", {}).get("ranking", "N/A")

                stats = {
                    "totalSolved": stats_map.get("all", 0),
                    "easySolved": stats_map.get("easy", 0),
                    "mediumSolved": stats_map.get("medium", 0),
                    "hardSolved": stats_map.get("hard", 0),
                    "ranking": ranking
                }
                log(f"LeetCode stats fetched via GraphQL: {stats}")
                return stats
            else:
                log(f"GraphQL returned no user for '{username}'. Trying fallback proxy...")
    except Exception as e:
        log(f"GraphQL failed ({e}), trying fallback proxy...")

    # 2. Fallback: Alfa LeetCode API (runs server-side in Python, no browser CORS)
    try:
        fallback_url = f"https://alfa-leetcode-api.onrender.com/userProfile/{username}"
        req_fallback = urllib.request.Request(
            fallback_url,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req_fallback, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            total = data.get("totalSolved") or data.get("solvedProblem")
            if total is not None:
                stats = {
                    "totalSolved": int(total),
                    "easySolved": int(data.get("easySolved", 0)),
                    "mediumSolved": int(data.get("mediumSolved", 0)),
                    "hardSolved": int(data.get("hardSolved", 0)),
                    "ranking": data.get("ranking", "N/A")
                }
                log(f"LeetCode stats fetched via fallback proxy: {stats}")
                return stats
    except Exception as e:
        error(f"Fallback proxy also failed: {e}")

    return None
