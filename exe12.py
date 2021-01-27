lista1 = [1,2,3,4,5,6]
lista2 = [7,8,9,0,11,22]

listafinal = [] 

#teoricamente deveria ser listafinal=[1,3,5,8,0,22]

for i in range(len(lista1)):
    if lista1[i]%2!=0:
        listafinal.append(lista1[i])
    
for i in range(len(lista2)):
    if lista2[i]%2==0:
        listafinal.append(lista2[i])

print(listafinal)