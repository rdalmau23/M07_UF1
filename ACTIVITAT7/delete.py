from connection import get_cursor, conn

def delete_usuari(usuari_id):
    cursor = get_cursor()
    cursor.execute('DELETE FROM usuaris WHERE id = %s', (usuari_id,))
    conn.commit()
    cursor.close()
    print("Eliminat correctrament")
