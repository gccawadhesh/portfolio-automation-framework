import json
import urllib.request
import urllib.error
from config import LEETCODE_USERNAME
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

    # 2. Handle Resume / Markdown updates safely
    updated_md = False
    try:
        # If you import a function to update the markdown:
        from resume_utils import update_resume_markdown # adjust if your function name differs
        updated_md = update_resume_markdown()
    except Exception as e:
        log(f"Resume markdown update skipped or failed: {e}")

    if updated_md:
        log("Resume markdown was updated.")
    else:
        log("No markdown updates needed.")

if __name__ == "__main__":
    main()
