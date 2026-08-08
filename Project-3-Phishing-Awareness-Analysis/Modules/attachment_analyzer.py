# ============================================================
# PHISHING AWARENESS ANALYZER
# ============================================================
#
# Author      : Hafiz Muhammad Ali Haider
# Date        : 09 August 2026
# Project     : Phishing Awareness Analysis
# File        : attachment_analyzer.py
#
# Description :
# Detects potentially dangerous email attachments by comparing
# file extensions against predefined attachment risk patterns.
#
# ============================================================

from Modules.config import ATTACHMENT_KEYWORDS


def analyze_attachment(content):

     high_risk_attachments = []
     medium_risk_attachments = []
     low_risk_attachments = []

     content = content.lower()

     words = content.split()

     # Load attachment extensions and their assigned risk levels.
     with open(ATTACHMENT_KEYWORDS, "r") as file:

          patterns = []

          for line in file:

               line = line.strip()

               if not line or line.startswith("#") or not "@" in line:
                    continue

               pattern, risk = line.split(":")

               pattern = pattern.strip().lower()
               risk = risk.strip().upper()

               patterns.append((pattern, risk))

          # Check longer extensions first to avoid partial matches.
          patterns.sort(
               key=lambda item: len(item[0]),
               reverse=True
          )

     # Match words in the email against known attachment extensions.
     for word in words:

          word = word.strip(".,!?;:(){}[]<>\"'")

          for pattern, risk in patterns:

               if word.endswith(pattern):

                    if risk == "HIGH":
                         if word not in high_risk_attachments:
                              high_risk_attachments.append(word)

                    elif risk == "MEDIUM":
                         if word not in medium_risk_attachments:
                              medium_risk_attachments.append(word)

                    elif risk == "LOW":
                         if word not in low_risk_attachments:
                              low_risk_attachments.append(word)

     return high_risk_attachments, medium_risk_attachments, low_risk_attachments