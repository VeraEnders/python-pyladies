#  n-tice (angl. tuple)

# N-tice se tvoří jako seznamy, jen kolem sebe nemají hranaté závorky
# Chovají se skoro stejně jako seznamy, jen nejdou měnit

prazdna_ntice = () # n-tice s žádným prvkem
jednoprvkova_ntice = ('a', ) # n-tice s jedním prvkem
print(prazdna_ntice, jednoprvkova_ntice) # () ('a',)

osoby = 'máma', 'teta', 'babička'
for osoba in osoby:
  print(osoba)
print('První je {}'.format(osoby[0]))


seznam_dvojic = []
for i in range(10):
  # `append` bere jen jeden argument; dáme mu jednu dvojici
  seznam_dvojic.append((i, i**2))
print(seznam_dvojic)

# N-tice se hodí, pokud chceme z funkce vrátit víc než jednu hodnotu
def podil_a_zbytek(a, b):
  return a // b, a % b

# pokud chceš přiřadit do několika proměnných najednou, 
# stačí je na levé straně rovnítka oddělit čárkou 
# a na pravou stranu dát nějakou „složenou” hodnotu – třeba právě n-tici
podil, zbytek = podil_a_zbytek(13, 5)
print(podil)  # 2
print(zbytek) # 3

x, o = 'xo'
print(x) # x
print(o) # o

jedna, dva, tri = [1, 2, 3]
print(jedna) # 1
print(dva)   # 2
print(tri)   # 3