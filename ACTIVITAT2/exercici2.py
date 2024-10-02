def calcular_iva():

    valor = float(input("Introdueix un valor en €: "))


    while True:
        iva = float(input("Introdueix l'IVA a aplicar (4%, 10% o 21%): "))
        if iva in [4, 10, 21]:
            break
        else:
            print("IVA incorrecte. Si us plau, introdueix un IVA vàlid (4%, 10% o 21%).")

    valor_final = valor + (valor * (iva / 100))

    print(f"Valor introduït: {valor} €")
    print(f"IVA aplicat: {iva} %")
    print(f"Valor final amb IVA: {valor_final} €")

calcular_iva()
