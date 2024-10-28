assignatures = ["Matemàtiques", "Física", "M7", "Català", "Anglès", "M3"]
notes = []

for assignatura in assignatures:
    nota = float(input(f"Indica la nota de {assignatura}: "))
    notes.append(nota)

for i in range(len(assignatures)):
    print(f"A {assignatures[i]} ha tret {notes[i]}")
