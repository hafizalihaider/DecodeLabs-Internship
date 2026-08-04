

               line = line.strip()

               if not line or line.startswith("#") or not "@" in line:
                    continue

               pattern, risk = line.split(":")

               pattern = pattern.strip().lower()
               risk = risk.strip().upper()

               patterns.append((pattern, risk))

          patterns.sort(
          key=lambda item: len(item[0]),
          reverse=True
          )

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