import psycopg2

conn = psycopg2.connect(
        database="postgres",
        user='rdalmau',
        password='daw',
        host='localhost',
        port='5432' 
) 


def get_cursor():
    return conn.cursor()
