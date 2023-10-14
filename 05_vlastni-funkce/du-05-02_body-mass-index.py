'''
Ukol 2

Vytvoř funkci, která spočítá Body Mass Index pro kočky. Vstupem (parametry) funkce bude obvod hrudníku (cm) a délka zadní nohy od kolena ke kotníku (cm). Funkce vrátí číslo feline body mass index (fBMI).

Postup výpočtu fBMI: 1. Vydělit obvod hrudníku 0.7062 a odečíst délku nohy. 2. Vydělit výsledek 0.9156. 3. Od výsledku bodu 2 odečíst délku nohy.
'''

def feline_bmi(obvod_hrudniku, delka_nohy):
  vysledek = ((obvod_hrudniku / 0.7062 - delka_nohy) / 0.9156) - delka_nohy
  return vysledek

print(feline_bmi(31, 14))