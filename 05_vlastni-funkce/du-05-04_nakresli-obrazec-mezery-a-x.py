'''
Ukol 4

Napiš funkci, která s pomocí cyklu for a příkazu if vypíše z jednotlivých 'X' a mezer následující obrazec:

X X X X X X
X         X
X         X
X         X
X         X
X X X X X X
'''

def nakresli_obrazec():
  pocet_radku = 6
  pocet_pozic = 6

  for radek in range(pocet_radku):
    for pozice in range(pocet_pozic):
      if radek == 0 or radek == pocet_radku-1 or pozice == 0 or pozice == pocet_pozic-1:
        print('X', end=' ')
      else:
        print(' ', end=' ')
    print()

nakresli_obrazec()