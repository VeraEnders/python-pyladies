'''
Ukol 2
Najdi na internetu text své oblíbené písně, zkopíruj si ho do řetězce a zjisti, kolikrát je v něm použito písmeno K (započítej malá i velká písmena).
'''

def spocitej_pismena(text, pismeno):
  return text.lower().count(pismeno)

text_pisne = '''Kde domov můj,
kde domov můj?
Voda hučí po lučinách,
bory šumí po skalinách,
v sadě skví se jara květ,
zemský ráj to na pohled!
A to je ta krásná země,
země česká, domov můj,
země česká, domov můj!
'''

print(spocitej_pismena(text_pisne, 'k'))