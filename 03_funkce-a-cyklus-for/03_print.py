# Funkce print zavolaná bez argumentů napíše prázdný řádek.
print()

# Funkce print při výpisu odděluje jednotlivé argumenty mezerou, ale pomocí argumentu sep se dá použít i něco jiného.
print(1, 2, 3, 4, sep=', ') # Místo mezery odděluj čárkou
print(1, 2, 3, 4, sep=': ') # Místo mezery odděluj čárkou

# Dá se změnit i to, co print udělá na konci výpisu. 
# Normálně přejde na nový řádek, ale argumentem end můžeš říct, co se má vypsat místo toho.
print('1 + 2', end=' = ')
print(1 + 2, end='!')
