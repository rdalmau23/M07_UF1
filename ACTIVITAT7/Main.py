from create import create_usuari
from read import read_usuaris
from update import update_usuari
from delete import delete_usuari

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
            create_usuari(nom, cognom, email, posicio, salari)
        elif choice == '2':
            read_usuaris()
        elif choice == '3':
            user_id = int(input("ID de l'usuari a actualitzar: "))
            nova_posicio = input("Nova posició (opcional): ")
            nou_salari = input("Nou salari (opcional): ")
            nou_salari = float(nou_salari) if nou_salari else None
            update_usuari(user_id, nova_posicio, nou_salari)
        elif choice == '4':
            user_id = int(input("ID de l'usuari a eliminar: "))
            delete_usuari(user_id)
        elif choice == '5':
            break
        else:
            print("Opció no vàlida, intenta de nou.")

if __name__ == "__main__":
    main()
