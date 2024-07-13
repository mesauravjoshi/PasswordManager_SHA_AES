# computeMasterKey
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512

from getpass import getpass
# my files 
from encryp_decryp import encrypt_message
# from dbconfig import dbconfig

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
    username = input("Enter username : ")
    site = input("Enter site : ")
    password = getpass("Enter password : ")
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
