import os
from Modules.email_analyzer import analyze_email

def get_demo_emails():

     while True:

          print("="*100)
          print(f"{'Demo Email Analyzer':^100}")
          print("="*100)

          print()
          print("Select only one option:\n")

          email_list = []

          folder = os.listdir("Demo-Emails")

          for file in folder:
               if file.endswith(".txt"):
                    email_list.append(file)

          email_list.sort(key = lambda file: int(file.split("-")[1]))
          print(f"{len(email_list)} email(s) found!\n")

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
                    read_demo_email(email_list[demo_email_choice - 1])

               else:
                    print(f"[!] Email {demo_email_choice} does not exist.")

          else:
               print(f"[!] '{demo_email_choice}' is not a valid number.")


def read_demo_email(file_name):

     path = os.path.join(r"Demo-Emails",file_name)

     with open(path , "r") as file:
          content = file.read()

     display_demo_email(content, file_name)


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
                    analyze_email(content)
                    break
          else:
               print("Please enter 1 or 0.")
