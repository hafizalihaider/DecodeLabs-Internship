from Modules.keyword_analyzer import check_keywords
from Modules.url_analyzer import extract_urls, analyze_urls
from Modules.sender_analyzer import check_sender, check_domain
from Modules.attachment_analyzer import analyze_attachment
from Modules.grammar_analyzer import check_grammar
from Modules.urgency_analyzer import check_urgency
from Modules.spoofing_analyzer import check_spoofing
from Modules.calculate_risk_score import calculate_risk_score

def analyze_email(content):

     high_risk_keywords, medium_risk_keywords, low_risk_keywords = check_keywords(content)

     urls = extract_urls(content)
     trusted_urls, suspicious_urls = analyze_urls(urls)

     senders = check_sender(content)
     trusted_domains, unknown_domains, malicious_domains = check_domain(senders)

     high_risk_attachments, medium_risk_attachments, low_risk_attachments = analyze_attachment(content)

     high_risk_grammar, medium_risk_grammar, low_risk_grammar = check_grammar(content)
     high_risk_urgency, medium_risk_urgency, low_risk_urgency = check_urgency(content)
     high_risk_spoofing, medium_risk_spoofing, low_risk_spoofing = check_spoofing(content)

     print("="*70)
     print(f"{'Remarks':^70}")
     print("="*70)
     print("\nHigh Risk Keywords:", len(high_risk_keywords))
     for keyword in high_risk_keywords:
          print("-", keyword)

     print("\nMedium Risk Keywords:", len(medium_risk_keywords))
     for keyword in medium_risk_keywords:
          print("-", keyword)

     print("\nLow Risk Keywords:", len(low_risk_keywords))
     for keyword in low_risk_keywords:
          print("-", keyword)

     print("\nTrusted URLs:", len(trusted_urls))
     for url in trusted_urls:
          print("-", url)

     print("\nSuspicious URLs:", len(suspicious_urls))
     for url in suspicious_urls:
          print("-", url)

     print("\nTrusted Domains:", len(trusted_domains))
     for domain in trusted_domains:
          print("-", domain)

     print("\nUnknown Domains:", len(unknown_domains))
     for domain in unknown_domains:
          print("-", domain)

     print("\nMalicious Domains:", len(malicious_domains))
     for domain in malicious_domains:
          print("-", domain)

     print("\nHigh Risk Attachments:", len(high_risk_attachments))
     for attachment in high_risk_attachments:
          print("-", attachment)

     print("\nMedium Risk Attachments:", len(medium_risk_attachments))
     for attachment in medium_risk_attachments:
          print("-", attachment)

     print("\nLow Risk Attachments:", len(low_risk_attachments))
     for attachment in low_risk_attachments:
          print("-", attachment)

     print("\nHigh Risk Grammar Patterns:", len(high_risk_grammar))
     for pattern in high_risk_grammar:
          print("-", pattern)

     print("\nMedium Risk Grammar Patterns:", len(medium_risk_grammar))
     for pattern in medium_risk_grammar:
          print("-", pattern)

     print("\nLow Risk Grammar Patterns:", len(low_risk_grammar))
     for pattern in low_risk_grammar:
          print("-", pattern)

     print("\nHigh Risk Urgency Patterns:", len(high_risk_urgency))
     for pattern in high_risk_urgency:
          print("-", pattern)

     print("\nMedium Risk Urgency Patterns:", len(medium_risk_urgency))
     for pattern in medium_risk_urgency:
          print("-", pattern)

     print("\nLow Risk Urgency Patterns:", len(low_risk_urgency))
     for pattern in low_risk_urgency:
          print("-", pattern)

     print("\nHigh Risk Spoofing Patterns:", len(high_risk_spoofing))
     for pattern in high_risk_spoofing:
          print("-", pattern)

     print("\nMedium Risk Spoofing Patterns:", len(medium_risk_spoofing))
     for pattern in medium_risk_spoofing:
          print("-", pattern)

     print("\nLow Risk Spoofing Patterns:", len(low_risk_spoofing))
     for pattern in low_risk_spoofing:
          print("-", pattern)

     score, level = calculate_risk_score(
     high_risk_keywords=high_risk_keywords,
     medium_risk_keywords=medium_risk_keywords,
     low_risk_keywords=low_risk_keywords,

     trusted_urls=trusted_urls,
     suspicious_urls=suspicious_urls,

     trusted_domains=trusted_domains,
     unknown_domains=unknown_domains,
     malicious_domains=malicious_domains,

     high_risk_attachments=high_risk_attachments,
     medium_risk_attachments=medium_risk_attachments,
     low_risk_attachments=low_risk_attachments,

     high_risk_grammar=high_risk_grammar,
     medium_risk_grammar=medium_risk_grammar,
     low_risk_grammar=low_risk_grammar,

     high_risk_urgency=high_risk_urgency,
     medium_risk_urgency=medium_risk_urgency,
     low_risk_urgency=low_risk_urgency,

     high_risk_spoofing=high_risk_spoofing,
     medium_risk_spoofing=medium_risk_spoofing,
     low_risk_spoofing=low_risk_spoofing
     )
     
     print("\n" + "=" * 70)
     print(f"{f'Risk Score: {score}/100':^70}")
     print(f"{f'Risk Level : {level}':^70}")
     print("=" * 70)