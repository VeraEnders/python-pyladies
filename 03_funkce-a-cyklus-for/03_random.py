from random import randrange, uniform

# randrange(a, b)    náhodné celé číslo od a do b-1
# uniform(a, b)      náhodné reálné číslo od a do b

cislo = randrange(0, 3)  # číslo je 0, 1, nebo 2
if cislo == 0:
    print('Kolečko. Vypadla 0.')
elif cislo == 1:
    print('Čtvereček. Vypadla 1.')
else:  # tady musí být číslo 2
    print('Trojúhelníček. Vypadla 2.')