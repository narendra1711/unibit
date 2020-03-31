
import sqlite3
from sqlite3 import Error
from database_connection import create_connection

def f_user_validation(user, password, db_file):
    # Get login details from user
    msg = ''
    login_flag = False
    try:
        # Connect to database
        #db = sqlite3.connect(db_file)
        conn = create_connection(db_file)
        c = conn.cursor()
        # Execute sql statement and grab all records for given user name and password
        c.execute('SELECT * FROM LOGIN_DETAILS WHERE USER_NAME = ? AND PASSWORD = ?', (user, password))

        # If nothing was found then c.fetchone() would be an empty list, which
        # evaluates to False 
        if c.fetchone():
            msg = 'Welcome'
            login_flag = True
        else:
            msg = 'Login Failed'
            
        conn.close()
    except Error as e:
        msg = e

    return msg, login_flag

