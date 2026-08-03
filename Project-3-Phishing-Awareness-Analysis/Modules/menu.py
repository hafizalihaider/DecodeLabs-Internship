from Modules.email_loader import get_demo_emails
from Modules.multiple_email_analyzer import analyze_multiple_emails
from Modules.all_email_analyzer import analyze_all_emails


def display_banner():
     print("=" * 70)
     print()
     print(f"{'PHISHING AWARENESS ANALYZER':^70}\n")
     print("=" * 70)

def main_menu():

     while True:

          print(f"{'Main Menu':^70}")
          print("=" * 70)

          print("\n1. Analyze Demo Email")
          print("2. Analyze Custom Email")
          print("3. View Analysis Reports")
          print("0. Exit")
          print("-"*70)

          main_choice = input("\nEnter your choice: ")

          if main_choice.isdigit():

               main_choice = int(main_choice)
               if main_choice == 1:
                    email_analyzer_menu()

               elif main_choice == 2:
                    analyze_multiple_emails()

               elif main_choice == 3:
                    view_reports()

               elif main_choice == 0:
                    print("\nThank you for using Phishing Awareness Analyzer.")
                    break
               else:
                    print("\n[!] Invalid choice. Please select an option from 0-3.")

          else:
               print("\n[!] Invalid choice. Please select an option from 0-3.")


def email_analyzer_menu():

     while True:


          print("=" * 70)
          print(f"{'Email Analyzer':^70}")
          print("=" * 70)

          print("\n1. Analyze One Email")
          print("2. Analyze Multiple Emails")
          print("3. Analyze all Emails")
          print("0. Back")
          print("-"*70)
          
          sub_choice = input("\nEnter your choice: ")
     
          if sub_choice.isdigit():

               sub_choice = int(sub_choice)
               if sub_choice == 1:
                    get_demo_emails()
                    break


               elif sub_choice == 2:
                    analyze_multiple_emails()
                    break

               elif sub_choice == 3:
                    analyze_all_emails()
                    break

               elif sub_choice == 0:
                    break
               else:
                    print("\n[!] Invalid choice. Please select an option from 0-3.")
                            
          else:
               print("\n[!] Invalid choice. Please select an option from 0-3.")
