user_input = input("Introdueix entre 1 i 3 paraules separades per espais: ")

paraules = user_input.split()

if len(paraules) < 1 or len(paraules) > 3:
    print("Error: Has d'introduir entre 1 i 3 paraules.")
else:
    for paraula in paraules:
        num_caracters = len(paraula)
        primer_caracter = paraula[0]
        ultim_caracter = paraula[-1]

        print(f"\nParaula: {paraula}")
        print(f"Nombre de caràcters: {num_caracters}")
        print(f"Primer caràcter: {primer_caracter}")
        print(f"Últim caràcter: {ultim_caracter}")
