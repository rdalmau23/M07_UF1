#Demanar a l’usuari un número. Indicar si el número inserit per l’usuari és parell o senar.

num = int(input("Introdueix un número:"))

if num % 2:
    print(num, "és imparell")
else:
    print(num, "és parell")