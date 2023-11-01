# Metoda split
# dostane seznam slov z řetězce

slova = 'Tato věta je složitá, rozdělme ji na slova!'.split()
print(slova) # ['Tato', 'věta', 'je', 'složitá,', 'rozdělme', 'ji', 'na', 'slova!']

zaznamy = '3A,8B,2E,9D'.split(',')
print(zaznamy) # ['3A', '8B', '2E', '9D']

# Metoda join
# spojit seznam řetězců zase dohromady do jediného řetězce
veta = ' '.join(slova)
print(veta) # Tato věta je složitá, rozdělme ji na slova!