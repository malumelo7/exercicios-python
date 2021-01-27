def prefixesDivBy5(A):
    res = []
    current = 0

    for element in A:
        if element:
            current = current*2 + 1
            print('entrou no primeiro if e o valor de current ', current)
        else:
            current = current*2
            print('entrou no primeiro else e o valor de current ', current)
            

        if current%5 == 0:
            res.append(True)
        else:
            res.append(False)
    return res

A = [0,1,1]
print(prefixesDivBy5(A))