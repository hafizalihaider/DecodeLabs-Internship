from urll
def extract_urls(content):

     content = content.lower()

     matched_urls = []
     words = content.split()

     with open(URL_PATTERNS , "r") as file:

          for line in file
          if matched_urls:
               return matched_urls
                
          else:
               return []

def analyze_urls(urls):

     trusted_urls = []
     trusted_database = []
     suspicious_ur

          if domain.startswith("www."):
               domain = domain[4:]

          if domain in trusted_database:
               trusted_urls.append(url)

