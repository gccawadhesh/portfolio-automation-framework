"""
Configuration for Awadhesh Kumar's Portfolio Automation Framework.

Personal details, API credentials, profile configuration,
LeetCode username, and resume paths are maintained here.
"""

import os
from pathlib import Path


# ============================================================
# PROJECT PATHS
# ============================================================

# config.py is located inside /scripts.
# parent.parent points to the repository root.
ROOT_DIR = Path(__file__).resolve().parent.parent


# ============================================================
# PERSONAL INFORMATION
# ============================================================

NAME = "Awadhesh Kumar"

EMAIL = "awadheshkumar210424@gmail.com"

PHONE = "6388923839"

LOCATION = "Kanpur, Uttar Pradesh, India"

COLLEGE = "Maharana Institute of Professional Studies, Kanpur"

DEGREE = "B.Tech Computer Science & Engineering"

SPECIALIZATION = "Artificial Intelligence & Machine Learning"

CURRENT_YEAR = "Final Year"


# ============================================================
# GITHUB
# ============================================================

GITHUB_USERNAME = "gccawadhesh"

GITHUB_URL = "https://github.com/gccawadhesh"


# ============================================================
# LINKEDIN
# ============================================================

LINKEDIN_URL = (
    "https://www.linkedin.com/"
    "in/awadhesh-kumar-366963291"
)


# ============================================================
# LEETCODE
# ============================================================

# GitHub Actions can provide LEETCODE_USERNAME as an
# environment variable.
#
# If the variable is not available, Awadhesh's username
# below will be used automatically.

LEETCODE_USERNAME = os.getenv(
    "LEETCODE_USERNAME",
    "awadhesh_2906"
)


# ============================================================
# API / ENVIRONMENT VARIABLES
# ============================================================

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

LINKEDIN_ACCESS_TOKEN = os.getenv(
    "LINKEDIN_ACCESS_TOKEN"
)

LINKEDIN_AUTHOR_URN = os.getenv(
    "LINKEDIN_AUTHOR_URN"
)

DEV_TO_API_KEY = os.getenv(
    "DEV_TO_API_KEY"
)


# ============================================================
# RESUME CONFIGURATION
# ============================================================

# Source markdown resume
RESUME_FILE = ROOT_DIR / "resume.md"

# Final generated resume PDF
RESUME_PDF = ROOT_DIR / "Awadhesh_Kumar_Resume.pdf"

# Compatibility alias for scripts that expect PRIMARY_RESUME
PRIMARY_RESUME = RESUME_PDF


# ============================================================
# PORTFOLIO INFORMATION
# ============================================================

PORTFOLIO_TITLE = (
    "Awadhesh Kumar | Software Developer & AI/ML Engineer"
)

PORTFOLIO_DESCRIPTION = (
    "Final-year B.Tech CSE (AI & ML) student at Maharana "
    "Institute of Professional Studies, Kanpur, passionate "
    "about Software Development, Artificial Intelligence, "
    "Machine Learning, Backend Engineering, Full-Stack "
    "Development, Automation, and Problem Solving."
)


# ============================================================
# VALIDATION HELPERS
# ============================================================

def validate_config():
    """
    Display warnings for optional credentials that have
    not been configured in the environment.
    """

    missing = []

    if not GEMINI_API_KEY:
        missing.append("GEMINI_API_KEY")

    if not LINKEDIN_ACCESS_TOKEN:
        missing.append("LINKEDIN_ACCESS_TOKEN")

    if not LINKEDIN_AUTHOR_URN:
        missing.append("LINKEDIN_AUTHOR_URN")

    if not DEV_TO_API_KEY:
        missing.append("DEV_TO_API_KEY")

    return missing