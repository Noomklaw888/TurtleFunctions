import random
import TomFunctions as t
t.thick(10)
t.speed()

for i in range (5):
    t.randompos()#go to random position
    t.color()#chhose a random color from
    t.square(random.randint(1,5))#square fuction makes a square
    t.randompos()
    t.color()
    t.drawhearts(random.randint(1,5))#drawhearts makes a heart
    t.randompos()
    t.color()
    t.drawstars(random.randint(1,5))#drawstars makes a star
    t.randompos()
    t.color()
    t.circlespiral(random.randint(1,5))#circlespiral makes a cool spiral
    t.randompos()
    t.color()
    t.bumpy(random.randint(1,5))#bumpy makes a bumpy shape
t.tom.goto(0,0)
t.drawcubey()#cubey is cool!
tomtext='Hello World!'
t.rewrite("white", tomtext)#rewrite writes on the screen
t.tom.right(90)
t.thick(10)#line width

#t.curve(40)makes the arc of a half circle

t.tom.hideturtle()
