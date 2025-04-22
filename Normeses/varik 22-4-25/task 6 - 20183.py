from turtle import *

tracer(0)
lt(90)
m = 10

for _ in range(7):
    fd(9 * m)
    rt(90)
    fd(16*m)
    rt(90)

up()
fd(3*m)
rt(90)
fd(4*m)
lt(90)
down()

for _ in range(4):
    fd(7*m)
    rt(90)
    fd(13*m)
    rt(90)

for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        teleport(x, y)
        dot(3, "white")

done()