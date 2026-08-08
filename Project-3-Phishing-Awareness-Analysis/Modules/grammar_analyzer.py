# ============================================================
# PHISHING AWARENESS ANALYZER
# ============================================================
#
# Author      : Hafiz Muhammad Ali Haider
# Date        : 09 August 2026
# Project     : Phishing Awareness Analysis
# File        : grammar_analyzer.py
#
# Description :
# Checks email content for suspicious grammar patterns and
# classifies detected patterns according to their risk level.
#
# ============================================================


from Modules.config import GRAMMAR_PATTERNS


def check_grammar(content):

    content = content.lower()

    high_risk_grammar = []
    medium_risk_grammar = []
    low_risk_grammar = []

    # Load and classify grammar patterns from the database
    with open(GRAMMAR_PATTERNS, "r") as file:

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
                    if pattern not in high_risk_grammar:
                        high_risk_grammar.append(pattern)

                elif risk == "MEDIUM":
                    if pattern not in medium_risk_grammar:
                        medium_risk_grammar.append(pattern)

                elif risk == "LOW":
                    if pattern not in low_risk_grammar:
                        low_risk_grammar.append(pattern)

    return high_risk_grammar, medium_risk_grammar, low_risk_grammar