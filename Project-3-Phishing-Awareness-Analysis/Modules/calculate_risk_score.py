# ============================================================
# PHISHING AWARENESS ANALYZER
# ============================================================
#
# Author      : Hafiz Muhammad Ali Haider
# Date        : 09 August 2026
# Project     : Phishing Awareness Analysis
# File        : calculate_risk_score.py
#
# Description :
# Calculates the overall phishing risk score using the
# detected keywords, URLs, domains, attachments, grammar,
# urgency, and spoofing indicators.
#
# ============================================================


def calculate_risk_score(
     high_risk_keywords,
     medium_risk_keywords,
     low_risk_keywords,
     trusted_urls,
     suspicious_urls,
     trusted_domains,
     unknown_domains,
     malicious_domains,
     high_risk_attachments,
     medium_risk_attachments,
     low_risk_attachments,
     high_risk_grammar,
     medium_risk_grammar,
     low_risk_grammar,
     high_risk_urgency,
     medium_risk_urgency,
     low_risk_urgency,
     high_risk_spoofing,
     medium_risk_spoofing,
     low_risk_spoofing
):

     score = 0

     # Assign higher weights to indicators that are stronger
     # signs of phishing and lower weights to weaker indicators.
     # ---------- HIGH RISK ----------
     score += len(high_risk_keywords) * 12
     score += len(suspicious_urls) * 35
     score += len(malicious_domains) * 35
     score += len(high_risk_attachments) * 35
     score += len(high_risk_spoofing) * 30
     score += len(high_risk_urgency) * 15
     score += len(high_risk_grammar) * 12

     # ---------- MEDIUM RISK ----------
     score += len(medium_risk_keywords) * 5
     score += len(medium_risk_attachments) * 10
     score += len(medium_risk_spoofing) * 10
     score += len(medium_risk_urgency) * 5
     score += len(medium_risk_grammar) * 4

     # ---------- LOW RISK ----------
     score += len(low_risk_keywords) * 0.5
     score += len(unknown_domains) * 5
     score += len(low_risk_attachments) * 2
     score += len(low_risk_spoofing) * 2
     score += len(low_risk_urgency) * 1
     score += len(low_risk_grammar) * 1

     # Trusted sources reduce the overall risk score.
     # ==========================================
     # TRUST BONUS (LOWERS RISK)
     # ==========================================

     trust_bonus = (
          len(trusted_urls) * 15 +
          len(trusted_domains) * 20
     )

     score -= trust_bonus

     # Additional legitimate indicators help reduce
     # false positives for genuine emails.
     # ==========================================
     # LEGITIMATE INDICATORS BONUS
     # ==========================================

     if trusted_domains:
          score -= 5

     if trusted_urls:
          score -= 5

     # Keep the final score within the 0-100 range.
     # ==========================================
     # LIMIT SCORE
     # ==========================================

     score = max(0, min(score, 100))

     # Convert the numerical score into a readable
     # risk classification.
     # ==========================================
     # FINAL CLASSIFICATION
     # ==========================================

     if score <= 10:
          level = "SAFE"

     elif score <= 25:
          level = "LOW RISK"

     elif score <= 45:
          level = "SUSPICIOUS"

     elif score <= 100:
          level = "HIGH RISK"

     else:
          level = "CRITICAL PHISHING"

     return score, level