from Modules.email_analyzer import analyze_email
from Modules.batch_report_generator import batch_report_menu
import os

def analyze_all_emails():

    print("=" * 100)
    print(f"\n{'Analyzing All Emails':^100}\n")
    print("=" * 100)

    email_list = []
    all_report_data = []

    folder = os.listdir("Demo-Emails")


    for file in folder:
        if file.endswith(".txt"):
            email_list.append(file)

    email_list.sort(key = lambda file: int(file.split("-")[1]))
    print(f"{len(email_list)} email(s) found!\n")

    for email in email_list:

        path = os.path.join("Demo-Emails", email)

        with open(path , "r") as file:
            contents = file.read()

        print("-"*100)
        print(f"{email:^100}")
        print("-"*100)

        print(contents)

        # Analyze email
        email_report_data = analyze_email(contents)

        # Add email filename to report data
        email_report_data["file_name"] = email

        # Save this email's report data
        all_report_data.append(email_report_data.copy())

    # Open batch report menu after all emails are analyzed
    batch_report_menu(all_report_data)