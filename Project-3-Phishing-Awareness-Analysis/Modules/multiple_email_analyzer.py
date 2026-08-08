import os
from Modules.email_loader import load_demo_email
from Modules.email_analyzer import analyze_email
from Modules.batch_report_generator import batch_report_menu

def analyze_multiple_emails():

    all_report_data = []
    analyzed = []

    while True:

        email_list = []

        print("="*100)
        print(f"\n{'Multiple Emails Analyzer':^100}\n")
        print("="*100)

        print("\nEnter the email number(s) you want to analyze.")
        print("Example: 1,4,7")
        print()

        folder = os.listdir("Demo-Emails")

        for file in folder:
            if file.endswith(".txt"):
                email_list.append(file)

        email_list.sort(key = lambda file: int(file.split("-")[1]))
        print(f"{len(email_list)} email(s) found!\n")

        for number, file in enumerate(email_list, 1):
            print(f"[{number:02}] {file}")

        print("[00] Back")
        print("-"*100)


        multiple_emails_choice = input("Enter the email number(s): ")
        selected_emails = multiple_emails_choice.split(",")

        if multiple_emails_choice == "00":
            break

        for email in selected_emails:

            email = email.strip()

            if email.isdigit():

                email = int(email)

                if email >= 1 and email <= len(email_list):

                    if email not in analyzed:
                        analyzed.append(email)

                        content = load_demo_email(email_list[email - 1])

                        print("-" * 100)
                        print(f"{email_list[email - 1]:^100}")
                        print("-" * 100)

                        print(content)

                        email_report_data = analyze_email(content)
                        email_report_data["file_name"] = email_list[email -1]

                        all_report_data.append(email_report_data.copy())

                else:
                    print(f"[!] Email {email} does not exist.")

            else:
                print(f"[!] '{email}' is not a valid number.")

        batch_report_menu(all_report_data)
        break