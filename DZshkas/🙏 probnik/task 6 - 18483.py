from turtle import *

m = 10
tracer(0)
lt(90)

for i in range(4):
    fd(16*m)
    lt(90)
    fd(20*m)
    lt(90)

pu()
fd(4*m)
lt(90)
fd(8*m)
rt(180)
pd()

for i in range(3):
    fd(35*m)
    lt(90)
    fd(6*m)
    lt(90)

for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        teleport(x, y)
        dot(3, "white")

done()
