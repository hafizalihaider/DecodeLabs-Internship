from Modules.con

     high_risk_urgency = []
     medium_risk_urgency = []
     low_risk_urgency = []

     with open(URGENCY_PATTERNS, "r") as file:

          patterns = []

          for line in file:

               line = line.strip()

               if not line or line.startswith("#"):
                    continue
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
                    if pattern not in med