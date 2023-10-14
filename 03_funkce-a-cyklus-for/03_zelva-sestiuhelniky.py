# zkus nakreslit těchto šest (nebo sedm?) šestiúhelníků

from turtle import forward, left, right, exitonclick 

left(60)

for i in range(6):
  left(60)
  forward(50)
  for j in range(2):
    right(60)
    forward(50)

right(60)

for i in range(6):
  for j in range(2):
    forward(50)
    left(60)
  forward(50)
  left(180)

exitonclick()