# Nakresli tři čtverce, každý otočený třeba o 20°

from turtle import forward, left, exitonclick
# # první čtverec
# forward(50)
# left(90)
# forward(50)
# left(90)
# forward(50)
# left(90)
# forward(50)
# left(90)

# # druhý čtverec
# left(20)
# forward(50)
# left(90)
# forward(50)
# left(90)
# forward(50)
# left(90)
# forward(50)
# left(90)

# # třetí čtverec
# left(20)
# forward(50)
# left(90)
# forward(50)
# left(90)
# forward(50)
# left(90)
# forward(50)
# left(90)

# nakresli 3 čtverce, každý otočený o 20°. Tentokrát už víš, jak to dělat chytře: opakuj pomocí příkazu for, ne kopírováním kódu.
for ctverec in range(3):
  for strana in range(4):
    forward(50)
    left(90)
  left(20)

exitonclick()