# Ukol 1
# nahodné číslo 1-10
# Program nechá uživatele hádat číslo
# Pokud se uživatel trefí program pogratuluje
# Pokud ne uživatel hádá znovu

import random

nahodne_cislo = random.randrange(10)
tip = int(input('Hádej číslo 0-9: '))

while tip != nahodne_cislo:
  tip = int(input('Hádej číslo 0-9: '))

print("Hurá uhodla jsi!")