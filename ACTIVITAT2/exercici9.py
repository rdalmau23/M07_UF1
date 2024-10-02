user_input = input("Introdueix 2 paraules: ")

paraules = user_input.split()

if len(paraules) != 2:
    print("Error: Has d'introduir 2 paraules.")
else:
    for paraula in paraules:
        paraula1 = paraules[0]
        paraula2 = paraules[1]

        nova_paraula1 = paraula2[:2] + paraula1[2:]
        nova_paraula2 = paraula1[:2] + paraula2[2:]

        print(f"Resultat: {nova_paraula1} {nova_paraula2}")
