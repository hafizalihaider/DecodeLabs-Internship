# Phishing Awareness Analyzer

## Overview

**Phishing Awareness Analyzer** is a Python-based cybersecurity project that analyzes emails and detects common phishing and scam indicators.

The program checks an email for different suspicious patterns, calculates a **risk score from 0–100**, assigns a risk level, and can generate a detailed analysis report.

---

## Features

* Analyze predefined demo emails
* Analyze multiple emails at once
* Analyze all demo emails
* Analyze custom emails
* Detect suspicious keywords
* Analyze URLs and domains
* Detect malicious domains
* Analyze suspicious attachments
* Detect suspicious grammar patterns
* Detect urgency-based language
* Detect spoofing indicators
* Calculate an overall risk score
* Generate separate reports
* Generate combined reports
* View saved reports
* Delete saved reports

---

## How It Works

The analyzer processes an email through several independent modules:

```text
Email
  │
  ├── Keyword Analysis
  ├── URL Analysis
  ├── Domain/Sender Analysis
  ├── Attachment Analysis
  ├── Grammar Analysis
  ├── Urgency Analysis
  └── Spoofing Analysis
          │
          ▼
     Risk Score
          │
          ▼
     Risk Level
          │
          ▼
       Report
```

Each analyzer returns the suspicious indicators it finds. These results are passed to the **risk score calculator**, which produces the final score and classification.

---

## Risk Levels

The analyzer classifies emails according to their calculated score:

|  Score | Risk Level |
| -----: | ---------- |
|   0–10 | Safe       |
|  11–25 | Low Risk   |
|  26–45 | Suspicious |
| 46–100 | High Risk  |

The scoring system gives higher weights to serious indicators such as malicious domains, suspicious URLs, dangerous attachments, and spoofing indicators.

Trusted URLs and trusted domains can reduce the final risk score.

---

## Project Structure

```text
Phishing-Awareness-Analysis/
│
├── Database/
│   ├── suspicious_keywords.txt
│   ├── trusted_domains.txt
│   ├── malicious_domains.txt
│   ├── url_patterns.txt
│   ├── attachment_keywords.txt
│   ├── grammar_patterns.txt
│   ├── urgency_patterns.txt
│   └── spoofing_patterns.txt
│
├── Demo-Emails/
│   └── Email sample files
│
├── Custom-Emails/
│   └── User-entered emails
│
├── Reports/
│   ├── Combined/
│   └── Separate/
│       ├── Safe/
│       ├── Low_Risk/
│       ├── Suspicious/
│       ├── High_Risk/
│       └── Critical_Phishing/
│
├── Modules/
│   ├── menu.py
│   ├── email_loader.py
│   ├── email_analyzer.py
│   ├── multiple_email_analyzer.py
│   ├── all_email_analyzer.py
│   ├── custom_email.py
│   ├── keyword_analyzer.py
│   ├── url_analyzer.py
│   ├── sender_analyzer.py
│   ├── attachment_analyzer.py
│   ├── grammar_analyzer.py
│   ├── urgency_analyzer.py
│   ├── spoofing_analyzer.py
│   ├── calculate_risk_score.py
│   ├── report_generator.py
│   ├── batch_report_generator.py
│   ├── report_viewer.py
│   ├── report_data.py
│   └── config.py
│
└── phishing-awareness-analysis.py
```

---

## Main Menu

When the program starts, the user gets four main options:

```text
1. Analyze Demo Email
2. Analyze Custom Email
3. View Analysis Reports
0. Exit
```

### Demo Email Analyzer

Allows the user to:

* Analyze one email
* Analyze multiple selected emails
* Analyze all available emails

For individual analysis, the user can choose whether to generate a report.

For multiple or all emails, the user can generate either:

* A separate report for each email
* One combined report

### Custom Email Analyzer

The user can paste an email directly into the program.

The program saves the entered email in the `Custom-Emails` folder and analyzes it.

---

## Report System

Reports are stored inside the `Reports` folder.

```text
Reports/
├── Combined/
└── Separate/
    ├── Safe/
    ├── Low_Risk/
    ├── Suspicious/
    ├── High_Risk/
    └── Critical_Phishing/
```

Separate reports are automatically placed into the folder matching their risk level.

The **View Analysis Reports** menu allows the user to:

* View combined reports
* View separate reports by risk level
* Delete reports

---

## Database

The analyzer uses text files instead of hard-coding all detection patterns directly into Python.

For example:

```text
suspicious_keywords.txt
trusted_domains.txt
malicious_domains.txt
grammar_patterns.txt
urgency_patterns.txt
spoofing_patterns.txt
```

This makes the project easier to update because new keywords, domains, or patterns can be added without changing the main Python code.

---

## Technologies Used

* **Python**
* File handling
* String processing
* Lists and dictionaries
* Functions
* Loops and conditional statements
* Modular programming
* Text-based databases
* Automated report generation

---

## How to Run

Make sure Python is installed, then run:

```bash
python phishing-awareness-analysis.py
```

The program will display the main menu and guide the user through the available options.

---

## Limitations

This project is an **awareness and rule-based analysis tool**. It does not use a machine-learning model or a live threat-intelligence service.

Therefore, its results depend on the keywords, domains, patterns, and scoring rules stored in the project's database files.

---

## Future Improvements

Possible future improvements include:

* Machine-learning based phishing detection
* Real-time URL reputation checking
* Email header analysis
* Better attachment detection
* More advanced sender verification
* GUI application
* Web-based interface
* Export reports to PDF

---

## Author

**Hafiz Muhammad Ali Haider**

**Project:** Phishing Awareness Analyzer
**Date:** August 2026
