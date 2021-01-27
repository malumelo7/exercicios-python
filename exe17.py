

def exponent(base, exp):
    multil = 1
    for i in range(1, exp+1):
        multil*=base
    return print(base, 'raises to the power of', exp, 'is:',multil)

exponent(5, 3)
