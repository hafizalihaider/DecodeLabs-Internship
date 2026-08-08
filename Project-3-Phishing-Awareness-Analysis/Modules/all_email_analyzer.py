# ============================================================
# PHISHING AWARENESS ANALYZER
# ============================================================
#
# Author      : Hafiz Muhammad Ali Haider
# Date        : 09 August 2026
# Project     : Phishing Awareness Analysis
# File        : all_email_analyzer.py
#
# Description :
# Analyzes all demo emails automatically and stores
# their analysis results for separate or combined reports.
#
# ============================================================

from Modules.email_analyzer import analyze_email
from Modules.batch_report_generator import batch_report_menu
import os


def analyze_all_emails():

    # Collect all demo emails and their analysis results.
    print("=" * 100)
    print(f"\n{'Analyzing All Emails':^100}\n")
    print("=" * 100)

    email_list = []
    all_report_data = []

    folder = os.listdir("Demo-Emails")

    for file in folder:
        if file.endswith(".txt"):
            email_list.append(file)

    email_list.sort(key=lambda file: int(file.split("-")[1]))
    print(f"{len(email_list)} email(s) found!\n")

    # Analyze each demo email and store its results.
    for email in email_list:

        path = os.path.join("Demo-Emails", email)

        with open(path, "r") as file:
            contents = file.read()

        print("-" * 100)
        print(f"{email:^100}")
        print("-" * 100)

        print(contents)

        email_report_data = analyze_email(contents)

        # Keep the original filename so it appears in the report.
        email_report_data["file_name"] = email

        all_report_data.append(email_report_data.copy())

    # Let the user choose separate or combined report generation.
    batch_report_menu(all_report_data)