import os
from pathlib import Path


# ============================================================
# PROJECT PATHS
# ============================================================

# config.py is inside /scripts
# parent.parent gives the repository root directory
ROOT_DIR = Path(__file__).resolve().parent.parent


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


# ============================================================
# PERSONAL INFORMATION
# ============================================================

NAME = "Awadhesh Kumar"

EMAIL = "awadheshkumar210424@gmail.com"

PHONE = "6388923839"

COLLEGE = (
    "Maharana Institute of Professional Studies, Kanpur"
)

DEGREE = (
    "B.Tech Computer Science & Engineering"
)

SPECIALIZATION = (
    "Artificial Intelligence & Machine Learning"
)

CURRENT_YEAR = "Final Year"


# ============================================================
# GITHUB
# ============================================================

GITHUB_USERNAME = "gccawadhesh"

GITHUB_URL = (
    "https://github.com/gccawadhesh"
)


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

LEETCODE_USERNAME = os.getenv(
    "LEETCODE_USERNAME",
    ""
)


# ============================================================
# RESUME FILES
# ============================================================

# Markdown source resume
RESUME_FILE = (
    ROOT_DIR / "resume.md"
)

# Final generated resume
RESUME_PDF = (
    ROOT_DIR / "Awadhesh_Kumar_Resume.pdf"
)