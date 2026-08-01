content = """
Subject: Urgent - Verify Your Bank Account

Dear Customer,

We detected unusual activity on your account.

To protect your account, you must verify your identity immediately.
Failure to verify your account within 24 hours will result in permanent suspension.

Click the secure link below and enter your username and password to continue:

https://secure-bank-login.example.com

If you do not verify your account today, your online banking access will be disabled.

Thank you,
 Team
"""

def check_keywords(content):

    content = content.lower()
    found = False
    keyword_count = 0
    matched_keywords = []

    with open("Database/suspicious_keywords.txt" , "r") as file:
        for line in file:
            keyword = line.strip()
            if keyword in content:
                found = True
                keyword_count += 1
                matched_keywords.append(keyword)

        if found:
            print("Suspicious keywords found:",keyword_count)
            for keyword in matched_keywords:
                print("-",keyword)
                
        else:
            print("No suspicious keywords found.")
check_keywords(content)