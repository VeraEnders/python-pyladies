'''
Ukol 8
Nakresli n-úhelník (např. čtyřúhelník, pětiúhelník), kde n zadá uživatel.
Vnitřní úhel pravidelného n-úhelníka má 180 × (1-2/n) stupňů.
Aby byly tvary zhruba stejně veliké, použij pro n-úhelník délku strany např. 200/n
'''
pocet_stran = int(input('Zadejte počet stran n-úhelníka: '))
delka_strany = 200 / pocet_stran

uhel = 180 - (180 * (1 - 2/pocet_stran))

from turtle import left, forward, exitonclick

for strana in range(pocet_stran):
  forward(delka_strany)
  left(uhel)

exitonclick()
