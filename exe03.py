primeiro = int(input('Digite o primeiro número:'))
segundo = int(input('Digite o segundo número:'))
soma = primeiro+segundo
multiplicar = primeiro*segundo

if multiplicar>1000:
    print('Deu maior que 1000, sua soma é:',soma)
else:
    print('Deu menor.')