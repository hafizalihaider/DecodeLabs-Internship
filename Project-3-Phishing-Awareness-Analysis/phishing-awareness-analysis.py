print("="*70)
print(f"{'Phishing Awareness Analysis':^70}")
print("="*70)

while True:

    print("\nStart Menu")
    print("-"*12)
    print("\n1. Analyze Email")
    print("2. Exit")

    try:
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
                pass

        elif choice == 2:
                print("\nThank you for using Phishing Awareness Analyzer.")
                break
        else:
            print("\nPlease choose 1 or 2.")

    except ValueError:
            print("\nPlease enter a numeric choice.")
