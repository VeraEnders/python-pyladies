zlate_stranky = {
    'Alice': '654321978',
    'Borivoj': '1475239980',
    'Cyril': '654213978'
}

zlate_stranky['Pepa'] = '1591236753'

print(zlate_stranky.values())
print(zlate_stranky.keys())
print(zlate_stranky.items())

for jmeno, cislo in zlate_stranky.items():
    print(jmeno)
    print(cislo)
    
for jmeno in list(zlate_stranky):
    if jmeno == 'Borivoj':
        del zlate_stranky['Borivoj']
    
print(zlate_stranky)