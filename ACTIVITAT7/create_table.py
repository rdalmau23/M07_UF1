from connection import get_cursor, conn

def create_table():
    cursor = get_cursor()

    
    cursor.execute('''DROP TABLE IF EXISTS usuaris''')

   
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuaris (
            id SERIAL PRIMARY KEY,
            nom VARCHAR(50),
            cognom VARCHAR(50),
            email VARCHAR(100),
            posicio VARCHAR(50),
            salari NUMERIC
        )
    ''')

    conn.commit()
    cursor.close()
    print("Taula usuaris creada")

if __name__ == "__main__":
    create_table()