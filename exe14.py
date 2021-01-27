income = int(45000)
cont = 0

if income <= int(10000):
    print('R$ =',income)

elif int(10000) < income < int(20000):
    cont = income - 10000
    pagar = 0*10000 + cont*0.2
    print ('R$ =', pagar)

elif income >= int(20000):
    cont = income - 20000
    pagar = 0*10000 + 0.1*10000 + cont*0.2
    print ('R$ =', pagar)

else:
    print('Erro!')