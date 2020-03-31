
import sqlite3
from sqlite3 import Error
from database_connection import create_connection

def f_user_registration(user, password, db_file):
    # Get login details from user
    msg = ''
    
    try:
        # Connect to database
        #db = sqlite3.connect(db_file)
        conn = create_connection(db_file)
        c = conn.cursor()
        # Execute sql statement and grab all records for given user name and password
        sql = ''' INSERT INTO LOGIN_DETAILS(USER_NAME, PASSWORD) VALUES(?,?) '''
        cur = conn.cursor()
        cur.execute(sql, (user,password))
        conn.commit()
        msg = 'Registered'
        conn.close()
    except Error as e:
        msg = e

    return msg

