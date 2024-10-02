import random

numero_secret = random.randint(1, 100)

intents = 0

print("Endevina el número que està entre 1 i 100")

while True:
    intent = int(input("Introdueix el número: "))

    intents += 1

    if intent < numero_secret:
        print("El número és més gran")
    elif intent > numero_secret:
        print("El número és més petit")
    else:
        print(f"Has encertat el número {numero_secret}")
        print(f"Intents: {intents}")
        break
