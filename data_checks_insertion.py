
import sqlite3
from sqlite3 import Error
from database_connection import create_connection

def f_data_checks(module_name,process_name,query,notify_email,db_file):
    # Get login details from user
    msg = ''
    
    try:
        # Connect to database
        #db = sqlite3.connect(db_file)
        conn = create_connection(db_file)
        c = conn.cursor()
        # Execute sql statement and grab all records for given user name and password
        sql = ''' INSERT INTO D_CHECKS(MODULE_NAME,PROCESS_NAME,QUERY,EMAIL) VALUES(?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, (module_name,process_name,query,notify_email))
        conn.commit()
        msg = 'Submitted'
        conn.close()
    except Error as e:
        msg = e

    return msg

