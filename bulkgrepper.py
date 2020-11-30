#importa
import sys
#prendi argomenti
path = sys.argv[1]

#apri file e prendi contenuto
with open(str(path), 'r') as file:
	dati = file.read()
print(dati)

