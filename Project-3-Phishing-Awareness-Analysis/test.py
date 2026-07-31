import os 


def get_demo_emails():

    print("="*70)
    print(f"{'Demo Email Analyzer':^70}")
    print("="*70)
    print()
    print("Select only one option:\n")

    email_list = []
    number = 0

    folder = os.listdir("Demo-Emails")

    for files in folder:
        if files.endswith(".txt"):
            number += 1
            email_list.append(files)
        print(f"[{number:02}] {email_list[number - 1]}")

    print(f"[{number + 1}] All of them")
    print("\n[00] Back")
    print("[0] Exit")