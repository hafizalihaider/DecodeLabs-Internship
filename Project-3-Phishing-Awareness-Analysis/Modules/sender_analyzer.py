from Modules.config import TRUSTED_DOMAINS
from Modules.config import MALICIOUS_DOMAINS

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
     unknown_domains = []
     malicious_domains = []

     trusted_database = []
     malicious_database = []

     with open(TRUSTED_DOMAINS, "r") as file:

          for line in file:

               trusted_database.append(line.strip().lower())

     with open(MALICIOUS_DOMAINS, "r") as file:

          for line in file:

               malicious_database.append(line.strip().lower())

     for line in sender:

          if "@" not in line:
               continue

          domain = line.split("@")[1]

          if domain in trusted_database:
               if domain not in trusted_domains:
                    trusted_domains.append(domain)

          elif domain in malicious_database:
               if domain not in malicious_domains:
                    malicious_domains.append(domain)

          elif ( domain.endswith(".edu")
                or domain.endswith(".edu.pk")
                or domain.endswith(".gov")
                or domain.endswith(".gov.pk")
                or domain.endswith(".ac.uk")
                or domain.endswith(".ac.in")
                or domain.endswith(".ac.nz")
          ):
               if domain not in trusted_domains:
                    trusted_domains.append(domain)

          else:
               if domain not in unknown_domains:
                    unknown_domains.append(domain)

     return trusted_domains, unknown_domains, malicious_domains