from turtle import *

screensize(3000,3000)

lt(90)
m = 100
tracer(0)

rt(30)

for i in range(3):
    rt(150)
    fd(6*m)
    rt(30)
    fd(12*m)

for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        teleport(x, y)
        dot(2, "crimson")

done()