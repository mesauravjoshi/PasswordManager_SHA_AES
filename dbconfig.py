import mysql.connector

def dbconfig():
    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",  # by default root
        password="yourpassword"  # which you set during MySQL installation
    )

    cursor = mydb.cursor()

    # Create database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS pass_man")
    mydb.commit()  # Commit the creation of the database

    # Close cursor, do not close mydb yet
    cursor.close()

    # Return a connection to the database pass_man
    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",    # by default root
        password="yourpassword",   # which you set during MySQL installation
        database="pass_man"
    )
    # print("connection made ...............:) ")

    return mydb
