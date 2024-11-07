import psycopg2

conn = psycopg2.connect(

        database="postgres",
        user='rdalmau',
        password='rdc123',
        host='db',
        port='5432' 
     ) 


connection = conn.cursor() 
print(connection)