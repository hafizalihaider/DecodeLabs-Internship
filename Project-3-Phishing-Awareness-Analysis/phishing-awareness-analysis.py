# ==========================================
#        PHISHING AWARENESS ANALYZER
# ==========================================
import os

KEYWORDS_FILE = "Database/suspicious_keywords.txt"
TRUSTED_DOMAINS = "Database/trusted_domains.txt"
URL_PATTERNS = "Database/url_patterns.txt"


def display_banner():
     print("=" * 70)
     print()
     print(f"{'PHISHING AWARENESS ANALYZER':^70}\n")
     print("=" * 70)




def main_menu():

     print(f"{'Main Menu':^70}")
     print("=" * 70)

     print("\n1. Analyze Demo Email")
     print("2. Analyze Custom Email")
     print("3. View Analysis Reports")
     print("0. Exit")
     print("-"*70)

     while True:

          main_choice = input("\nEnter your choice: ")

          if main_choice.isdigit():

               main_choice = int(main_choice)
               if main_choice == 1:
                    email_analyzer_menu()

               elif main_choice == 2:
                    analyze_email()

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

     print("=" * 70)
     print(f"{'Email Analyzer':^70}")
     print("=" * 70)

     print("\n1. Analyze One Email")
     print("2. Analyze Multiple Emails")
     print("3. Analyze all Emails")
     print("0. Exit")
     print("-"*70)

     while True:
          
          sub_choice = input("\nEnter your choice: ")
     
          if sub_choice.isdigit():

               sub_choice = int(sub_choice)
               if sub_choice == 1:
                    get_demo_emails()


               elif sub_choice == 2:
                    get_demo_emails()

               elif sub_choice == 3:
                    print("Analyze all emails added soon.")

               elif sub_choice == 0:
                    break
               else:
                    print("\n[!] Invalid choice. Please select an option from 0-3.")
                            
          else:
               print("\n[!] Invalid choice. Please select an option from 0-3.")





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

     email_list.sort(key = lambda file: int(file.split("-")[1]))
     print(f"{len(email_list)} email(s) found!\n")

     for number,files in enumerate(email_list, 1):
          print(f"[{number:02}] {files}")
          
     print("\n[00] Back")
     print("-"*70)

     while True:

          demo_email_choice = input("\nEnter your choice: ")

          if demo_email_choice == "00":
               break

          if demo_email_choice.isdigit():

               demo_email_choice = int(demo_email_choice)

               if demo_email_choice >= 1 and demo_email_choice <= len(email_list):
                    read_demo_email(email_list[demo_email_choice - 1])

               else:
                    print(f"\n[!] Invalid selection. Please enter a number between 1-{len(email_list)}, {len(email_list)+1} for all emails, or [00] to go back.")

          else:
               print(f"\n[!] Invalid selection. Please enter a number between 1-{len(email_list)}, {len(email_list)+1} for all emails, or [00] to go back.")


def read_demo_email(file_name):

     path = os.path.join(r"Demo-Emails",file_name)

     with open(path , "r") as file:
          content = file.read()

     display_demo_email(content, file_name)


def display_demo_email(content, file_name):

     print()

     print("-"*70)
     print(f"{file_name:^70}")
     print("-"*70)
     print()
     print(content)


     print("-"*70)
     print("1. Analyze this Email")
     print("0. Back")
     print("-"*70)

     print()

     while True:

          analyzer_choice = input("Enter your choice: ")
          print()
          print()

          if analyzer_choice.isdigit():

               analyzer_choice = int(analyzer_choice)

               if analyzer_choice == 0:
                    break

               if analyzer_choice == 1:
                    analyze_email(content)
          else:
               print("Please enter 1 or 0.")




      
def check_keywords(content):

     content = content.lower()
     matched_keywords = []

     with open(KEYWORDS_FILE , "r") as file:
        
          for line in file:
            
               keyword = line.strip()

               if keyword in content:

                    matched_keywords.append(keyword)

          if matched_keywords:
            
               print("\nSuspicious keywords found:",len(matched_keywords))

               for keyword in matched_keywords:
                
                    print("-",keyword)

               return matched_keywords
                
          else:
               print("\nNo suspicious keywords found.")
               return []



def check_urls(content):

     content = content.lower()

     matched_urls = []
     words = content.split()

     with open(URL_PATTERNS , "r") as file:

          for line in file:

               url = line.strip()

               for word in words:

                    if url in word:

                         if word not in matched_urls:

                              matched_urls.append(word)

          if matched_urls:
               print("\nSuspicious url found:",len(matched_urls))

               for url in matched_urls:
                    print("-",url)
                
          else:
               print("\nNo suspicious url found.")


def check_sender(content):

     content = content.lower()

     matched_senders = []

     for line in content.splitlines():

          if line.startswith("from:"):

               sender = line.replace("from:","").strip()

               matched_senders.append(sender)

     if matched_senders:
          print("\nSender email(s) found:",len(matched_senders))

          for sender in matched_senders:
               print("-",sender)

          return matched_senders

     else:
          print("\nNo sender email(s) found.")
          return[]


def check_domain(sender):

     trusted_domains = []
     trusted_database = []
     suspicious_domains = []

     with open(TRUSTED_DOMAINS, "r") as file:

          for line in file:

               trusted_database.append(line.strip().lower())

          for line in sender:

               if "@" not in line:
                    continue

          domain = line.split("@")[1]

          if domain in trusted_database:
               if domain not in trusted_domains:
                    trusted_domains.append(domain)

          else:
               if domain not in suspicious_domains:
                    suspicious_domains.append(domain)


     if trusted_domains:
          print("\nTrusted domain(s) found:",len(trusted_domains))

          for domain in trusted_domains:
               print("-",domain)

     if suspicious_domains:
          print("\nSuspicious domain(s) found:",len(suspicious_domains))

          for domain in suspicious_domains:
               print("-",domain)


def analyze_email(content):

     check_keywords(content)
     check_urls(content)

     sender = check_sender(content)

     check_domain(sender)


display_banner()
main_menu()