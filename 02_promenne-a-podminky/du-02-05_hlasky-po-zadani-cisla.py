# Úkol 5
# Zkus napsat program, který píše hlášky podle zadané rychlosti chůze, 
# váhy ulovené ryby, počtu tykadel, teploty vody nebo třeba vzdálenosti od rovníku.

delka_spanku = float(input('Kolik hodin spíš v noci? '))
if delka_spanku >= 10:
  print('Jsi profesionální spáč.')
elif delka_spanku >= 6:
  print('Máš dostatek spánku.')
else:
  print('Máš málo spánku. Doporučuji více spát.')