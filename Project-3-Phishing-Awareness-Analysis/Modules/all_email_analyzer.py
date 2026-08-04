

    email_list.sort(key = lambda file: int(file.split("-")[1]))
    print(f"{len(email_list)} email(s) found!\n")

    for email in email_list:

        path = os.path.join("Demo-Emails", email)

        with open(path , "r") as file:
            contents = file.read()

        print("-"*70)
        print(f"{email:^70}")
        print("-"*70)

        print(contents)

        analyze_email(contents)