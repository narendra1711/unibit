
import sqlite3
from sqlite3 import Error
from database_connection import create_connection
import json

def f_data_api(db_file, query):
    # Get login details from user
    msg = ''
    
    try:
        # Connect to database
        #db = sqlite3.connect(db_file)
        conn = create_connection(db_file)
        c = conn.cursor()
        # Execute sql statement and grab all records for given user name and password
        rows = c.execute(query)
        msg = []
        for row in rows:
            msg.append({'JOB_ID':row[0], 'JOB_NAME':row[1], 'STATUS':row[2], 'START_DATETIME':row[3],
                        'END_DATETIME':row[4], 'LAST_UPDATED':row[5], 'ERROR':row[6]})
        
        conn.close()         
    except Error as e:
        msg = e

    return msg

