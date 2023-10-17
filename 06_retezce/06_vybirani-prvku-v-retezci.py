slovo = 'čokoláda'
pate_pismeno = slovo[5]
print(pate_pismeno)

print(len(slovo))

# vypise vsechna pismena v retezci
for pismeno in slovo:
    print(pismeno)

# Sekání řetězců
print(slovo[:4])
print(slovo[2:5])
print(slovo[-4:])

username = 'Jimmy1994'

print(username[-4:]) # 1994
print(username[:5]) # Jimmy
print(username[:-4]) # Jimmy

print(username[:username.index('1')]) # Jimmy

