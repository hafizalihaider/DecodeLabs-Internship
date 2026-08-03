from Modules.config import KEYWORDS_FILE

def check_keywords(content):

     content = content.lower()
     high_risk_keywords = []
     medium_risk_keywords = []
     low_risk_keywords = []

     with open(KEYWORDS_FILE , "r") as file:

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
               key = lambda item: len(item[0]),
               reverse = True
          )

     for pattern, risk in patterns:

          if pattern in content:

               if risk == "HIGH":
                    if pattern not in high_risk_keywords:
                         high_risk_keywords.append(pattern)

               elif risk == "MEDIUM":
                    if pattern not in medium_risk_keywords:
                         medium_risk_keywords.append(pattern)

               elif risk == "LOW":
                    if pattern not in low_risk_keywords:
                         low_risk_keywords.append(pattern)

     return high_risk_keywords, medium_risk_keywords, low_risk_keywords
