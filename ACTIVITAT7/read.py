from connection import get_cursor

def read_employees():
    cursor = get_cursor()
    cursor.execute('SELECT * FROM usuaris')
    employees = cursor.fetchall()
    for employee in employees:
        print(employee)
    cursor.close()
