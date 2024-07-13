import hashlib
from getpass import getpass
from dbconfig import dbconfig



def delete_entries():
    try:
        mydb = dbconfig()
        cursor =  mydb.cursor()
        del_Name = input("Enter username to delete: ")
        
        # SQL query to delete entry based on username
        del_query = "DELETE FROM entries WHERE username = %s"
        cursor.execute(del_query, (del_Name,))
        
        if cursor.rowcount == 0:
            print(f"User '{del_Name}' not found.")
        else:
            # Fetch hashed master key for confirmation
            cursor.execute("SELECT masterkey_hashed FROM pass_man.secrets;")
            rows = cursor.fetchall()
            for row in rows:
                masterkey_hashed = row[0]
            
            confirm_delete = getpass("Please confirm your password for PASSWORD MANAGER: ")
            # Hash user input for comparison
            confirm_hash = hashlib.sha256(confirm_delete.encode()).hexdigest()

            if confirm_hash == masterkey_hashed:
                mydb.commit()
                print(f"           {cursor.rowcount} record(s) deleted successfully.")
            else:
                print(f"           Incorrect password. Deletion canceled.")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False