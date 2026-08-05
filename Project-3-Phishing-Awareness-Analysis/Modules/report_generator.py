import os

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
        low_risk_spoofing
    ):

    report_folder = "Reports"
    report_count = 0
    reports = []
    
    os.makedirs(report_folder, exist_ok = True)
    folder = os.listdir(report_folder)

    for file in folder:

        reports.append(file)

        report_count += 1

    file_name = f"Report-{len(reports)}.txt"
    file_path = os.path.join(report_folder, file_name)

    with open(file_path, "w") as file:

        file.write("="*70 + "\n")
        file.write(f"{'Remarks':^70}\n")
        file.write("="*70 + "\n")

        file.write(f"\nHigh Risk Keywords: {len(high_risk_attachments)}"
        for keyword in high_risk_keywords:
            file.write(f"- {keyword}\n")

        file.write(f"\nMedium Risk Keywords: {len(medium_risk_attachments)}"
        for keyword in medium_risk_keywords:
            file.write(f"- {keyword}\n")

        file.write(f"\nLow Risk Keywords: {len(low_risk_attachments)}"
        for keyword in low_risk_keywords:
            file.write(f"- {keyword}\n")

        file.write(f"\nTrusted URLs: {len(trusted_urls)}")
        for url in trusted_urls:
            file.write(f"- {url}\n")

        file.write(f"\nSuspicious URLs: {len(suspicious_urls)}")
        for url in suspicious_urls:
            file.write(f"- {url}\n")

        file.write(f"\nTrusted Domains: {len(trusted_domains)}")
        for domain in trusted_domains:
            file.write(f"- {domain}\n")

        file.write(f"\nUnknown Domains: {len(unknown_domains)}")
        for domain in unknown_domains:
            file.write(f"- {domain}\n")

        file.write(f"\nMalicious Domains: {len(malicious_domains)}")
        for domain in malicious_domains:
            file.write(f"- {domain}\n")

        file.write(f"\nHigh Risk Attachments: {len(high_risk_attachments)}")
        for attachment in high_risk_attachments:
            file.write(f"- {attachment}\n")

        file.write(f"\nMedium Risk Attachments: {len(medium_risk_attachments)}")
        for attachment in medium_risk_attachments:
            file.write(f"- {attachment}\n")

        file.write(f"\nLow Risk Attachments: {len(low_risk_attachments)}")
        for attachment in low_risk_attachments:
            file.write(f"- {attachment}\n")

        file.write(f"\nHigh Risk Grammar Patterns: {len(high_risk_grammar)}")
        for pattern in high_risk_grammar:
            file.write(f"- {pattern}\n")

        file.write(f"\nMedium Risk Grammar Patterns: {len(medium_risk_grammar)}")
        for pattern in medium_risk_grammar:
            file.write(f"- {pattern}\n")

        file.write(f"\nLow Risk Grammar Patterns: {len(low_risk_grammar)}")
        for pattern in low_risk_grammar:
            file.write(f"- {pattern}\n")

        file.write(f"\nHigh Risk Urgency Patterns: {len(high_risk_urgency)}")
        for pattern in high_risk_urgency:
            file.write(f"- {pattern}\n")

        file.write(f"\nMedium Risk Urgency Patterns: {len(medium_risk_urgency)}")
        for pattern in medium_risk_urgency:
            file.write(f"- {pattern}\n")

        file.write(f"\nLow Risk Urgency Patterns: {len(low_risk_urgency)}")
        for pattern in low_risk_urgency:
            file.write(f"- {pattern}\n")

        file.write(f"\nHigh Risk Spoofing Patterns: {len(high_risk_spoofing)}")
        for pattern in high_risk_spoofing:
            file.write(f"- {pattern}\n")

        file.write(f"\nMedium Risk Spoofing Patterns: {len(medium_risk_spoofing)}")
        for pattern in medium_risk_spoofing:
            file.write(f"- {pattern}\n")

        file.write(f"\nLow Risk Spoofing Patterns: {len(low_risk_spoofing)}")
        for pattern in low_risk_spoofing:
            file.write(f"- {pattern}\n")