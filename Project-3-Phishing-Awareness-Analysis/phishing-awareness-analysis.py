# ==========================================
#        PHISHING AWARENESS ANALYZER
# ==========================================
import os

KEYWORDS_FILE = "Database/suspicious_keywords.txt"
TRUSTED_DOMAINS = "Database/trusted_domains.txt"
URL_PATTERNS = "Database/url_patterns.txt"
ATTACHMENT_KEYWORDS = "Database/attachment_keywords.txt"
GRAMMAR_PATTERNS = "Database/grammar_patterns.txt"
URGENCY_PATTERNS = "Database/urgency_patterns.txt"


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
               return matched_keywords
                
          else:
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
               return matched_urls
                
          else:
               return []


def check_sender(content):

     content = content.lower()

     matched_senders = []

     for line in content.splitlines():

          if line.startswith("from:"):

               sender = line.replace("from:","").strip()

               matched_senders.append(sender)

     if matched_senders:
          return matched_senders

     else:
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
          return trusted_domains

     if suspicious_domains:
          return suspicious_domains


def check_attachments(content):

     content = content.lower()
     matched_attachments = []

     with open(ATTACHMENT_KEYWORDS , "r") as file:
        
          for line in file:
            
               attachments = line.strip()

               if attachments in content and attachments not in matched_attachments:
                    matched_attachments.append(attachments)

     if matched_attachments:
          return matched_attachments
               
     else:
          return []


def check_grammar(content):

     content = content.lower()
     matched_grammar = []

     with open(GRAMMAR_PATTERNS , "r") as file:
        
          for line in file:
            
               pattern = line.strip().lower()

               if not pattern or pattern.startswith("#"):
                    continue

               if pattern in content and pattern not in matched_grammar:
                    matched_grammar.append(pattern)

     if matched_grammar:
          return matched_grammar
               
     else:
          return []


def check_urgency(content):

     content = content.lower()

     matched_urgency = []

     with open(URGENCY_PATTERNS, "r") as file:

          for line in file:

               pattern = line.strip().lower()

               if not pattern or pattern.startswith("#"):
                    continue

               if pattern in content and pattern not in matched_urgency:
                    matched_urgency.append(pattern)

     if matched_urgency:
          return matched_urgency

     else:
          return []

           
def analyze_email(content):

     keywords = check_keywords(content)
     urls = check_urls(content)
     senders = check_sender(content)
     domains = check_domain(senders)
     attachments = check_attachments(content)
     grammar = check_grammar(content)
     urgency = check_urgency(content)

     print("\nSuspicious keywords:", len(keywords))
     for keyword in keywords:
          print("-", keyword)

     print("\nSuspicious URLs:", len(urls))
     for url in urls:
          print("-", url)

     print("\nSender(s):", len(senders))
     for sender in senders:
          print("-", sender)

     print("\nSuspicious domains:", len(domains))
     for domain in domains:
          print("-", domain)

     print("\nSuspicious Attachment:", len(attachments))
     for attachment in attachments:
          print("-", attachment)

     print("\nSuspicious writing patterns found:", len(grammar))
     for word in grammar:
          print("-", word)

     print("\nUrgency indicators found:", len(urgency))

     for pattern in urgency:
          print("-", pattern)

display_banner()
main_menu()