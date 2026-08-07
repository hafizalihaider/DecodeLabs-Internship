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


def get_report_list():

    if not os.path.exists(FOLDER):
        print("[!] No reports found.")
        return []
    
    reports = os.listdir(FOLDER)

    report_list = []

    for file in reports:
        if file.endswith(".txt"):
            report_list.append(file)

    if not report_list:
        print("[!] No reports found.")
        return []

    report_list.sort(key = lambda file: int(file.split("_")[-1].replace(".txt", "")))

    print()
    print("=" * 100)
    print(f"{'AVAILABLE REPORTS':^100}")
    print("=" * 100)
    print(f"\nTotal Reports : {len(report_list)}\n")

    for number, file in enumerate (report_list, 1):
        print(f"[{number:02}] {file}")

    print("\n[00] Back")
    print("-"*100)

    return report_list

    

def list_reports():

    while True:

        report_list = get_report_list()

        if len(report_list) == 0:
            break

        list_choice = input("\nEnter your choice: ")

        if list_choice == "00":
            break

        if list_choice.isdigit():

            list_choice = int(list_choice)

            if list_choice >= 1 and list_choice <= len(report_list):
                view_report(report_list[list_choice - 1])

            else:
                print(f"[!] Report {list_choice} does not exist.")

        else:
            print(f"[!] '{list_choice}' is not a valid number.")



def view_report(report_file):

    path = os.path.join(FOLDER, report_file)

    try:

        with open(path, "r") as file:
            content = file.read()

        print("="*100)
        print(f"{report_file:^100}")
        print("="*100)

        print(content)

        print("-"*100)

        input("\nPress Enter to return to return...")

    except FileNotFoundError:
        print(f"[!] Report '{report_file}' not found.")

    except Exception as e:
        print(f"[!] Error: {e}")



def delete_report():

    while True:

        report_list = get_report_list()

        if len(report_list) == 0:
            break

        delete_choice = input("\nEnter your choice: ")

        if delete_choice == "00":
            break

        if delete_choice.isdigit():

            delete_choice = int(delete_choice)

            if 1 <= delete_choice <= len(report_list):
                selected_report = report_list[delete_choice - 1]
                path = os.path.join(FOLDER, selected_report)

                while True:

                    confirmation = input(f"\nDelete '{selected_report}'? (Y/N): ").strip().upper()

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

            else:
                print(f"[!] Report {delete_choice} does not exist.")

        else:
            print(f"[!] '{delete_choice}' is not a valid number.")