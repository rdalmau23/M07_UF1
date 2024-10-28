assignatures = ["Matemàtiques", "Física", "Història", "Català", "Anglès", "Biologia"]
notes = []

for assignatura in assignatures:
    nota = float(input(f"Indica la nota de {assignatura}: "))
    notes.append(nota)

for i in range(len(assignatures)):
    print(f"A {assignatures[i]} ha tret {notes[i]}")
