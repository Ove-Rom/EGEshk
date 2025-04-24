from turtle import *

m = 10
tracer(0)
screensize(7000, 7000)

rt(45)

for _ in range(10):
    rt(45)
    fd(203*m)
    rt(45)

up()
back(40*m)
rt(45)
down()

for _ in range(5):
    fd(20*m)
    lt(90)

for x in range(-210*m, 10 * m, m):
    for y in range(-250*m, 10 * m, m):
        teleport(x, y)
        dot(3, "crimson")

done()