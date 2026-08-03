from Modules.email_analyzer import analyze_email
import os

def analyze_all_emails():

    print("=" * 70)
    print(f"\n{'Analyzing All Emails':^70}\n")
    print("=" * 70)

    email_list = []

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

        print("-"*70)
        print(f"{email:^70}")
        print("-"*70)

        print(contents)

        analyze_email(contents)