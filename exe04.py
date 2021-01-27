numero = int(input('Digite um valor:'))
j=0
print('Current as previous number sum in a range(',numero,')')


for i in range(numero):
    
    print('Current number:',i,'Previous number',j,'Sum:',i+j)
    j=i