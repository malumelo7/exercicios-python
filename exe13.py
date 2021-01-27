num = str(7536)

lista = []
for i in range(len(num)):
    lista.insert(i,num[i])

print(' '.join(reversed(lista)))