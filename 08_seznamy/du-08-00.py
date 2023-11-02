'''
Ukol 0
Udělej si seznam domácích zvířat. Budeš ho potřebovat v dalších úlohách. 
Domácí zvířata známe tato: "pes", "kočka", "králík", "had".

Napiš funkci, která dostane jako argumenty seznam zvířat a slovo a zjistí, jestli je toto slovo v seznamu. 
„Zjistí“ znamená, že funkce vrátí True nebo False.
'''

def je_slovo_v_seznamu(seznam, slovo):
  return slovo in seznam

zvirata = ["pes", "kočka", "králík", "had"]
print(je_slovo_v_seznamu(zvirata, "had"))
print(je_slovo_v_seznamu(zvirata, "krtek"))