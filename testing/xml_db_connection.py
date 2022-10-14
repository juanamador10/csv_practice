#Juan Fernando Amador Miranda - 9° A BIS - ISW

# import mysql connector
import mysql.connector
  
# give the connection parameters
# user name is root
# password is empty
# server is localhost
# database name is xmldatabase
conn = mysql.connector.connect(user='root', 
                               password='', 
                               host='localhost', 
                               database='xmldatabase')
  

      
# sql query to insert data into database
data = """INSERT INTO xmltable(model,memory,ram,battery,cost) VALUES(%s,%s,%s,%s,%s)"""
# creating the cursor object
c = conn.cursor()
    
# executing cursor object
c.execute(data, ("Samsung Galaxy S22","128 GB","8 GB","3,700 mAh","USD 799.99"))
c.execute(data, ("iPhone 13","128 GB","4 GB","3,227 mAh","USD 599.00"))

conn.commit()

exec(open("xml_update.py").read())



