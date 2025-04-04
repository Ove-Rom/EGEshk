from turtle import *
tracer(0)
lt(90)
m = 10

for i in range(9):
    fd(9*m)
    rt(90)
    fd(25*m)
    rt(90)

up()
back(10*m)
rt(90)
down()

for i in range(8):
    fd(15*m)
    lt(90)
    fd(25*m)
    lt(90)

up()
fd(6*m)
lt(90)
down()

for i in range(7):
    fd(15*m)
    rt(90)
    fd(25*m)
    rt(90)

for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        teleport(x, y)
        dot(3, "crimson")

done()