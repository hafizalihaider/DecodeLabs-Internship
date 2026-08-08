from Modules.email_analyzer import analyze_email
import os

def analyze_custom_email():

    email_lines = []
    folder = "Custom-Emails"
    txt_files = 0

    os.makedirs(folder, exist_ok= True)
    folder_files = os.listdir(folder)

    print("="*100)
    print(f"\n{'Custom Email Analyzer':^100}\n")
    print("="*100)

    print("\nPaste your email below.\nType END on a new line when finished.\n")

    while True:

        line = input()

        if line.upper() == "END":
            break

        email_lines.append(line)

    content = "\n".join(email_lines)

    if not email_lines:
        print("[!] No email entered.")
        return

    for file in folder_files:
        if file.endswith(".txt"):
            txt_files += 1

    folder_name = f"Email-{txt_files+1}.txt"
    full_path = os.path.join(folder,folder_name)

    with open(full_path, "w") as file:

        file.write(content)

    print(f"\n[✓] Email saved as '{folder_name}'.")

    analyze_email(content, file_name=None)