import hashlib
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from getpass import getpass
# import pyperclip  # Import pyperclip for clipboard operations

# my files 
from encryp_decryp import decrypt_message
from dbconfig import dbconfig

def computeMasterkey2(mpp,rkk):
    """
    Compute the master key using PBKDF2 with SHA512.
    """
    mpp = hashlib.sha256(mpp.encode()).hexdigest()
    mpp = mpp.encode()
    rkk = rkk.encode() 
    masterKeyy = PBKDF2(mpp, rkk, 32, count=1000000, hmac_hash_module=SHA512)
    return masterKeyy

def retri(rk ,row_entry):
    mydb = dbconfig()
    cursor =  mydb.cursor()
    
    verifyPass = getpass("Enter Password of PASSWORD MANAGER : ")
    try:
        equalPass = computeMasterkey2(verifyPass,rk)
        
        print(f"           Verified")
        print(f"           Decrypted ")
        decrypted = decrypt_message(equalPass,row_entry)
         # Prompt user for input again when needed
        use_decrypted_data = input("Do you want to use this decrypted data? (y/n): ")
        
        if use_decrypted_data.lower() == 'y':
            # Use decrypted_data in further processing
            print(f"Your password : {decrypted}")
            return True
        else:
            return None
        
        # return True
    except Exception as e:
        print(f"Error: {e}")
        print(f"Password does not match or decryption failed.")
        return False
    