import os

FOLDER = "Reports"

def report_menu():

    while True:

        print("=" * 100)
        print(f"{'Report Analysis Menu':^100}")
        print("=" * 100)

        print("1. View Reports")
        print("2. Delete Report")
        print("0. Back")

        report_choice = input("\nEnter your choice: ")

        if report_choice.isdigit():

            report_choice = int(report_choice)

            if report_choice == 1:
                list_reports()

            elif report_choice == 2:
                delete_report()

            elif report_choice == 0:
                break

            else:
                print("\n[!] Invalid choice. Please select an option from 0-2.")

        else:
            print("\n[!] Invalid choice. Please select an option from 0-2.")


def get_report_list(folder):

    if not os.path.exists(folder):
        print("[!] No reports found.")
        return []

    reports = os.listdir(folder)

    report_list = []

    for file in reports:

        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path) and file.endswith(".txt"):
            report_list.append(file)

    if not report_list:
        print("[!] No reports found.")
        return []

    report_list.sort()

    print()
    print("=" * 100)
    print(f"{'AVAILABLE REPORTS':^100}")
    print("=" * 100)
    print(f"\nTotal Reports : {len(report_list)}\n")

    for number, file in enumerate(report_list, 1):
        print(f"[{number:02}] {file}")

    print("\n[00] Back")
    print("-" * 100)

    return report_list

    

def list_reports():

    while True:

        print()
        print("=" * 100)
        print(f"{'VIEW REPORTS':^100}")
        print("=" * 100)

        print("\n1. Combined Reports")
        print("2. Separate Reports")
        print("0. Back")
        print("-" * 100)

        choice = input("\nEnter your choice: ").strip()

        # Combined
        if choice == "1":

            folder = os.path.join(FOLDER, "Combined")

            report_list = get_report_list(folder)

            if not report_list:
                continue

            report_choice = input("\nEnter your choice: ").strip()

            if report_choice == "00":
                continue

            if report_choice.isdigit():

                report_choice = int(report_choice)

                if 1 <= report_choice <= len(report_list):

                    report_path = os.path.join(
                        folder,
                        report_list[report_choice - 1]
                    )

                    view_report(report_path)

                else:
                    print("[!] Report does not exist.")

            else:
                print("[!] Invalid input.")

        # Separate
        elif choice == "2":

            separate_reports_menu()

        # Back
        elif choice == "0":

            break

        else:

            print("\n[!] Invalid choice. Please select 0-2.")

def separate_reports_menu():

    while True:

        print()
        print("=" * 100)
        print(f"{'SEPARATE REPORTS':^100}")
        print("=" * 100)

        print("\n1. Safe")
        print("2. Low Risk")
        print("3. Suspicious")
        print("4. High Risk")
        print("5. Critical Phishing")
        print("0. Back")
        print("-" * 100)

        choice = input("\nEnter your choice: ").strip()

        folders = {
            "1": "Safe",
            "2": "Low_Risk",
            "3": "Suspicious",
            "4": "High_Risk",
            "5": "Critical_Phishing"
        }

        if choice == "0":
            break

        if choice not in folders:
            print("\n[!] Invalid choice.")
            continue

        folder = os.path.join(
            FOLDER,
            "Separate",
            folders[choice]
        )

        report_list = get_report_list(folder)

        if not report_list:
            continue

        report_choice = input("\nEnter your choice: ").strip()

        if report_choice == "00":
            continue

        if report_choice.isdigit():

            report_choice = int(report_choice)

            if 1 <= report_choice <= len(report_list):

                report_path = os.path.join(
                    folder,
                    report_list[report_choice - 1]
                )

                view_report(report_path)

            else:
                print("[!] Report does not exist.")

        else:
            print("[!] Invalid input.")


def view_report(report_path):

    try:

        with open(report_path, "r") as file:
            content = file.read()

        report_file = os.path.basename(report_path)

        print()
        print("=" * 100)
        print(f"{report_file:^100}")
        print("=" * 100)
        print()

        print(content)

        print("-" * 100)

        input("\nPress Enter to return...")

    except FileNotFoundError:

        print("[!] Report not found.")

    except Exception as e:

        print(f"[!] Error: {e}")



def delete_report():

    while True:

        print()
        print("=" * 100)
        print(f"{'DELETE REPORT':^100}")
        print("=" * 100)

        print("\n1. Combined Reports")
        print("2. Separate Reports")
        print("0. Back")
        print("-" * 100)

        choice = input("\nEnter your choice: ").strip()

        # ---------------- COMBINED REPORTS ----------------

        if choice == "1":

            folder = os.path.join(FOLDER, "Combined")

            report_list = get_report_list(folder)

            if not report_list:
                continue

            delete_choice = input("\nEnter your choice: ").strip()

            if delete_choice == "00":
                continue

            if delete_choice.isdigit():

                delete_choice = int(delete_choice)

                if 1 <= delete_choice <= len(report_list):

                    selected_report = report_list[delete_choice - 1]
                    path = os.path.join(folder, selected_report)

                    delete_confirmation(path, selected_report)

                else:
                    print(f"[!] Report {delete_choice} does not exist.")

            else:
                print(f"[!] '{delete_choice}' is not a valid number.")

        # ---------------- SEPARATE REPORTS ----------------

        elif choice == "2":

            print()
            print("=" * 100)
            print(f"{'SEPARATE REPORTS':^100}")
            print("=" * 100)

            print("\n1. Safe")
            print("2. Low Risk")
            print("3. Suspicious")
            print("4. High Risk")
            print("5. Critical Phishing")
            print("0. Back")
            print("-" * 100)

            risk_choice = input("\nEnter your choice: ").strip()

            risk_folders = {
                "1": "Safe",
                "2": "Low_Risk",
                "3": "Suspicious",
                "4": "High_Risk",
                "5": "Critical_Phishing"
            }

            if risk_choice == "0":
                continue

            if risk_choice not in risk_folders:
                print("\n[!] Invalid choice.")
                continue

            folder = os.path.join(
                FOLDER,
                "Separate",
                risk_folders[risk_choice]
            )

            report_list = get_report_list(folder)

            if not report_list:
                continue

            delete_choice = input("\nEnter your choice: ").strip()

            if delete_choice == "00":
                continue

            if delete_choice.isdigit():

                delete_choice = int(delete_choice)

                if 1 <= delete_choice <= len(report_list):

                    selected_report = report_list[delete_choice - 1]
                    path = os.path.join(folder, selected_report)

                    delete_confirmation(path, selected_report)

                else:
                    print(f"[!] Report {delete_choice} does not exist.")

            else:
                print(f"[!] '{delete_choice}' is not a valid number.")

        # ---------------- BACK ----------------

        elif choice == "0":
            break

        else:
            print("\n[!] Invalid choice. Please select 0-2.")


def delete_confirmation(path, selected_report):

    while True:

        confirmation = input(
            f"\nDelete '{selected_report}'? (Y/N): "
        ).strip().upper()

        if confirmation == "Y":

            try:

                os.remove(path)

                print("\n✓ Report deleted successfully.")
                break

            except Exception as e:

                print(f"\n[!] Error deleting report: {e}")
                break

        elif confirmation == "N":

            print("\nDeletion cancelled.")
            break

        else:

            print("\n[!] Invalid input. Please enter Y or N.")