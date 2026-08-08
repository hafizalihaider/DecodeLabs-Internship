# ============================================================
#
# PHISHING AWARENESS ANALYZER
#
# Author      : Hafiz Muhammad Ali Haider
# Date        : 09 August 2026
# Project     : Phishing Awareness Analysis
# File        : urgency_analyzer.py
#
# Description :
# Detects urgency-related indicators in an email by comparing
# its content against predefined urgency patterns and
# classifying detected patterns by risk level.
#
# ============================================================



from Modules.config import URGENCY_PATTERNS

def check_urgency(content):

     content = content.lower()

     high_risk_urgency = []
     medium_risk_urgency = []
     low_risk_urgency = []

     with open(URGENCY_PATTERNS, "r") as file:

          patterns = []

          for line in file:

               line = line.strip()

               if not line or line.startswith("#"):
                    continue

               pattern, risk = line.split(":")

               pattern = pattern.strip().lower()
               risk = risk.strip().upper()

               patterns.append((pattern, risk))

          patterns.sort(
               key=lambda item: len(item[0]),
               reverse=True
          )

     for pattern, risk in patterns:

          if pattern in content:
               if risk == "HIGH":
                    if pattern not in high_risk_urgency:
                         high_risk_urgency.append(pattern)

               elif risk == "MEDIUM":
                    if pattern not in medium_risk_urgency:
                         medium_risk_urgency.append(pattern)

               elif risk == "LOW":
                    if pattern not in low_risk_urgency:
                         low_risk_urgency.append(pattern)

     return high_risk_urgency, medium_risk_urgency, low_risk_urgency