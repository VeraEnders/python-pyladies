def obvod_ctvrce(strana):
    vysledek = 4 * strana
    if strana <= 0:
        raise ValueError(f'Strana musi byt kladna, {strana} neni kladne cislo.')
    return vysledek

print(obvod_ctvrce(-2))

