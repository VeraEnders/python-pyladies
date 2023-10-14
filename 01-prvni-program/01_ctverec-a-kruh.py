# Spočítej obvod a obsah čtverce se stranou 356 cm
# Po spuštění by se mělo vypsat: 
# "Obvod čtverce se stranou 356 cm je 1424 cm"
# "Obsah čtverce se stranou 356 cm je 126736 cm2"

# Obvod čtverce se stranou a je O = 4a 
# Obsah je S = a²

strana_ctverce = 123 # v centimetrech
print("Obvod čtverce se stranou", strana_ctverce, "cm je", 4 * strana_ctverce, "cm")
print("Obsah čtverce se stranou", strana_ctverce, "cm je", strana_ctverce ** 2, "cm2")

############################################

# Spočítej obvod a obsah kruhu se stejným poloměrem, jakou má čtverec stranu
# obvod kruhu s poloměrem r je o = 2πr
# obsah S = πr² a π je zhruba 3,1415926

pi = 3.1415926
polomer = strana_ctverce # v centimetrech
print("Obvod kruhu s poloměrem", polomer, "cm je", 2 * pi * polomer, "cm")
print("Obsah kruhu s poloměrem", polomer, "cm je", pi * polomer**2, "cm2")
