import os
from datetime import datetime
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

    current_time = datetime.now()
    date = current_time.strftime("%d %B, %Y")
    time = current_time.strftime("%I:%M %p")

    report_folder = "Reports/Demo-Email-Reports"
    
    os.makedirs(report_folder, exist_ok = True)

    report_count = len([file for file in os.listdir(report_folder) if file.endswith(".txt")])

    file_name_txt = f"{current_time.strftime('Phishing_Analysis_Report_%y_%m_%d')}_{report_count + 1 :03}.txt"
    file_path = os.path.join(report_folder, file_name_txt)

    with open(file_path, "w") as file:

        file.write("="*100 + "\n")
        file.write(f"{'PHISHING ANALYSIS REPORT':^100}\n")
        file.write("\n")
        file.write("="*100 + "\n")
        file.write("\n")

        file.write(f"{'Date: ' + date:<50}{'Time: ' + time:>50}\n")
        file.write("="*100 + "\n")

        file.write(f"\n{file_name_txt:^100}\n")
        file.write("="*100 + "\n")

        file.write(f"{'SUMMARY':^100}\n")
        file.write("="*100 + "\n")
        file.write("\n")

        file.write(f"\nHigh Risk Keywords: {len(high_risk_keywords)}\n")
        file.write("-"*100 + "\n")
        if high_risk_keywords:
            for keyword in high_risk_keywords:
                file.write(f"- {keyword}\n")
        else:
            file.write("No high risk keywords found.\n")
        file.write("\n")

        file.write(f"\nMedium Risk Keywords: {len(medium_risk_keywords)}\n")
        file.write("-"*100 + "\n")
        if medium_risk_keywords:
            for keyword in medium_risk_keywords:
                file.write(f"- {keyword}\n")
        else:
            file.write("No medium risk keywords found.\n")
        file.write("\n")

        file.write(f"\nLow Risk Keywords: {len(low_risk_keywords)}\n")
        file.write("-"*100 + "\n")
        if low_risk_keywords:
            for keyword in low_risk_keywords:
                file.write(f"- {keyword}\n")
        else:
            file.write("No low risk keywords found.\n")
        file.write("\n")

        file.write(f"\nTrusted URLs: {len(trusted_urls)}\n")
        file.write("-"*100 + "\n")
        if trusted_urls:
            for url in trusted_urls:
                file.write(f"- {url}\n")
        else:
            file.write("No trusted URLs found.\n")
        file.write("\n")

        file.write(f"\nSuspicious URLs: {len(suspicious_urls)}\n")
        file.write("-"*100 + "\n")
        if suspicious_urls:
            for url in suspicious_urls:
                file.write(f"- {url}\n")
        else:
            file.write("No suspicious URLs found.\n")
        file.write("\n")

        file.write(f"\nTrusted Domains: {len(trusted_domains)}\n")
        file.write("-"*100 + "\n")
        if trusted_domains:
            for domain in trusted_domains:
                file.write(f"- {domain}\n")
        else:
            file.write("No trusted domains found.\n")
        file.write("\n")

        file.write(f"\nUnknown Domains: {len(unknown_domains)}\n")
        file.write("-"*100 + "\n")
        if unknown_domains:
            for domain in unknown_domains:
                file.write(f"- {domain}\n")
        else:
            file.write("No unknown domains found.\n")
        file.write("\n")

        file.write(f"\nMalicious Domains: {len(malicious_domains)}\n")
        file.write("-"*100 + "\n")
        if malicious_domains:
            for domain in malicious_domains:
                file.write(f"- {domain}\n")
        else:
            file.write("No malicious domains found.\n")
        file.write("\n")

        file.write(f"\nHigh Risk Attachments: {len(high_risk_attachments)}\n")
        file.write("-"*100 + "\n")
        if high_risk_attachments:
            for attachment in high_risk_attachments:
                file.write(f"- {attachment}\n")
        else:
            file.write("No high risk attachments found.\n")
        file.write("\n")

        file.write(f"\nMedium Risk Attachments: {len(medium_risk_attachments)}\n")
        file.write("-"*100 + "\n")
        if medium_risk_attachments:
            for attachment in medium_risk_attachments:
                file.write(f"- {attachment}\n")
        else:
            file.write("No medium risk attachments found.\n")
        file.write("\n")

        file.write(f"\nLow Risk Attachments: {len(low_risk_attachments)}\n")
        file.write("-"*100 + "\n")
        if low_risk_attachments:
            for attachment in low_risk_attachments:
                file.write(f"- {attachment}\n") 
        else:
            file.write("No low risk attachments found.\n")
        file.write("\n")

        file.write(f"\nHigh Risk Grammar Patterns: {len(high_risk_grammar)}\n")
        file.write("-"*100 + "\n")
        if high_risk_grammar:
            for pattern in high_risk_grammar:
                file.write(f"- {pattern}\n")
        else:
            file.write("No high risk grammar patterns found.\n")
        file.write("\n")

        file.write(f"\nMedium Risk Grammar Patterns: {len(medium_risk_grammar)}\n")
        file.write("-"*100 + "\n")
        if medium_risk_grammar:
            for pattern in medium_risk_grammar:
                file.write(f"- {pattern}\n")
        else:
            file.write("No medium risk grammar patterns found.\n")
        file.write("\n")

        file.write(f"\nLow Risk Grammar Patterns: {len(low_risk_grammar)}\n")
        file.write("-"*100 + "\n")
        if low_risk_grammar:
            for pattern in low_risk_grammar:
                file.write(f"- {pattern}\n")
        else:
            file.write("No low risk grammar patterns found.\n")
        file.write("\n")

        file.write(f"\nHigh Risk Urgency Patterns: {len(high_risk_urgency)}\n")
        file.write("-"*100 + "\n")
        if high_risk_urgency:
            for pattern in high_risk_urgency:
                file.write(f"- {pattern}\n")
        else:
            file.write("No high risk urgency patterns found.\n")
        file.write("\n")

        file.write(f"\nMedium Risk Urgency Patterns: {len(medium_risk_urgency)}\n")
        file.write("-"*100 + "\n")
        if medium_risk_urgency:
            for pattern in medium_risk_urgency:
                file.write(f"- {pattern}\n")
        else:
            file.write("No medium risk urgency patterns found.\n")
        file.write("\n")

        file.write(f"\nLow Risk Urgency Patterns: {len(low_risk_urgency)}\n")
        file.write("-"*100 + "\n")
        if low_risk_urgency:
            for pattern in low_risk_urgency:
                file.write(f"- {pattern}\n")
        else:
            file.write("No low risk urgency patterns found.\n")
        file.write("\n")

        file.write(f"\nHigh Risk Spoofing Patterns: {len(high_risk_spoofing)}\n")
        file.write("-"*100 + "\n")
        if high_risk_spoofing:
            for pattern in high_risk_spoofing:
                file.write(f"- {pattern}\n")
        else:
            file.write("No high risk spoofing patterns found.\n")
        file.write("\n")

        file.write(f"\nMedium Risk Spoofing Patterns: {len(medium_risk_spoofing)}\n")
        file.write("-"*100 + "\n")
        if medium_risk_spoofing:
            for pattern in medium_risk_spoofing:
                file.write(f"- {pattern}\n")
        else:
            file.write("No medium risk spoofing patterns found.\n")
        file.write("\n")

        file.write(f"\nLow Risk Spoofing Patterns: {len(low_risk_spoofing)}\n")
        file.write("-"*100 + "\n")
        if low_risk_spoofing:
            for pattern in low_risk_spoofing:
                file.write(f"- {pattern}\n")
        else:
            file.write("No low risk spoofing patterns found.\n")
        file.write("\n")

        file.write("=" * 100 + "\n")
        file.write(f"{'FINAL VERDICT':^100}\n")
        file.write("-" * 100 + "\n")
        file.write(f"Risk Score : {score}/100\n")
        file.write(f"Risk Level : {level}\n")
        file.write("=" * 100 + "\n")