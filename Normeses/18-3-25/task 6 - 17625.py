from turtle import *

tracer(0)
m = 10
lt(90)

for i in range(10):
    fd(22*m)
    rt(90)
    fd(16*m)
    rt(90)

up()
fd(m)
rt(90)
fd(m)
lt(90)
down()

for i in range(10):
    fd(72*m)
    rt(90)
    fd(79*m)
    rt(90)

for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        teleport(x, y)
        dot(3, "crimson")

done()