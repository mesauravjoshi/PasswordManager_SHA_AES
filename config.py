import hashlib
import random
import string
from getpass import getpass
import mysql.connector
from first_display_message import first_display_message
from dbconfig import dbconfig  # Assuming this imports your database connection function
from valid.validation import validate_input
def generateDeviceSecret(length=12):
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

def checkConfig():
    mydb = dbconfig()  # Assuming dbconfig() returns a MySQL connection object
    cursor = mydb.cursor()
    
    cursor.execute("SHOW TABLES LIKE 'secrets'")
    result = cursor.fetchone()
    if result:
         # print("Table 'secrets' already exists.")
         pass
    else:
        first_display_message()
        # Password Validation 
        attempts = 0  # Counter for attempts
        while attempts < 3:
            valid = getpass("Enter initial password for PASSWORD MANAGER: ")
            managerPassword = validate_input(valid)  # Validation File
            if managerPassword:
                break
            else:
                print(f"\nError: The password must be 6+ characters with at least one uppercase letter, one lowercase letter, one digit, and one special symbol\n")
                attempts += 1
        
        if attempts == 3:
            print("Maximum attempts reached. Exiting.")
            exit()

        Confirm_managerPassword = getpass("Confirm password for PASSWORD MANAGER: ")
        if Confirm_managerPassword == managerPassword:
            try:
                # Check if 'secrets' table already exists
                cursor.execute("SHOW TABLES LIKE 'secrets'")
                result = cursor.fetchone()
                if result:
                    pass
                else:
                    # Create 'secrets' table if it does not exist
                    query_secrets = """
                        CREATE TABLE secrets (
                            masterkey_hashed VARCHAR(255) NOT NULL,
                            random_key VARCHAR(255) NOT NULL
                        )
                    """
                    cursor.execute(query_secrets)
                    # print("Table 'secrets' created.")
                    
                    # Create 'secrets' table if it does not exist
                    query_entries  = """
                    CREATE TABLE entries (
                        username VARCHAR(255) NOT NULL,
                    site VARCHAR(255) NOT NULL,
                        password VARCHAR(255) NOT NULL
                        )
                    """
                    cursor.execute(query_entries)
                    # print("Entries tables created .")
                    
                    # Hash the password using SHA-256
                    hashed_password  = hashlib.sha256(managerPassword.encode()).hexdigest()

                    # Generate random password (device secret)
                    device_secret  = generateDeviceSecret(12)

                    # Insert hashed password and random key into 'secrets' table
                    insert_query = """
                        INSERT INTO secrets (masterkey_hashed, random_key)
                        VALUES (%s, %s)
                    """
                    insert_values = (hashed_password, device_secret)

                    try:
                        cursor.execute(insert_query, insert_values)
                        mydb.commit()
                        # print("Inserted manager password and random key .")
                    except mysql.connector.Error as err:
                        print(f"Error inserting data: {err}")

            except mysql.connector.Error as err:
                print(f"Database Error: {err}")

            finally:
                cursor.close()
                mydb.close()
            return  # No need for True return value if not used elsewhere
                
        else :
            print(f"Passwords do not match.")
            exit()

    # return  # No need for True return value if not used elsewhere
