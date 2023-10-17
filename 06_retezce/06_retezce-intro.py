print("let's go")
print("let's go \"na jedno\"")

print('--\N{LATIN SMALL LETTER L WITH STROKE}--')
print('--\N{SECTION SIGN}--')
print('--\N{PER MILLE SIGN}--')
print('--\N{BLACK STAR}--')
print('--\N{SNOWMAN}--')
print('--\N{KATAKANA LETTER TU}--')

print('C:\\PyLadies\\Nový adresář')

# víceřádkové stringy
basen = '''Haló haló!
Co se stalo?
Prase kozu potrkalo!'''

print(basen)

# dokumentační řetězce u funkcí
def vynasob(a, b):
    """Vynásobí argumenty a vrátí výsledek.

    Oba argumenty by měly být čísla.
    """
    return a * b

print(vynasob(2, 4))

# spojovat dohromady kratší řetězce
spojeny_retezec = 'a' + 'b'
dlouhy_retezec = 'ó' * 100
print(spojeny_retezec, dlouhy_retezec)

pate_pismeno = 'čokoláda'[5]
print(pate_pismeno)