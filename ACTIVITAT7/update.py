from connection import get_cursor, conn

def update_employee(usuari_id, nova_posicio=None, nou_salari=None):
    cursor = get_cursor()
    if nova_posicio:
        cursor.execute('UPDATE usuaris SET posicio = %s WHERE id = %s', (nova_posicio, usuari_id))
    if nou_salari:
        cursor.execute('UPDATE usuaris SET salari = %s WHERE id = %s', (nou_salari, usuari_id))
    conn.commit()
    cursor.close()
    print("Registro actualizado exitosamente.")
