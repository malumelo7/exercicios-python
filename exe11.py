num = str(1256)

lista = []
for i in range(len(num)):
    lista.insert(i, num[i])

reversedstring = str(''.join(reversed(lista)))

if reversedstring==num:
    print("É igual!")

else:
    print("Diferente!")