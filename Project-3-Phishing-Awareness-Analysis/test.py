sender = """support@paypal.com
hacker@papol.com"""
TRUSTED_DOMAINS = "Database/trusted_domains.txt"

def check_domain(senders):

     trusted_database = []

     with open(TRUSTED_DOMAINS, "r") as file:
          for line in file:
               trusted_database.append(line.strip())

     for sender in senders:

          domain = sender.split("@")[1]

          if domain in trusted_database:
               print("Trusted:", domain)

          else:
               print("Suspicious:", domain)
check_domain(sender)