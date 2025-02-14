from turtle import *

m = 10
tracer(0)
lt(90)

for i in range(9):
    fd(22*m)
    rt(90)
    fd(6*m)
    rt(90)

up()
fd(m)
rt(90)
fd(5*m)
lt(90)
down()

for i in range(9):
    fd(53*m)
    rt(90)
    fd(75*m)
    rt(90)

for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        teleport(x, y)
        dot(3, "crimson")

done()