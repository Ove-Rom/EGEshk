from turtle import *

lt(90)
tracer(0)
m = 100
screensize(2000, 3000)

rt(30)

for i in range(3):
    rt(150)
    fd(6*m)
    rt(30)
    fd(12*m)

for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        teleport(x, y)
        dot(3, "crimson")

done()