import os
import json
from github_utils import fetch_leetcode_stats
from utils import log, error


def main():
    log("Starting Daily Automation Pipeline...")

    # 1. Fetch and save LeetCode Stats
    stats = fetch_leetcode_stats()
    if stats:
        os.makedirs("data", exist_ok=True)
        with open("data/leetcode.json", "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=2)
        log("Saved LeetCode stats to data/leetcode.json")
    else:
        log("No LeetCode stats returned.")

    # 2. Resume / Markdown updates
    updated_md = False
    try:
        from resume_utils import update_resume_markdown
        updated_md = update_resume_markdown()
    except Exception as e:
        log(f"Resume markdown update skipped: {e}")

    if updated_md:
        log("Resume markdown was updated.")
    else:
        log("No markdown updates needed.")


if __name__ == "__main__":
    main()
