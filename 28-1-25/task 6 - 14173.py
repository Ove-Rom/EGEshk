from turtle import *

m = 10
lt(90)
tracer(0)

for i in range(2):
    down()
    for j in range(2):
        fd(8*m)
        rt(90)
        fd(8*m)
        rt(90)
    up()
    fd(6*m)
    rt(90)
    fd(6*m)
    lt(90)
rt(180)
fd(4*m)
down()
for i in range(4):
    fd(8*m)
    rt(270)

for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        teleport(x, y)
        dot(3, "crimson")

done()