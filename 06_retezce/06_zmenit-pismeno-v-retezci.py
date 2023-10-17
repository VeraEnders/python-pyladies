# zamen('palec', 0, 'v') == 'valec'
# zamen('valec', 2, 'j') == 'vajec'

# 'palec'[0] = 'v' nelze

def zamen(retezec, pozice, znak):
    """Zamění znak na dané pozici

    Vrátí řetězec, který má na dané pozici daný znak;
    jinak je stejný jako vstupní retezec
    """

    return retezec[:pozice] + znak + retezec[pozice + 1:]

print(zamen('palec', 0, 'v'))