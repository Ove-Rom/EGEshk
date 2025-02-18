from turtle import *

m = 20

tracer(0)
lt(90)

for i in "10":
    rt(120)
    fd(7*m)

rt(300)

for i in "10":
    rt(120)
    fd(7*m)

for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        teleport(x, y)
        dot(3, "crimson")

done()