from turtle import *

tracer(0)
lt(90)
m = 10

for _ in range(2):
    fd(5*m)
    lt(90)
    bk(13*m)
    lt(90)

pu()
bk(10*m)
rt(90)
fd(9*m)
lt(90)
pd()

for _ in range(2):
    fd(11*m)
    rt(90)
    fd(7*m)
    rt(90)

for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        teleport(x, y)
        dot(3, "crimson")

done()