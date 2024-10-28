divises = {
    "Euro": "€",
    "Dòlar": "$",
    "Lliura": "£",
    "Ien": "¥",
    "Dòlar Australià": "A$"
}

divisa = input("Escriu el nom d'una divisa: ")
simbol = divises.get(divisa)

if simbol:
    print(f"El símbol de {divisa} és {simbol}")
else:
    print("La divisa no està al diccionari.")
