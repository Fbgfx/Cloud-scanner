📁 Project 1: Cloud Security Scanner (AWS)
🔍 Overview
The Cloud Security Scanner is a Python-based tool designed to assess AWS environments for common security misconfigurations and governance gaps. The project focuses on identifying preventive control failures that increase the risk of account compromise, data exposure, and compliance violations.
This project reflects real-world cloud security assessments performed by cloud governance and security engineering teams.

🎯 Objectives
Identify insecure cloud configurations early


Reduce cloud risk through visibility and guardrails


Align findings with cloud security best practices


Build foundational skills for cloud governance engineering



🛠️ Technologies Used
Python


AWS SDK (boto3)


AWS IAM


AWS S3


AWS CloudTrail


Streamlit (UI demo)


AWS Well-Architected Framework



🔐 Security Checks Performed
IAM users without MFA


Root account usage


Publicly accessible S3 buckets


CloudTrail logging status


Overly permissive IAM policies


Missing basic security controls


🧩 Real-World Use Case
Cloud security assessments


Governance baseline reviews


Pre-compliance audits (CIS, SOC 2)


Continuous security posture monitoring



🚀 Future Enhancements
Add AWS Organizations support


Map findings to CIS AWS Foundations


Convert scanner into a FastAPI service


Integrate policy-as-code checks



📌 Skills Demonstrated
Cloud security fundamentals


AWS identity & access management


Security posture assessment


Preventive control mindset














📂 Lab Steps

1. Firstly, I created a Python virtual environment (.venv) to isolate dependencies and ensure reproducible development for a cloud security scanning application.



2. Designed a modular project structure using an app/ package to separate AWS S3, IAM, and CloudTrail security checks, following clean code and scalability principles.
3. Implemented multiple security check modules (s3_checks.py, iam_checks.py, cloudtrail_checks.py) to simulate real-world cloud misconfiguration detection logic.



4. Created and managed dependency tracking with requirements.txt, installing core libraries such as boto3, streamlit, and python-dotenv to support AWS interactions and UI rendering.



5. Successfully installed and resolved Python package dependencies using pip, demonstrating environment setup, dependency resolution, and familiarity with Python tooling.



6. Built a Streamlit-based web interface (main.py) to provide an interactive UI for scanning cloud storage endpoints for public exposure risks. Our title for our UI is displayed this way..


7. Developed logic to detect public S3 bucket access by analyzing HTTP response codes (200, 403, 404), mapping technical results to clear security risk indicators for users.











8. Ultimately we end up with this User Interface. With 3 functions that call ontp

