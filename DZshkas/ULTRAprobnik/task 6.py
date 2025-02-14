from turtle import *

m = 20
tracer(0)
lt(90)

up()
fd(20*m)

for i in range(10):
    rt(120)
    fd(10*m)

down()
for i in range(7):
    fd(15*m)
    rt(90)

for i in range(5):
    rt(60)
    fd(20*m)
    rt(30)

for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        teleport(x, y)
        dot(3, "crimson")

done()