from connection import get_cursor

def read_usuaris():
    cursor = get_cursor()
    cursor.execute('SELECT * FROM usuaris')
    usuaris = cursor.fetchall()
    for usuari in usuaris:
        print(usuari)
    cursor.close()
