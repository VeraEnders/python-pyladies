'''
Ukol 4
Načti od uživatele číslo n a:

Vypočti faktoriál n! (součin všech celých čísel od 1 do n).
Zjisti, jestli je n prvočíslo.
Vypiš prvních n členů Fibonacciho posloupnosti (1, 1, 2, 3, 5, 8, 13, 21, …).
'''

def vypocti_faktorial(n):
  if n == 1:
    return 1
  else:
    return n * vypocti_faktorial(n - 1)
  
def je_prvocislo(n):
  if n <= 1: return False
  
  if n == 2: return True

  for i in range(2, (n // 2) + 2):
    if n % i == 0:
      return False
  
  return True 

def fib(n):
  a = 1
  b = 1
  vysledek = '1, 1'

  for i in range(2, n):
    next_num = a + b
    vysledek += ', ' + str(next_num)
    a = b
    b = next_num
    
  return vysledek

cislo_input = int(input('Zadejte číslo: '))
print(f'Faktoriál čísla {cislo_input} je {vypocti_faktorial(cislo_input)}')
print(f'Je číslo {cislo_input} prvočíslo? {je_prvocislo(cislo_input)}')
print(f'Fibonacciho posloupnost prvních {cislo_input} členů: {fib(cislo_input)}')
