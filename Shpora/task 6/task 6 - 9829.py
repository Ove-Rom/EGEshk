from turtle import *

tracer(0)
m = 100
screensize(10000, 10000)

for i in range(3):
    rt(45)
    fd(10*m)
    rt(45)

rt(315)
fd(10*m)

for i in range(2):
    rt(90)
    fd(10*m)

for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        teleport(x, y)
        dot(3, "crimson")

done()