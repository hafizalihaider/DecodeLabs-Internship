
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
        print("-"*70)


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

                        print("-" * 70)
                        print(f"{email_list[email - 1]:^70}")
                        print("-" * 70)

                        print(content)

                        analyze_email(content)

                else:
                    print(f"[!] Email {email} does not exist.")

            else:
                print(f"[!] '{email}' is not a valid number.")