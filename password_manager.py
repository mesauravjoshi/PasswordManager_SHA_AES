from dbconfig import dbconfig
from add import addentry
from retri import retri
from display_entry import display_entries
from delete_entries import delete_entries 
from config import checkConfig 
    

def main_box():
    print(''' 
          You are in Password Manager
            ================================================
            |       1. Create New Entry                     |
            |       2. Retrieve Password                    |
            |       3. Display Entries                      |
            |       4. Delete Password                      |
            |       5. Exit                                 |
            ================================================
    ''')

    enter_num = int(input("Enter your choice: "))
    return enter_num

if __name__ == "__main__":
    checkConfig()
    mydb = dbconfig()
    cursor = mydb.cursor()
    # print(f"\n")
    while True:
        enter_num = main_box()

        if enter_num == 1:

            cursor.execute("SELECT masterkey_hashed, random_key FROM secrets;")
            row = cursor.fetchone()

                # If row is not None, fetch the values into variables
            if row:
                mp = row[0]  # masterkey_hashed
                rk = row[1]  # random_key
                
            addentry(mydb,cursor,mp,rk)
        elif enter_num ==2:
            
            cursor.execute("SELECT masterkey_hashed, random_key FROM secrets;")
            row = cursor.fetchone()

            if row:
                mp = row[0]  # masterkey_hashed
                rk = row[1]  # random_key
            
            print(f"           Want to get password .?")
            uName = input("Enter username : ")
            retri_query = "SELECT password FROM entries WHERE username = %s"
            cursor.execute(retri_query, (uName,))
            row_entry = cursor.fetchone()
            if row_entry:
                print(f"           Username {uName} found .")
                retri(rk,row_entry[0])
            else:
                print(f"           User '{uName}' not found.")            

        elif enter_num == 3:
            display_entries()
        elif enter_num == 4:
            delete_entries()
        elif enter_num == 5:
            print(f"            Bye")
            exit()
        else:
            print("         Invalid Input.")
