from turtle import *

screensize(5000, 5000)

tracer(0)

lt(90)

m = 100

for _ in range(15):
    fd(4*m)
    rt(60)

for x in range(m, 10*m, m):
    for y in range(m, 10*m, m):
        teleport(x, y)
        dot(3, "crimson")

done()
