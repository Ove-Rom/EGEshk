from turtle import *
screensize(4000, 4000)
tracer(0)

m = 100
lt(90)

rt(30)

for _ in range(3):
    rt(150)
    fd(6*m)
    rt(30)
    fd(12*m)

for x in range(-20*m, 20*m, m):
    for y in range(-20*m, 20*m, m):
        teleport(x, y)
        dot(3, "crimson")

done()