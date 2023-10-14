# Nakresli čtverec.
# Čtverec má čtyři rovné strany a čtyři rohy po 90°.

from turtle import forward, left, exitonclick

# forward(50)
# left(90)
# forward(50)
# left(90)
# forward(50)
# left(90)
# forward(50)
# left(90)

# s použitím cyklů
# V programu použij forward jen dvakrát: jednou v importu, jednou jako volání.
for strana in range(4):
  forward(50)
  left(90)

exitonclick()