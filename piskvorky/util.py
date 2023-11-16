# Pomocný modul - funkce tah()

'''
Napiš funkci tah, která dostane řetězec s herním polem, číslo políčka (0-19), a symbol (x nebo o) a vrátí herní pole (t.j. řetězec) s daným symbolem umístěným na danou pozici.
'''
def tah(pole, cislo_policka, symbol):
  return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]