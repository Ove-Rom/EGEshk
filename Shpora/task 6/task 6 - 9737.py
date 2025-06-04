from turtle import *

tracer(0)
lt(90)
m = 10

for i in range(2):
    fd(10*m)
    rt(90)
    fd(18*m)
    rt(90)

pu()
fd(5*m)
rt(90)
fd(7*m)
lt(90)
pd()

for i in range(2):
    fd(10*m)
    rt(90)
    fd(7*m)
    rt(90)

for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        teleport(x, y)
        dot(3, "crimson")

done()