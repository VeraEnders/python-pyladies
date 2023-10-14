'''
Ukol 3
Vytvoř funkci nakresli_n_uhelnik, která vykreslí pro zadaný počet stran n-úhelník. Pomocí této funkce vykresli následující obrázek:
Vnitřní úhel pravidelného n-úhelníka má 180 × (1-2/n) stupňů.
Aby byly tvary zhruba stejně veliké, použij pro n-úhelník délku strany např. 200/n
'''

from turtle import left, forward, penup, pendown, exitonclick

def nakresli_n_uhelnik(pocet_stran):
  delka_strany = 200 / pocet_stran
  uhel = 180 - (180 * (1 - 2/pocet_stran))

  for strana in range(pocet_stran):
    forward(delka_strany)
    left(uhel)

for n_uhelnik in range(5, 9):
  nakresli_n_uhelnik(n_uhelnik)
  penup()
  forward(70)
  pendown()

exitonclick()