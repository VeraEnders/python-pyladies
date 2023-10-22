# Úkol 0
# Na hodině jsme se naučili pracovat s interaktivní Python konzolí. Zkus pomocí Pythonu vypočítat: 3+(4+6)×8÷2−1 =
# (Závorky v Pythonu fungují jako v matematice)

print(3 + (4 + 6) * 8 / 2 - 1) # 42

# Úkol 1
# Jsou i jiné operátory než +, - a ty pro násobení a dělení. Co dělá s čísly operátor % (procento)?
'''
Operátor % se používá k výpočtu zbytku po dělení dvou čísel. 
'''

# Úkol 2
# A co dělá operátor ** (dvě hvězdičky)?
'''
Operátor ** se používá pro umocňování, například
>>> 2 ** 3
8
'''

# Úkol 3
# Jaký je v Pythonu rozdíl mezi dělením pomocí / a //? (Zkus si v Pythonu a odpověz slovně)
'''
Dělení pomocí / je klasické dělení, výsledkem je desetinné číslo:
>>> 7 / 3
2.3333333333333335  

Dělení pomocí // je celočíselné dělení (dělení se zbytkem), výsledkem je celé číslo:
>>> 7 // 3
2
'''

# Úkol 4
# Řetězce jdou spojovat sčítáním. Například: 
# >>> 'A' + "B"
# 'AB'
# Poznáš, co je tady špatně? Jak bys to spravila? 
# >>> 'Ahoj' + 'PyLadies!'
'''
Operátor + spojí řetězce dohromady.
>>> 'Ahoj' + 'PyLadies!'
'AhojPyLadies!'

Příkaz je správný, po spuštění příkazu se žádná chybová hláška neobjevila. 
Přidala bych mezi slovy mezeru
>>> 'Ahoj' + ' ' + 'PyLadies!'
'Ahoj PyLadies!'

nebo čárku
>>> 'Ahoj' + ', ' + 'PyLadies!' 
'Ahoj, PyLadies!
'''

# Úkol 5
# Řetězce se dají sčítat. Dají se i násobit? Dělit? Odečítat? (Odpověz slovně)
'''
V Pythonu nelze násobit, dělit ani odečítat řetězce.
'''

# Úkol 6
# Co se stane, když se pokusím sečíst číslo a řetězec? (Můžeš vložit výsledek z konzole, ale odpověz i slovně)
'''
Pokud se pokusíme sečíst číslo a řetězec, objeví se chybová hláška, 
protože jde o různé typy dat.

>>> "Ahoj" + 42
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
'''

# Úkol 7
# A vynásobit? (Můžeš vložit výsledek z konzole, ale odpověz i slovně)
'''
Pokud se pokusíme vynásobit řetězec číslem, výsledkem bude řetězec, 
který obsahuje opakování původního řetězce.

>>> "Ahoj" * 3
'AhojAhojAhoj'
'''

# Úkol 8
# Poslední úkol se neodevzdává. Je pro tebe, aby sis před další hodinou ověřila, že vše funguje, jak má:
# V adresáři 01 ve složce pro kurz si vytvoř soubor funguju.py . Do souboru ulož:
# print("Hurá, funguju!")
# Pak se v příkazové řádce přepni do adresáře, kde jsi vytvořila soubor, aktivuj virtuální prostředí a do příkazové řádky napiš:
# python funguju.py
# Objevila se oslavná hláška? Gratulujeme, jsi připravena na další hodinu!