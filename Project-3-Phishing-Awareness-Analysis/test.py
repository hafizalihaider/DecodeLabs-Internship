import os

folder = "Reports"

reports = os.listdir(folder)
report_count = 0

for file in reports:
    if file.endswith(".txt"):
        report_count += 1
        print(f"[{report_count :02}] {file}")