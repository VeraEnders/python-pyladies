'''
Ukol 4
Napiš funkci na zpracování rodného čísla. Funkce vezme řetězec s rodným číslem bez lomítka a vrátí zjištěné hodnoty jako n-tici ve formátu (rok, měsíc, den, pohlaví). Například pro RČ 9057121234 vrátí hodnotu: (1990, 7, 12, 'žena').

Rodné číslo není třeba kontrolovat (dělitelnost 11, ...).

Pozn.: Pokud je část rodného čísla, která odpovídá roku, >= 54, jedná se o osoby narozené před rokem 2000. V opačném případě se osoba narodila v roce 2000 nebo později.

Do řešení prosím nedávejte vlastní rodná čísla, ale pouze vymyšlená.

Otestujte (například) pomocí:

print(zpracuj_rodne_cislo('9057121234')) # (1990, 7, 12, 'žena')
print(zpracuj_rodne_cislo('0007021234')) # (2000, 7, 2, 'muž')
'''

def zpracuj_rodne_cislo(rodne_cislo):
  rok = int(rodne_cislo[:2])
  if rok >= 54:
    rok += 1900
  else:
    rok += 2000
    
  mesic = int(rodne_cislo[2:4])

  if mesic > 12:
    pohlavi = 'žena'
    mesic -= 50
  else:
    pohlavi = 'muž'

  den = int(rodne_cislo[4:6])

  return (rok, mesic, den, pohlavi)

print(zpracuj_rodne_cislo('9057121234')) # (1990, 7, 12, 'žena')
print(zpracuj_rodne_cislo('0007021234')) # (2000, 7, 2, 'muž')