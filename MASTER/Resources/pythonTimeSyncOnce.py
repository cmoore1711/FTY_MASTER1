import os
import time
import mysql.connector


try:
    cnx = mysql.connector.connect(user='cronos', password='zeusdad',host='10.10.9.107')
    cursor = cnx.cursor()
        

    selectTimeString = "SELECT now();"
        
        
    cursor.execute(selectTimeString)
    currTime = str(cursor.fetchone()[0])
     
    changeTimeString = "sudo date -s " + '"' + currTime +'"'
    os.system(changeTimeString)
    cnx.close()
except:
    print('Error')
