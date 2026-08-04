from Modules.email_analyzer import analyze_email
import os

def analyze_custom_email():

    email_lines = []
    folder = "Custom-Emails"
    folder_files = os.listdir(folder)
    txt_files = 0

    os.makedirs(folder, exist_ok= True)

    print("="*70)
    print(f"\n{'Custom Email Analyzer':^70}\n")
    print("="*70)

    print("\nPaste your email below.\nType END on a new line when finished.\n")

    while True:

        line = input()

        if line.upper() == "END":
            break

        email_lines.append(line)

    content = "\n".join(email_lines)

    for file in folder_files:
        if file.endswith(".txt"):
            txt_files += 1

    folder_name = f"Email-{txt_files+1}.txt"
    full_path = os.path.join(folder,folder_name)

    with open(full_path, "w") as file:

        file.write(content)

    analyze_email(content)