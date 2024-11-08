from create import create_user
from read import read_users
from update import update_user
from delete import delete_user

def main():
    while True:
        print("\nMenú:")
        print("1. Crear usuari")
        print("2. Llegir usuaris")
        print("3. Actualitzar usuari")
        print("4. Eliminar usuari")
        print("5. Sortir")
        choice = input("Escull una opció: ")

        if choice == '1':
            nom = input("Nom: ")
            cognom = input("Cognom: ")
            email = input("Correu electrònic: ")
            posicio = input("Posició: ")
            salari = float(input("Salari: "))
            create_user(nom, cognom, email, posicio, salari)
        elif choice == '2':
            read_users()
        elif choice == '3':
            user_id = int(input("ID de l'usuari a actualitzar: "))
            nova_posicio = input("Nova posició (opcional): ")
            nou_salari = input("Nou salari (opcional): ")
            nou_salari = float(nou_salari) if nou_salari else None
            update_user(user_id, nova_posicio, nou_salari)
        elif choice == '4':
            user_id = int(input("ID de l'usuari a eliminar: "))
            delete_user(user_id)
        elif choice == '5':
            break
        else:
            print("Opció no vàlida, intenta-ho de nou.")

if __name__ == "__main__":
    main()
