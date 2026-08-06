from Modules.keyword_analyzer import check_keywords
from Modules.url_analyzer import extract_urls, analyze_urls
from Modules.sender_analyzer import check_sender, check_domain
from Modules.attachment_analyzer import analyze_attachment
from Modules.grammar_analyzer import check_grammar
from Modules.urgency_analyzer import check_urgency
from Modules.spoofing_analyzer import check_spoofing
from Modules.calculate_risk_score import calculate_risk_score
from Modules.report_handler import report_menu
from Modules.report_data import report_data

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

     report_menu()

     report_data.clear()  # Clear previous report data

     report_data.update({
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

     print("="*100)
     print(f"{'Risk Score : ' + str(score) + '/100':^100}")
     print(f"{('Risk Level : ' + level):^100}")
     print("="*100)