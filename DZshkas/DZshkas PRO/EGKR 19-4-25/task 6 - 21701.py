from turtle import *

lt(90)
m = 10
tracer(0)
teleport(-10*m, -20*m)

for _ in range(2):
    fd(28 * m)
    rt(90)
    fd(18 * m)
    rt(90)

pu()
fd(14*m)
rt(90)
fd(10*m)
lt(90)
pd()

for _ in range(2):
    fd(30*m)
    rt(90)
    fd(7*m)
    rt(90)

for x in range(-50*m, 50*m, m):
    for y in range(-50*m, 50*m, m):
        teleport(x, y)
        dot(3, "crimson")

done()