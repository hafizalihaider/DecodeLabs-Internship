# ==========================================
#        PHISHING AWARENESS ANALYZER
# ==========================================
import os

def display_banner():
    print("=" * 70)
    print()
    print(f"{'PHISHING AWARENESS ANALYZER':^70}\n")
    print("=" * 70)

def main_menu():

        print("-" * 70)
        print(f"{'Main Menu':^70}")
        print("-" * 70)

        print("\n1. Analyze Demo Email")
        print("2. Analyze Custom Email")
        print("3. View Analysis Reports")
        print("4. Exit")

        while True:

                choice = input("\nEnter your choice: ")

                if choice.isdigit():
                       choice = int(choice)
                       if choice == 1:
                            get_demo_emails()


                       elif choice == 2:
                           analyze_custom_email()


                       elif choice == 3:
                            view_reports()

                       elif choice == 4:
                            print("\nThank you for using Phishing Awareness Analyzer.")
                            break
                       else:
                            print("\n[!] Invalid choice. Please select an option from 1-4.")

                else:
                        print("\n[!] Invalid choice. Please select an option from 1-4.")
    
def get_demo_emails():

    print("="*70)
    print(f"{'Demo Email Analyzer':^70}")
    print("="*70)
    print()
    print("Select only one option:\n")

    email_list = []

    folder = os.listdir("Demo-Emails")

    for file in folder:
        if file.endswith(".txt"):
              email_list.append(file)

    print(f"\n{len(email_list)} email(s) found!\n")

    for number,files in enumerate(email_list, 1):
          print(f"[{number:02}] {files}")
          

    print(f"[{len(email_list) + 1}] All of them")
    print("\n[00] Back")
    

    while True:

        choice = input("\nEnter your choice: ")

        if choice == "00":
              break

        if choice.isdigit():

                choice = int(choice)

                if choice >= 1 and choice <= len(email_list):
                      print("Selected:", email_list[choice - 1])

                elif choice == len(email_list) + 1:
                      print("Analyzing all emails...")

                else:
                      print(f"\n[!] Invalid selection. Please enter a number between 1-{len(email_list)}, {len(email_list)+1} for all emails, or [00] to go back.")

        else:
              print(f"\n[!] Invalid selection. Please enter a number between 1-{len(email_list)}, {len(email_list)+1} for all emails, or [00] to go back.")

def analyze_demo_email():
    print("\n[Analyze Demo Email]")
    print("Feature will be added soon.")



def analyze_custom_email():
    print("\n[Analyze Custom Email]")
    print("Feature will be added soon.")



def view_reports():
    print("\n[View Analysis Reports]")
    print("Feature will be added soon.")


display_banner()
main_menu()