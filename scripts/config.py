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

LINKEDIN_URL = "https://www.linkedin.com/in/awadhesh-kumar-366963291"

# ======================================================
# Resume Files
# ======================================================

RESUME_FILE = "resume.md"

PRIMARY_RESUME = "Awadhesh_Kumar_Resume.pdf"

ATS_RESUME = "Awadhesh_Kumar_ATS_Resume.pdf"

# ======================================================
# Portfolio Information
# ======================================================

PORTFOLIO_TITLE = "Awadhesh Kumar | AI & ML Engineer"

PORTFOLIO_DESCRIPTION = (
    "Final Year B.Tech CSE (AI & ML) student passionate about "
    "Artificial Intelligence, Machine Learning, Full-Stack Development, "
    "Backend Engineering, Automation, and Problem Solving."
)