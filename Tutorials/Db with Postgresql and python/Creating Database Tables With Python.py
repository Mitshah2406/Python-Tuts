import psycopg2

connect = psycopg2.connect(dbname="postgres",user="postgres",password="mitadi",host = "localhost",port="5432")
cur = connect.cursor() #calling method
cur.execute('''CREATE TABLE student(ID SERIAL,NAME TEXT,AGE TEXT, ADDRESS TEXT);''')
print("Table created")
connect.commit() #commit means save or finalise the changes
connect.close()