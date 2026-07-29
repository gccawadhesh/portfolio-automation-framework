"""
Awadhesh Kumar - Portfolio Automation Pipeline

This script runs the daily portfolio automation workflow.

Pipeline:
1. Fetch LeetCode statistics
2. Update resume markdown
3. Generate updated resume PDF
4. Generate LinkedIn post
5. Publish LinkedIn post when configured
"""

from github_utils import fetch_leetcode_stats
from resume_utils import update_resume_markdown
from pdf_utils import compile_pdf_variant
from ai_utils import generate_linkedin_post
from linkedin_utils import publish_post

from config import RESUME_PDF

from utils import log


def main():
    """
    Run Awadhesh Kumar's portfolio automation pipeline.
    """

    log("=" * 60)
    log("Starting Awadhesh Kumar Portfolio Automation...")
    log("=" * 60)

    # ==========================================================
    # STEP 1: FETCH LEETCODE STATISTICS
    # ==========================================================

    log("Fetching LeetCode statistics...")

    stats = fetch_leetcode_stats()

    if not stats:
        log("Unable to fetch LeetCode statistics.")
        log("Automation stopped.")
        return

    total_solved = stats.get("totalSolved", 0)

    log(
        f"LeetCode statistics fetched successfully. "
        f"Total solved: {total_solved}"
    )

    # ==========================================================
    # STEP 2: UPDATE RESUME MARKDOWN
    # ==========================================================

    log("Updating resume with latest coding statistics...")

    updated_md = update_resume_markdown(
        total_solved
    )

    if not updated_md:
        log("Resume markdown was not updated.")
    else:
        log("Resume markdown updated successfully.")

        # ======================================================
        # STEP 3: GENERATE RESUME PDF
        # ======================================================

        log("Generating Awadhesh Kumar resume PDF...")

        try:
            compile_pdf_variant(
                updated_md,
                RESUME_PDF,
                "general"
            )

            log(
                f"Resume generated successfully: "
                f"{RESUME_PDF}"
            )

        except Exception as error:
            log(
                f"Resume PDF generation failed: {error}"
            )

    # ==========================================================
    # STEP 4: GENERATE LINKEDIN POST
    # ==========================================================

    log("Generating LinkedIn post...")

    try:
        post = generate_linkedin_post(
            stats
        )

    except Exception as error:
        log(
            f"LinkedIn post generation failed: {error}"
        )
        post = None

    # ==========================================================
    # STEP 5: PUBLISH LINKEDIN POST
    # ==========================================================

    if post:

        print(
            "\nGenerated LinkedIn Post:\n"
        )

        print(post)

        try:

            publish_post(
                post
            )

            log(
                "LinkedIn publishing step completed."
            )

        except Exception as error:

            log(
                f"LinkedIn publishing failed: {error}"
            )

    else:

        log(
            "No LinkedIn post was generated."
        )

    # ==========================================================
    # COMPLETE
    # ==========================================================

    log("=" * 60)
    log(
        "Awadhesh Kumar Portfolio Automation Completed."
    )
    log("=" * 60)


if __name__ == "__main__":
    main()