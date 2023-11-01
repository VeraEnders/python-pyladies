# Funkce list
# vytvoří seznam znaků -- pro seznam slov použijeme na řetězci metodu split
abeceda = list('abcde') 
cisla = list(range(10)) 
print(abeceda) # ['a', 'b', 'c', 'd', 'e']
print(cisla)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# funkce list ze seznamu udělá nový seznam
a = [1, 2, 3]
b = list(a)

print(b) # [1, 2, 3]
a.append(4)
print(b) # [1, 2, 3]

# Další způsob: udělat prázdný seznam, pak ho postupně naplnit pomocí funkce append
mocniny_dvou = []
for cislo in range(10):
  mocniny_dvou.append(2 ** cislo)
print(mocniny_dvou) # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

# seznam, který reprezentuje balíček karet
balicek_karet = []
for barva in '♠', '♥', '♦', '♣':
  for hodnota in list(range(2, 11)) + ['J', 'Q', 'K', 'A']:
    balicek_karet.append(str(hodnota) + barva)
print(balicek_karet)