from Modules import report_data
from Modules.report_generator import generate_report


def report_menu():
         
        while True:

            user_input = input("Do you want to generate a detailed report? (Y/N): ").strip().upper()

            if user_input == 'Y':
                generate_report(**report_data)
                print(f"\n✓ Report saved successfully.")
                break

            elif user_input == 'N':
                print("Report generation skipped.")
                break

            else:
                print("Invalid input. Please enter 'Y' or 'N'.")