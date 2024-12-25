from turtle import *

tracer(0)
m = 10
lt(90)

for i in range(8):
    fd(16*m)
    rt(90)
    fd(22*m)
    rt(90)

up()
fd(5*m)
rt(90)
fd(5*m)
lt(90)
down()

for i in range(8):
    fd(52*m)
    rt(90)
    fd(77*m)
    rt(90)

for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        teleport(x, y)
        dot(3, "crimson")

done()