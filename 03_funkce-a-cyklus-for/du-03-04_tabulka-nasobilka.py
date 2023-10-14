'''
Ukol 4
Napiš program, který vypíše „tabulku“ s násobilkou.
1 2 3 4
2 4 6 8
3 6 9 12
4 8 12 16
'''

for i in range(1, 5):
  for j in range(1, 5):
    print(i * j, end=' ')
  print()