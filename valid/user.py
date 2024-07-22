def validate_username():
    attempts = 0
    while attempts < 3:
        username = input("Enter a username: ")
        if username.isdigit():
            print("Username should not be only numeric. Please enter a valid username.")
            attempts += 1
        else:
            return username
    if attempts == 3:
        print("Maximum attempts reached. Exiting.")
        exit()
