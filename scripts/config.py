import os

# ======================================================
# API Keys & Environment Variables
# ======================================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

LINKEDIN_ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")

LINKEDIN_AUTHOR_URN = os.getenv("LINKEDIN_AUTHOR_URN")

LEETCODE_USERNAME = os.getenv(
    "LEETCODE_USERNAME",
    "your_leetcode_username"   # Replace with your LeetCode username
)

# ======================================================
# Personal Information
# ======================================================

NAME = "Awadhesh Kumar"

ROLE = "Final Year B.Tech CSE (AI & ML) Student"

COLLEGE = "Maharana Institute of Professional Studies, Kanpur"

EMAIL = "awadheshkumar210424@gmail.com"

PHONE = "+91 6388923839"

GITHUB_USERNAME = "gccawadhesh"

GITHUB_URL = "https://github.com/gccawadhesh"

LINKEDIN_URL = "https://www.linkedin.com/in/awadhesh-kumar-366963291"
# ============================================================
# RESUME FILES
# ============================================================

RESUME_FILE = ROOT_DIR / "resume.md"

RESUME_PDF = ROOT_DIR / "Awadhesh_Kumar_Resume.pdf"
# ======================================================
# Portfolio Information
# ======================================================

PORTFOLIO_TITLE = "Awadhesh Kumar | AI & ML Engineer"

PORTFOLIO_DESCRIPTION = (
    "Final Year B.Tech CSE (AI & ML) student passionate about "
    "Artificial Intelligence, Machine Learning, Full-Stack Development, "
    "Backend Engineering, Automation, and Problem Solving."
)