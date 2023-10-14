# Funkce penup a pendown z modulu turtle řeknou želvě, aby přestala, resp. začala kreslit.
# Zkus nakreslit přerušovanou čáru.

from turtle import forward, penup, pendown, exitonclick

for i in range(10):
  forward(10)
  penup()
  forward(5)
  pendown()

# Pak zkus zařídit, aby jednotlivé čárky byly postupně větší a větší.
for i in range(20):
  forward(i)
  penup()
  forward(5)
  pendown()

exitonclick()