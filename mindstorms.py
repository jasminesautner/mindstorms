import turtle

def draw_square(some_turtle):
#    window = turtle.Screen()
#    window.bgcolor("red")
    for i in range(0,4):
        some_turtle.forward(100)
        some_turtle.right(90)   


#    brad = turtle.Turtle()
#    brad.shape("turtle")
#    brad.color("yellow")
#    brad.speed(2)

#    for i in range(0,4):
#       brad.forward(100)
#       brad.right(90)

#    angie = turtle.Turtle()
#    angie.shape("arrow")
#    angie.color("blue")
#    angie.circle(100)

#    tom = turtle.Turtle()
#    tom.shape("turtle")
#    tom.color("green")

#    tom.forward(100)
#    tom.left(120)
#    tom.forward(100)
#    tom.left(120)
#    tom.forward(100)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #create the turtle Brad - Draws a square
    # brad = turtle.Turtle()
    # brad.shape("turtle")
    # brad.color("yellow")
    # brad.speed(2)
    # for i in range(1,37):
      #  draw_square(brad)
      #  brad.right(10)
    #draw_square(brad)
    # Create the turtle Angie - Draws a circle
    # angie = turtle.Turtle()
    # angie.shape("arrow")
    # angie.color("blue")
    # angie.circle(100)

#    tom = turtle.Turtle()
#    tom.shape("turtle")
#    tom.color("green")
#    for i in range(1, 38):
#       tom.forward(100)
#       tom.left(120)    
 
def draw_flower():
        window = turtle.Screen()
        window.bgcolor("blue")
      
        pen = turtle.Turtle()
        pen.shape("turtle")
        pen.color("#99ff00")

        for i in range(0,36):
               draw_square(pen)
               pen.right(30)

        for i in range(0,4):
                pen.circle(80)
                pen.right(90)

        pen.right(90)
        pen.forward(300)
        pen.right(90)
        draw_square(pen)
        pen.left(180)
        draw_square(pen)
        pen.left(270)
        pen.forward(200)

        window.exitonclick()
 
# draw_art()
draw_flower()
