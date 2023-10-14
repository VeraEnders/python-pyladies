'''
Ukol 1
Napiš funkci, která vrátí maximální hodnotu ze tří zadaných čísel. 
Zjištění maxima naprogramuj sama, pomocí příkazů if.
'''

def max_hodnota(a, b, c):
  if a >= b and a >= c:
    return a
  elif b >= c:
    return b
  else:
    return c
  
print(max_hodnota(14, 15, 1))