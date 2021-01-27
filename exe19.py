arr = [64, 34, 25, 12, 22, 11, 90]
##arr = [34, 25, 12, 22, 11, 64, 90]
##arr = [6, 5, 4, 3, 2, 1]

for j in range(len(arr)-1): 
    for i in range(len(arr)-1):  
        if arr[i] > arr[i+1]:
            
            tmp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = tmp
    print(arr)



