num = 25

list = []
while num > 0:
    list.append(int(num%2))
    num = int(num/2)
list.reverse()
list = [str(x) for x in list]
print(''.join(list))


num2 = str(11001)
result = sum([int(x) * (2**ind) for ind, x in enumerate(reversed(num2))])
print(result)



    

