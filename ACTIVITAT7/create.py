from connection import get_cursor, conn

def create_usuari(first_name, last_name, email, position, salary):
    cursor = get_cursor()
    cursor.execute('''
        INSERT INTO usuaris (nom, cognom, email, posicio, salari)
        VALUES (%s, %s, %s, %s, %s)
    ''', (first_name, last_name, email, position, salary))
    conn.commit()
    cursor.close()
    print("Registro creado exitosamente.")
