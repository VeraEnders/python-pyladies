'''
Ukol 6
Nakresli trojúhelník.
Poznámka: Rovnostranný trojúhelník má vnitřní úhly 60°. Želva se ale otáčí o vedlejší úhel 180 - 60 = 120°.
'''

from turtle import left, forward, exitonclick

for strana in range(3):
  forward(50)
  left(120)

exitonclick()
