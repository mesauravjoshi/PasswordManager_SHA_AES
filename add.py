# computeMasterKey
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512

from getpass import getpass
# my files 
from encryp_decryp import encrypt_message
from valid.validation import validate_input
from valid.user import validate_username
from valid.site import validate_site

def computeMasterkey(mp,rk):
    """
    Compute the master key using PBKDF2 key derivation function.
    """
    mp = mp.encode()
    rk = rk.encode() 
    masterKey = PBKDF2(mp, rk, 32, count=1000000, hmac_hash_module=SHA512)
    return masterKey

def addentry(mydb,cursor,mp,rk):
    """
    Add a new entry to the password manager database.
    """
    print(f"            Creating new entry...")
    username = validate_username()   #  user.py
    
    site = validate_site()   #  site.py
    
    # Password Validation 
    attempts = 0  # Counter for attempts
    while attempts < 3:
        valid = getpass("Enter password: ")
        password = validate_input(valid)  # Validation File
        if password:
            break
        else:
            print(f"Error: The password must be 6+ characters with at least one uppercase letter, one lowercase letter, one digit, and one special symbol")
            attempts += 1
    
    if attempts == 3:
        print("Maximum attempts reached. Exiting.")
        exit()
    confirm_passsword = getpass("Confirm password : ")
    if confirm_passsword == password:
        symKey = computeMasterkey(mp,rk)
        
        encrypted = encrypt_message(symKey,password)
        
        # Add to mydb
        insert_query_entry = """
            INSERT INTO pass_man.entries (username, site , password)
            VALUES (%s, %s, %s)
        """
        insert_value_entry = (username,site,encrypted)
        cursor.execute(insert_query_entry,insert_value_entry)
        mydb.commit()
        print(f"            Entry added succesfully .........")
    else :
        print(f"            Retry.. Passwords do not match.")
    
    return True
