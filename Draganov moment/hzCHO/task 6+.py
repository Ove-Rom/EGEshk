from turtle import *
tracer(0)

m = 10
lt(90)


for _ in range(3):
    fd(11*m)
    rt(90)
    fd(24*m)
    rt(90)

up()
fd(m*2)
rt(90)
fd(5*m)
lt(90)
down()

for _ in range(3):
    fd(6*m)
    lt(90)
    fd(9*m)
    lt(90)

for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        teleport(x, y)
        dot(3, "crimson")

done()