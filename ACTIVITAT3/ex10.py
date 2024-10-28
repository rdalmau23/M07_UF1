import string

abecedari = list(string.ascii_uppercase)
llista_filtrada = [lletra for i, lletra in enumerate(abecedari, start=1) if i % 3 != 0]
tupla_resultant = tuple(llista_filtrada)

print("Llista:", llista_filtrada)
print("Tupla:", tupla_resultant)
