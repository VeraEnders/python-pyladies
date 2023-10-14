'''
Ukol 7
Nakresli domeček!
Jak pravil Pythagoras, délka šikmé čáry v domečku je √2-krát délka stěny. O funkci na odmocninu jsme mluvili na srazu.
'''

from turtle import left, forward, exitonclick

stena = 50
sikma_cara = 2**(1/2) * stena
sklon_strechy = sikma_cara / 2

forward(stena)
left(90)
forward(stena)
left(45)
forward(sklon_strechy)
left(90)
forward(sklon_strechy)
left(45)

for i in range(2):
  forward(stena)
  left(135)
  forward(sikma_cara)
  left(135)

exitonclick()
