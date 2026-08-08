import os
from datetime import datetime

def write_report_content(file, report_data):

    file.write("=" * 100 + "\n")
    file.write(f"{'FINAL VERDICT':^100}\n")
    file.write("=" * 100 + "\n")
    file.write(f"Risk Score : {report_data['score']}/100\n")
    file.write(f"Risk Level : {report_data['level']}\n")
    file.write("=" * 100 + "\n")

    file.write("\n")
    file.write("=" * 100 + "\n")
    file.write(f"{'KEYWORD ANALYSIS':^100}\n")
    file.write("=" * 100 + "\n")

    file.write(f"\nHigh Risk Keywords: {len(report_data['high_risk_keywords'])}\n")
    file.write("-"*100 + "\n")
    if report_data['high_risk_keywords']:
        for keyword in report_data['high_risk_keywords']:
            file.write(f"- {keyword}\n")
    else:
        file.write("No high risk keywords found.\n")
    file.write("\n")

    file.write(f"\nMedium Risk Keywords: {len(report_data['medium_risk_keywords'])}\n")
    file.write("-"*100 + "\n")
    if report_data['medium_risk_keywords']:
        for keyword in report_data['medium_risk_keywords']:
            file.write(f"- {keyword}\n")
    else:
        file.write("No medium risk keywords found.\n")
    file.write("\n")

    file.write(f"\nLow Risk Keywords: {len(report_data['low_risk_keywords'])}\n")
    file.write("-"*100 + "\n")
    if report_data['low_risk_keywords']:
        for keyword in report_data['low_risk_keywords']:
            file.write(f"- {keyword}\n")
    else:
        file.write("No low risk keywords found.\n")
    file.write("\n")

    file.write("\n")
    file.write("=" * 100 + "\n")
    file.write(f"{'URL ANALYSIS':^100}\n")
    file.write("=" * 100 + "\n")

    file.write(f"\nTrusted URLs: {len(report_data['trusted_urls'])}\n")
    file.write("-"*100 + "\n")
    if report_data['trusted_urls']:
        for url in report_data['trusted_urls']:
            file.write(f"- {url}\n")
    else:
        file.write("No trusted URLs found.\n")
    file.write("\n")

    file.write(f"\nSuspicious URLs: {len(report_data['suspicious_urls'])}\n")
    file.write("-"*100 + "\n")
    if report_data['suspicious_urls']:
        for url in report_data['suspicious_urls']:
            file.write(f"- {url}\n")
    else:
        file.write("No suspicious URLs found.\n")
    file.write("\n")

    file.write("\n")
    file.write("=" * 100 + "\n")
    file.write(f"{'DOMAIN ANALYSIS':^100}\n")
    file.write("=" * 100 + "\n")

    file.write(f"\nTrusted Domains: {len(report_data['trusted_domains'])}\n")
    file.write("-"*100 + "\n")
    if report_data['trusted_domains']:
        for domain in report_data['trusted_domains']:
            file.write(f"- {domain}\n")
    else:
        file.write("No trusted domains found.\n")
    file.write("\n")

    file.write(f"\nUnknown Domains: {len(report_data['unknown_domains'])}\n")
    file.write("-"*100 + "\n")
    if report_data['unknown_domains']:
        for domain in report_data['unknown_domains']:
            file.write(f"- {domain}\n")
    else:
        file.write("No unknown domains found.\n")
    file.write("\n")

    file.write(f"\nMalicious Domains: {len(report_data['malicious_domains'])}\n")
    file.write("-"*100 + "\n")
    if report_data['malicious_domains']:
        for domain in report_data['malicious_domains']:
            file.write(f"- {domain}\n")
    else:
        file.write("No malicious domains found.\n")
    file.write("\n")

    file.write("\n")
    file.write("=" * 100 + "\n")
    file.write(f"{'ATTACHMENT ANALYSIS':^100}\n")
    file.write("=" * 100 + "\n")

    file.write(f"\nHigh Risk Attachments: {len(report_data['high_risk_attachments'])}\n")
    file.write("-"*100 + "\n")
    if report_data['high_risk_attachments']:
        for attachment in report_data['high_risk_attachments']:
            file.write(f"- {attachment}\n")
    else:
        file.write("No high risk attachments found.\n")
    file.write("\n")

    file.write(f"\nMedium Risk Attachments: {len(report_data['medium_risk_attachments'])}\n")
    file.write("-"*100 + "\n")
    if report_data['medium_risk_attachments']:
        for attachment in report_data['medium_risk_attachments']:
            file.write(f"- {attachment}\n")
    else:
        file.write("No medium risk attachments found.\n")
    file.write("\n")

    file.write(f"\nLow Risk Attachments: {len(report_data['low_risk_attachments'])}\n")
    file.write("-"*100 + "\n")
    if report_data['low_risk_attachments']:
        for attachment in report_data['low_risk_attachments']:
            file.write(f"- {attachment}\n") 
    else:
        file.write("No low risk attachments found.\n")
    file.write("\n")

    file.write("\n")
    file.write("=" * 100 + "\n")
    file.write(f"{'GRAMMAR ANALYSIS':^100}\n")
    file.write("=" * 100 + "\n")

    file.write(f"\nHigh Risk Grammar Patterns: {len(report_data['high_risk_grammar'])}\n")
    file.write("-"*100 + "\n")
    if report_data['high_risk_grammar']:
        for pattern in report_data['high_risk_grammar']:
            file.write(f"- {pattern}\n")
    else:
        file.write("No high risk grammar patterns found.\n")
    file.write("\n")

    file.write(f"\nMedium Risk Grammar Patterns: {len(report_data['medium_risk_grammar'])}\n")
    file.write("-"*100 + "\n")
    if report_data['medium_risk_grammar']:
        for pattern in report_data['medium_risk_grammar']:
            file.write(f"- {pattern}\n")
    else:
        file.write("No medium risk grammar patterns found.\n")
    file.write("\n")

    file.write(f"\nLow Risk Grammar Patterns: {len(report_data['low_risk_grammar'])}\n")
    file.write("-"*100 + "\n")
    if report_data['low_risk_grammar']:
        for pattern in report_data['low_risk_grammar']:
            file.write(f"- {pattern}\n")
    else:
        file.write("No low risk grammar patterns found.\n")
    file.write("\n")

    file.write("\n")
    file.write("=" * 100 + "\n")
    file.write(f"{'URGENCY ANALYSIS':^100}\n")
    file.write("=" * 100 + "\n")

    file.write(f"\nHigh Risk Urgency Patterns: {len(report_data['high_risk_urgency'])}\n")
    file.write("-"*100 + "\n")
    if report_data['high_risk_urgency']:
        for pattern in report_data['high_risk_urgency']:
            file.write(f"- {pattern}\n")
    else:
        file.write("No high risk urgency patterns found.\n")
    file.write("\n")

    file.write(f"\nMedium Risk Urgency Patterns: {len(report_data['medium_risk_urgency'])}\n")
    file.write("-"*100 + "\n")
    if report_data['medium_risk_urgency']:
        for pattern in report_data['medium_risk_urgency']:
            file.write(f"- {pattern}\n")
    else:
        file.write("No medium risk urgency patterns found.\n")
    file.write("\n")

    file.write(f"\nLow Risk Urgency Patterns: {len(report_data['low_risk_urgency'])}\n")
    file.write("-"*100 + "\n")
    if report_data['low_risk_urgency']:
        for pattern in report_data['low_risk_urgency']:
            file.write(f"- {pattern}\n")
    else:
        file.write("No low risk urgency patterns found.\n")
    file.write("\n")

    file.write("\n")
    file.write("=" * 100 + "\n")
    file.write(f"{'SPOOFING ANALYSIS':^100}\n")
    file.write("=" * 100 + "\n")

    file.write(f"\nHigh Risk Spoofing Patterns: {len(report_data['high_risk_spoofing'])}\n")
    file.write("-"*100 + "\n")
    if report_data['high_risk_spoofing']:
        for pattern in report_data['high_risk_spoofing']:
            file.write(f"- {pattern}\n")
    else:
        file.write("No high risk spoofing patterns found.\n")
    file.write("\n")

    file.write(f"\nMedium Risk Spoofing Patterns: {len(report_data['medium_risk_spoofing'])}\n")
    file.write("-"*100 + "\n")
    if report_data['medium_risk_spoofing']:
        for pattern in report_data['medium_risk_spoofing']:
            file.write(f"- {pattern}\n")
    else:
        file.write("No medium risk spoofing patterns found.\n")
    file.write("\n")

    file.write(f"\nLow Risk Spoofing Patterns: {len(report_data['low_risk_spoofing'])}\n")
    file.write("-"*100 + "\n")
    if report_data['low_risk_spoofing']:
        for pattern in report_data['low_risk_spoofing']:
            file.write(f"- {pattern}\n")
    else:
        file.write("No low risk spoofing patterns found.\n")
    file.write("\n")


def generate_report(

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
        low_risk_spoofing,

        score,
        level
    ):

    folder = ""

    current_time = datetime.now()
    date = current_time.strftime("%d %B, %Y")
    time = current_time.strftime("%I:%M %p")

    report_folder = "Reports"
    
    os.makedirs(report_folder, exist_ok = True)

    if level == "SAFE":
        folder = "Safe"

    elif level == "LOW RISK":
        folder = "Low_Risk"

    elif level == "SUSPICIOUS":
        folder = "Suspicious"

    elif level == "HIGH RISK":
        folder = "High_Risk"

    elif level == "CRITICAL PHISHING":
        folder = "Critical_Phishing"


    folder_path = os.path.join(report_folder, folder)
    os.makedirs(folder_path, exist_ok = True)

    report_count = len([file for file in os.listdir(folder_path) if file.endswith(".txt")])
    report_id = f"{current_time.strftime('%y_%m_%d')}_{report_count + 1:03}"

    file_name_txt = f"{current_time.strftime('Phishing_Analysis_Report_%y_%m_%d')}_{report_count + 1 :03}.txt"
    file_path = os.path.join(folder_path, file_name_txt)

    with open(file_path, "w") as file:

        file.write("=" * 100 + "\n")
        file.write(f"\n{'PHISHING ANALYSIS REPORT':^100}\n")
        file.write("\n")
        file.write("=" * 100 + "\n\n")

        file.write(f"Report ID  : {report_id}\n")
        file.write(f"Date       : {date}\n")
        file.write(f"Time       : {time}\n")
        file.write(f"File Name  : {file_name_txt}\n\n")

        write_report_content(file, {
            "high_risk_keywords": high_risk_keywords,
            "medium_risk_keywords": medium_risk_keywords,
            "low_risk_keywords": low_risk_keywords,

            "trusted_urls": trusted_urls,
            "suspicious_urls": suspicious_urls,

            "trusted_domains": trusted_domains,
            "unknown_domains": unknown_domains,
            "malicious_domains": malicious_domains,

            "high_risk_attachments": high_risk_attachments,
            "medium_risk_attachments": medium_risk_attachments,
            "low_risk_attachments": low_risk_attachments,

            "high_risk_grammar": high_risk_grammar,
            "medium_risk_grammar": medium_risk_grammar,
            "low_risk_grammar": low_risk_grammar,

            "high_risk_urgency": high_risk_urgency,
            "medium_risk_urgency": medium_risk_urgency,
            "low_risk_urgency": low_risk_urgency,

            "high_risk_spoofing": high_risk_spoofing,
            "medium_risk_spoofing": medium_risk_spoofing,
            "low_risk_spoofing": low_risk_spoofing,

            "score": score,
            "level": level
        })