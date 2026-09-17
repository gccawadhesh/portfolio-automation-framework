import os
import json
from github_utils import fetch_leetcode_stats
from utils import log, error

def main():
    log("Starting Daily Automation Pipeline...")

    # 1. Fetch from LeetCode and write to data/leetcode.json
    stats = fetch_leetcode_stats()
    if stats:
        os.makedirs("data", exist_ok=True)
        out_path = os.path.join("data", "leetcode.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=2)
        log(f"Saved stats to {out_path}")
    else:
        log("Skipping leetcode.json update due to fetch error.")

    # 2. Safely run resume update if available
    try:
        from update_resume_projects import update_resume_projects
        update_resume_projects()
    except Exception as e:
        log(f"Resume project update skipped or completed: {e}")

if __name__ == "__main__":
    main()
