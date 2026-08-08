# ============================================================
#
# PHISHING AWARENESS ANALYZER
#
# Author      : Hafiz Muhammad Ali Haider
# Date        : 09 August 2026
# Project     : Phishing Awareness Analysis
# File        : url_analyzer.py
#
# Description :
# Extracts URLs from email content and analyzes them by
# comparing their domains against trusted domains to identify
# trusted and suspicious URLs.
#
# ============================================================




from urllib.parse import urlparse
from Modules.config import URL_PATTERNS, TRUSTED_DOMAINS


def extract_urls(content):

     content = content.lower()

     matched_urls = []
     words = content.split()

     with open(URL_PATTERNS , "r") as file:

          for line in file:

               url = line.strip()

               if not line or line.startswith("#"):
                    continue

               for word in words:

                    if url in word:

                         if word not in matched_urls:

                              matched_urls.append(word)

          if matched_urls:
               return matched_urls
                
          else:
               return []

def analyze_urls(urls):

     trusted_urls = []
     trusted_database = []
     suspicious_urls = []

     with open(TRUSTED_DOMAINS, "r") as file:

          for line in file:

               trusted_database.append(line.strip().lower())

     for url in urls:

          domain = urlparse(url).netloc.lower()

          if domain.startswith("www."):
               domain = domain[4:]

          if domain in trusted_database:
               trusted_urls.append(url)

          else:
               suspicious_urls.append(url)

     return trusted_urls,suspicious_urls