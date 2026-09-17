from github_utils import fetch_leetcode_stats
from resume_utils import update_resume_markdown
from pdf_utils import compile_pdf_variant
from ai_utils import generate_linkedin_post
from linkedin_utils import publish_post

from config import RESUME_PDF
from utils import log
import os
import json
from utils import log

# In your main execution flow:


def main():

    log("Starting Daily Automation Pipeline...")

    stats = fetch_leetcode_stats()
    if stats:
        os.makedirs("data", exist_ok=True)
        with open("data/leetcode.json", "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=2)
        log("Saved LeetCode stats to data/leetcode.json")
    if updated_md:

        compile_pdf_variant(
            updated_md,
            RESUME_PDF,
            "default"
        )

    post = generate_linkedin_post(stats)

    if post:

        print("\nGenerated LinkedIn Post:\n")
        print(post)

        publish_post(post)

    log("Automation Completed.")


if __name__ == "__main__":
    main()
