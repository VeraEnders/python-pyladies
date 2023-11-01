import random

balicek = []
for barva in '♠', '♥', '♦', '♣':
  for hodnota in list(range(2, 11)) + ['J', 'Q', 'K', 'A']:
    balicek.append(str(hodnota) + barva)
print(balicek)

# Funkce shuffle 
# všechny prvky náhodně popřehází
random.shuffle(balicek)
print(balicek)

# Funkce choice 
# vybere ze seznamu jeden náhodný prvek 
mozne_tahy = ['kámen', 'nůžky', 'papír']
tah_pocitace = random.choice(mozne_tahy)
print(tah_pocitace)