import psycopg2

def create_db():
    connect = psycopg2.connect(dbname="postgres",user="postgres",password="mitadi",host = "localhost",port="5432")
    cur = connect.cursor() #calling method
    cur.execute('''CREATE TABLE aditya(ID SERIAL,NAME TEXT,AGE TEXT, ADDRESS TEXT);''')
    print("Table created")
    connect.commit() #commit means save or finalise the changes
    connect.close()

def insert_data_in_Db():
    connect = psycopg2.connect(dbname="postgres",user="postgres",password="mitadi",host = "localhost",port="5432")
    cur = connect.cursor() #calling method
    cur.execute('''INSERT INTO aditya(NAME,AGE,ADDRESS) VALUES ('John','18','Mumbai');''')
    connect.commit() #commit means save or finalise the changes
    connect.close()

insert_data_in_Db()