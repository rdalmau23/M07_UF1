import psycopg2

conn = psycopg2.connect(
    database="",
    user="",
    password="",
    host="localhost",
    port="5432"
    
)

connection = conn.cursor()

print(connection)