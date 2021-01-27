def Encontra(lista, proc,min, max):

    mid = (min + max)//2

    if proc == lista[mid]:
        print(f"Proc={proc}, lista[mid]= {lista[mid]} ")
        return mid

    elif proc < lista[mid]:
        print(f"Proc={proc}, lista[mid]= {lista[mid]} ")
        return Encontra(lista, proc, min, mid-1)

    elif proc > lista[mid]:
        print(f"Proc={proc}, lista[mid]= {lista[mid]} ")
        return Encontra(lista, proc, mid+1, max)


if __name__ == "__main__":
    lista = [1,2,3,4,5,6,7,8] 
    proc = 3
    min = 0
    max = len(lista) - 1

    result = Encontra(lista,proc, min, max)

    print('Element is present at index',result)
    











