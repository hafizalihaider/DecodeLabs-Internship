from Modules.report_generator import generate_report, write_report_content
from datetime import datetime
import os

def batch_report_menu(all_report_data):

    while True:

        print()
        print("=" * 100)
        print(f"{'BATCH REPORT MENU':^100}")
        print("=" * 100)
        print()

        print("1. Generate Separate Report for Each Email")
        print("2. Generate One Combined Report")
        print("0. Back")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            for report in all_report_data:
                report_copy = report.copy()
                report_copy.pop("file_name", None)
                generate_report(**report_copy)

            print("\n✓ Separate reports generated successfully.")
            break

        elif choice == "2":
            generate_combined_report(all_report_data)
            break

        elif choice == "0":
            break

        else:
            print("\n[!] Invalid choice.")



def generate_combined_report(all_report_data):

    report_folder = "Reports/Combined"
    os.makedirs(report_folder, exist_ok=True)

    current_time = datetime.now()

    file_name = f"Combined_Phishing_Analysis_Report_{current_time.strftime('%y_%m_%d_%H%M%S')}.txt"
    file_path = os.path.join(report_folder, file_name)

    with open(file_path, "w") as file:

        file.write("=" * 100 + "\n")
        file.write(f"{'COMBINED PHISHING ANALYSIS REPORT':^100}\n")
        file.write("=" * 100 + "\n\n")

        file.write(f"Date : {current_time.strftime('%d %B, %Y')}\n")
        file.write(f"Time : {current_time.strftime('%I:%M %p')}\n")
        file.write(f"Total Emails : {len(all_report_data)}\n")

        file.write("\n")
        file.write("=" * 100 + "\n\n")

        for number, report in enumerate(all_report_data, 1):

            file.write("=" * 100 + "\n")
            file.write(f"{'EMAIL ' + str(number):^100}\n")
            file.write("=" * 100 + "\n\n")

            file.write(f"Email Name : {report['file_name']}\n\n")

            write_report_content(file, report)

            file.write("\n\n")

    print(f"\n✓ Combined report generated successfully.")
    print(f"✓ Location: {file_path}")