# .lower()

odpoved = input('Jsi stastna? ')
print(odpoved)
print(odpoved.lower())

# if odpoved == 'ano' or odpoved == 'Ano' or odpoved == 'ANO'
if odpoved.lower() == 'ano':
    ...

# .upper()
def vypis_inicialy(jmeno, prijmeni):
    inicialy = jmeno[0] + prijmeni[0]
    return inicialy.upper()
    
print(vypis_inicialy('Petr', 'michal'))
