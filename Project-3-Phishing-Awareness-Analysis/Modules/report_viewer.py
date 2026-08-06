import os

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
                view_report()

            elif report_choice == 2:
                delete_report()

            elif report_choice == 0:
                break
            else:
                print("\n[!] Invalid choice. Please select an option from 0-2.")



def list_reports():

    folder = "Reports"

    report_list = []

    reports = os.listdir(folder)
    report_count = 0

    for file in reports:
        if file.endswith(".txt"):
            report_count += 1
            print(f"[{report_count :02}] {file}")
            report_list.append(file)

    report_list.sort(key = lambda file: int(file.split("-")[1]))
    print(f"\n{len(report_list)} report(s) found!\n")

    for file, number in enumerate (report_list, 1):
        print(f"[{number:02}] {file}")





def view_report():
    pass


def delete_report():
    pass