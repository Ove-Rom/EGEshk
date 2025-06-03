from turtle import *

tracer(0)
lt(90)
m = 10

for i in range(9):
    fd(27*m)
    rt(90)
    fd(30*m)
    rt(90)

pu()
fd(3*m)
rt(90)
fd(6*m)
lt(90)
pd()

for i in range(9):
    fd(77*m)
    rt(90)
    fd(66*m)
    rt(90)

for x in range(-100*m, 100*m, m):
    for y in range(-100 * m, 100 * m, m):
        teleport(x, y)
        dot(3, "crimson")

done()
