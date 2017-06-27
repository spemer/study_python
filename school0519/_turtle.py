import turtle, random

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

t3.pensize(10)
t3.penup()
t3.setposition(400,200)
t3.pendown()
t3.setposition(400,-200)
t3.penup()
t3.hideturtle()

screen = turtle.Screen()
image1 = "rabbit.gif"
image2 = "turtle.gif"
screen.addshape(image1)
screen.addshape(image2)

t1.shape(image1)
t2.shape(image2)
t1.pencolor("red")
t2.pencolor("blue")
t1.pensize(3)
t2.pensize(3)
t1.penup()
t2.penup()
t1.goto(-400,100)
t2.goto(-400,-100)

t1.pendown()
t2.pendown()

for i in range(150):
    d1 = random.randint(1,10)
    t1.forward(d1)
    d2 = random.randint(1,10)
    t2.forward(d2)

if (t1.goto(200,100) == True):
    t1.shape("turtle")
elif (t2.goto(200,-100) == True):
    t2.shape("turtle")