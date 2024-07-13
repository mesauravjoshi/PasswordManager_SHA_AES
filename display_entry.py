from dbconfig import dbconfig
from prettytable import PrettyTable

def display_entries():
    try:
        mydb = dbconfig()
        with mydb.cursor() as cursor:
            cursor = mydb.cursor()
            cursor.execute("SELECT username, site, password FROM pass_man.entries;")
            rows = cursor.fetchall()

            if not rows:
                print(f"           No entries found.")
                return False
            
            print(f"           Your entries .")

            # Create a PrettyTable instance
            table = PrettyTable(["Username", "Site", "Password"])

            # Add rows to the table
            for row in rows:
                # Add each row with username and site, and "hidden" for password
                table.add_row([row[0], row[1], "hidden"])

            # Set alignment and print the table
            table.align["Username"] = "l"  # Left align username
            table.align["Site"] = "l"      # Left align site
            table.align["Password"] = "l"  # Left align password

            # Print the table
            print(table)

            cursor.close()
            mydb.close()
        return True
    except Exception as e:
            print(f"Error: {e}")
            return False

