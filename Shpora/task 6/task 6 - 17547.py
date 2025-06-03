from turtle import *

lt(90)
tracer(0)
m = 10

for i in range(3):
    fd(7*m)
    rt(90)
    fd(12*m)
    rt(90)

pu()
fd(4*m)
rt(90)
fd(6*m)
lt(90)
pd()

for i in range(4):
    fd(83*m)
    rt(90)
    fd(77*m)
    rt(90)

for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        teleport(x, y)
        dot(3, "crimson")

done()