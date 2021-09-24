#first, import the package we have installed
import psycopg2
#then, make any variable and use connect function to pass the postgres databse name,user,pass,host,port
connect = psycopg2.connect(dbname="postgres",user="postgres",password="mitadi",host = "localhost",port="5432")
print("Connected")
#next process is in cmd