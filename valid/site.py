def validate_site():
    attempts = 0
    while attempts < 3:
        username = input("Enter a site : ")
        if username.isdigit():
            print("Website name should not be only numeric. Please enter a valid username.")
            attempts += 1
        else:
            print("Username is valid.")
            return username
    if attempts == 3:
        print("Maximum attempts reached. Exiting.")
        exit()
