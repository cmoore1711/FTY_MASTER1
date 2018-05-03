import os
import time
import mysql.connector




while(True):

    try:
        cnx = mysql.connector.connect(user='cronos', password='zeusdad',host='10.10.9.107')
        cursor = cnx.cursor()
        time.sleep(60)

        selectTimeString = "SELECT now();"
        
        
        cursor.execute(selectTimeString)
        currTime = str(cursor.fetchone()[0])
     
        changeTimeString = "sudo date -s " + '"' + currTime +'"'
        os.system(changeTimeString)
        cnx.close()
print('All done')    
