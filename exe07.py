def isFirst_And_Last_Same(numberList):
    print("Given list is ", numberList)
    firstElement = numberList[0]

## No código normal, tava um -1 no [] do lastElement, isso por que é uma forma de acessar o fim da tabela, como se na coluna zero, se ele andar pra tras, vai ficando -1, -2, etc.


    lastElement = numberList[4]
    if (firstElement == lastElement):
        return True
    else:
        return False

numList = [10, 20, 50, 40, 10]
print("result is", isFirst_And_Last_Same(numList))


