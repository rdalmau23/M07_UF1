assignatures_notes = {}

for assignatura in ["Matemàtiques", "Física", "M7", "Català", "Anglès", "M3"]:
    nota = float(input(f"Indica la nota de {assignatura}: "))
    assignatures_notes[assignatura] = nota

for assignatura, nota in assignatures_notes.items():
    print(f"A {assignatura} ha tret {nota}")
