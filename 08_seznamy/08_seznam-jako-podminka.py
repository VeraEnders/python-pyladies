# Seznam se dá použít v příkazu if (nebo while) jako podmínka, která platí, když v tom seznamu něco je. 
# Jinými slovy, seznam je tu „zkratka“ pro len(seznam) > 0.

seznam = ['E', 'E', 'D', 'E', 'F', 'D']

if seznam:
  print('V seznamu něco je!')
else:
  print('Seznam je prázdný!')