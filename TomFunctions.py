import turtle as tom
import random

tom.speed("fastest")#make tom a fast turtle 
tom.clearscreen() #clear the screen
tom.colormode(225)

tom.shape("turtle")#make tom a turtle and not an arrow
tom.shapesize(2, 2, 4) # Make tom bigger
col = ['red', 'purple', 'yellow', 'orange', 'green', 'blue', 'pink'] 
def speed():
    tom.speed("fastest")
def color():
    tom.fillcolor(col[random.randint(0, 6)])
    tom.width(5)
def circlespiral(cize):
    tom.penup()
    tom.pendown()
    tom.begin_fill()
    for i in range (18):
        tom.right(20)
        tom.circle(i*cize)
    tom.end_fill()
    tom.penup()
def randompos():
    tom.penup()
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    tom.goto(x, y)
    tom.pendown()
def drawhearts(cize):
    tom.pendown()
    tom.setheading(0)#point east
    tom.penup()
    tom.fillcolor(col[random.randint(0, 6)])#set Tom's color
    tom.begin_fill()#start filling
    tom.pendown()
    tom.left(125)
    tom.forward(205 * cize/5)
    tom.right(35)
    curve(cize/5)
    tom.left(180)
    curve(cize/5)
    tom.right(35)
    tom.forward(195 * cize/5)
    tom.end_fill()#end filling
    tom.penup()
    
def curve(curvesize):
    for i in range(45):
        tom.right(4)
        tom.forward(4 * curvesize)
def thick(no):
    tom.width(no)
def drawstars(cize):
    tom.pendown()
    points = (random.randint(2, 3) * 2) + 1
    tom.setheading(0)#point east
    tom.penup()
    tom.begin_fill()#start filling
    tom.pendown()
    tom.begin_fill()
    for i in range (5):
        tom.right(144)
        tom.forward(100 * cize/5)
    tom.end_fill()
    tom.penup()
tomtext = "qwerg"
def rewrite(col, text):
    tom.pencolor(f'{col}')
    tom.penup()
    tom.goto(0, 0)
    tom.pendown()
    tom.write(text, align="Center", font=("Arial", 40, "normal"))
    tom.pencolor('black')
def square(cize):
    tom.pendown()
    tom.begin_fill()
    for i in range(4):
        tom.right(90)
        tom.forward(cize*50)
    tom.end_fill()
    tom.penup()

def drawcubey():
    tom.penup()
    x = tom.xcor()
    y = tom.ycor()
    tom.penup()
    tom.goto(x+50,y+50)
    tom.setheading(0)
    tom.pendown()
    tom.fillcolor("blue")
    square(2)
    tom.fillcolor("white")
    tom.penup()
    tom.goto(x+25,y+25)
    tom.pendown()
    square(1)
    tom.penup()
    tom.goto(x,y)
    tom.color("black")
    tom.stamp()
    tom.pendown
    tom.penup()

def circle(cize):
    tom.pendown()
    tom.begin_fill()
    tom.circle(cize*25)
    tom.end_fill()

def triangle(cize):
    tom.pendown()
    tom.begin_fill()
    for i in range(3):
        tom.right(60)
        tom.forward(cize*25)
    tom.end_fill()
    tom.penup()

def bumpy(cize):
    tom.pendown()
    tom.begin_fill()
    for i in range(4):
        curve(cize/3)
        tom.left(90)
    tom.end_fill()
    tom.penup()

'''while True:
    rewrite()
    size = random.randint(5, 10)/20
    tom.width(5)
    drawhearts()
    size = random.randint(5, 10)/10
    tom.width(10 * size)
    drawstars()
    size = random.randint(2, 8)
    circlespiral()
'''

