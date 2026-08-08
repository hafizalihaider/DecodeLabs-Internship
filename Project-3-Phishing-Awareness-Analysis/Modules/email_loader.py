import os
from Modules.email_analyzer import analyze_email
from Modules.report_generator import generate_report
def get_demo_emails():

     while True:

          print("="*100)
          print(f"{'Demo Email Analyzer':^100}")
          print("="*100)

          print()

          email_list = []

          folder = os.listdir("Demo-Emails")

          for file in folder:
               if file.endswith(".txt"):
                    email_list.append(file)

          email_list.sort(key = lambda file: int(file.split("-")[1]))

          print()
          print("=" * 100)
          print(f"{'AVAILABLE DEMO EMAILS':^100}")
          print("=" * 100)
          print(f"\nTotal Reports : {len(email_list)}\n")
          print("Select only one option:\n")

          for number,files in enumerate(email_list, 1):
               print(f"[{number:02}] {files}")
               
          print("\n[00] Back")
          print("-"*100)

          demo_email_choice = input("\nEnter your choice: ")

          if demo_email_choice == "00":
               break

          if demo_email_choice.isdigit():

               demo_email_choice = int(demo_email_choice)

               if demo_email_choice >= 1 and demo_email_choice <= len(email_list):
                    return_value = read_demo_email(email_list[demo_email_choice - 1])

                    if return_value:
                         break

               else:
                    print(f"[!] Email {demo_email_choice} does not exist.")

          else:
               print(f"[!] '{demo_email_choice}' is not a valid number.")


def read_demo_email(file_name):

     path = os.path.join(r"Demo-Emails",file_name)

     with open(path , "r") as file:
          content = file.read()

     return display_demo_email(content, file_name)


def load_demo_email(file_name):

     path = os.path.join("Demo-Emails", file_name)

     with open(path, "r") as file:
          print()
          return file.read()

    
def display_demo_email(content, file_name):

     while True:

          print()

          print("-"*100)
          print(f"{file_name:^100}")
          print("-"*100)
          print()
          print(content)


          print("-"*100)
          print("1. Analyze this Email")
          print("0. Back")
          print("-"*100)

          print()

          analyzer_choice = input("Enter your choice: ")
          print()
          print()

          if analyzer_choice.isdigit():

               analyzer_choice = int(analyzer_choice)

               if analyzer_choice == 0:
                    break

               if analyzer_choice == 1:

                    email_report_data = analyze_email(content)

                    email_report_data["file_name"] = file_name


                    while True:

                         print()
                         print("=" * 100)
                         print(f"{'REPORT MENU':^100}")
                         print("=" * 100)
                         print()
                         print("1. Generate Report")
                         print("0. Cancel")
                         print("-" * 100)

                         report_choice = input("\nEnter your choice: ").strip()

                         if report_choice == "1":

                              report_data = email_report_data.copy()
                              report_data.pop("file_name", None)

                              generate_report(**report_data)

                              print("\n✓ Report generated successfully.")
                              input("\nPress Enter to return to Email Analyzer Menu...")
                              return True

                         elif report_choice == "0":

                              print("\n[!] Report generation cancelled.")
                              input("\nPress Enter to return to Email Analyzer Menu...")
                              return True

                         else:

                              print("\n[!] Invalid choice. Please enter 1 or 0.")

          else:
               print("Please enter 1 or 0.")
