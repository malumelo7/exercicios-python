
lista = ['Banana', 'maçã', 'Banana', 'laranja']
dicionario = {}

for i in lista:
    if not i in dicionario.keys():
        dicionario[i] = 1
    else:
        dicionario[i]+=1
print(dicionario)

    