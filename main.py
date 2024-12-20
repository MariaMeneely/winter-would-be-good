import turtle

screen = turtle.Screen()
screen.screensize(800,800)
screen.bgcolor('light steel blue')

#background
t_ground = turtle.Turtle()
t_ground.penup()
t_ground.pencolor('snow1')
t_ground.fillcolor('snow1')
t_ground.speed(0)
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.begin_fill()
t_ground.goto(1000,-100)
t_ground.goto(100,-1000)
t_ground.goto(-1000,-1000)
t_ground.goto(-1000,-100)
t_ground.end_fill()
t_ground.hideturtle()

#tree
t_tree = turtle.Turtle()
t_tree.penup()
t_tree.pencolor('dark green')
t_tree.fillcolor('dark green')

t_tree.goto(220,220)
t_tree.pendown()
t_tree.begin_fill()
t_tree.goto(280, -100)
t_tree.goto(160,-100)
t_tree.goto(220,220)
t_tree.end_fill()

#stump
t_tree.penup()
t_tree.pencolor('saddle brown')

t_tree.goto(220,-100)
t_tree.pendown()
t_tree.pensize(15)
t_tree.goto(220,-128)
t_tree.hideturtle()
#endoftree

#gift
t_gift = turtle.Turtle()
t_gift.penup()
t_gift.pencolor('green')
t_gift.goto(180,-129)
t_gift.pendown()
t_gift.pensize(15)
t_gift.fillcolor('green')
t_gift.begin_fill()
t_gift.goto(145,-129)
t_gift.goto(145,-180)
t_gift.goto(180,-180)
t_gift.goto(180,-129)
t_gift.end_fill()

t_gift.penup()
t_gift.pencolor('red')
t_gift.goto(165,-129)
t_gift.pendown()
t_gift.goto(165,-180)
t_gift.penup()
t_gift.goto(145,-139)
t_gift.pendown()
t_gift.goto(180, -139)
t_gift.hideturtle()

#snow flake
t = turtle.Turtle()
t.pencolor('light blue')
t.pensize(6)
t.penup()
t.goto(-200, 200)
t.pendown()
for _ in range(6):
    t.forward(100)
    t.backward(100)
    t.right(60)


#snow man
man = turtle.Turtle()
man.penup()
man.pencolor('white')
man.fillcolor('white')
man.speed(0)
man.goto(-100,-100)
man.pendown()
man.begin_fill()
man.circle(50)
man.end_fill()

man.penup()
man.pencolor('white')
man.fillcolor('white')
man.speed(0)
man.goto(-100,-25)
man.pendown()
man.begin_fill()
man.circle(40)
man.end_fill()

man.penup()
man.pencolor('white')
man.fillcolor('white')
man.speed(0)
man.goto(-100,50)
man.pendown()
man.begin_fill()
man.circle(30)
man.end_fill()

#candycane

candy = turtle.Turtle()
candy.pensize(5)
candy.color("red")

candy.penup()
candy.goto(0, -100)
candy.pendown()
candy.setheading(90)
candy.forward(50)
candy.right(90)
candy.forward(10)
candy.right(90)
candy.forward(10)
candy.penup()
candy.goto(0, -100)
candy.pendown()

candy.hideturtle()


#ordements
t2 = turtle.Turtle()

t2.color("red")
t2.penup()
t2.goto(220,10)
t2.pendown()
t2.fillcolor('red')
t2.begin_fill()
t2.circle(10)
t2.end_fill()

t2.color("yellow")
t2.penup()
t2.goto(239,29)
t2.pendown()
t2.fillcolor('yellow')
t2.begin_fill()
t2.circle(10)
t2.end_fill()

t2.color("purple")
t2.penup()
t2.goto(200,-37)
t2.pendown()
t2.fillcolor('purple')
t2.begin_fill()
t2.circle(10)
t2.end_fill()

t2.color("blue")
t2.penup()
t2.goto(225,79)
t2.pendown()
t2.fillcolor('blue')
t2.begin_fill()
t2.circle(10)
t2.end_fill()

t2.color("light green")
t2.penup()
t2.goto(225,-35)
t2.pendown()
t2.fillcolor('light green')
t2.begin_fill()
t2.circle(10)
t2.end_fill()

#text
t3 = turtle.Turtle()
t3.penup()
t3.goto(0,300)
t3.pendown()
t3.write("Merry christmas!", font=("Arial", 24, "bold"), align="center")
t3.hideturtle()



turtle.done()