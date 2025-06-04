from turtle import *

tracer(0)
lt(90)
m = 10

for _ in range(2):
    fd(13*m)
    rt(90)
    fd(20*m)
    rt(90)

pu()
fd(8*m)
rt(90)
bk(3*m)
lt(90)
pd()

for _ in range(2):
    fd(16*m)
    rt(90)
    fd(8*m)
    rt(90)

for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        teleport(x, y)
        dot(3, "crimson")

done()