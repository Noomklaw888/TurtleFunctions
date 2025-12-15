import TomFunctions as t
t.move(0, 100)
t.rewrite("black", "Loading...")
t.thick(width=None)
t.speed()
t.move(0,0)
x=1
t.invis(1)
while True:
    t.tom.fillcolor(col[(x-1)%7])
    t.circle(1)
    t.tom.left(50)
    x += 1
