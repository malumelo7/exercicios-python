listinha = [1,2,3,4,5]

proc = 3

found = False

for i in range(len(listinha)):
    if listinha[i] == proc:
        print('O indice e:',i)
        found = True

if  not found:
    print(-1)


