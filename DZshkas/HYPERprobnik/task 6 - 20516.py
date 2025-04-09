from turtle import *

m = 10
tracer(0)
lt(90)

for i in range(3):
    fd(m * 2)
    rt(90)
    fd(m * 3)
    lt(90)

rt(180)
fd(m * 6)
rt(90)
fd(m * 9)
up()
back(m * 3)
rt(90)
down()

for i in range(2):
    fd(m)
    rt(90)
    fd(m * 2)
    lt(90)

rt(180)
fd(m * 3)
rt(90)
fd(m * 4)
rt(90)
fd(m)

for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        teleport(x, y)
        dot(3, "crimson")

done()