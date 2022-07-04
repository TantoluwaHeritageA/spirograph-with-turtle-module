import random
# import turtle
import turtle as t
from turtle import Turtle , Screen

timmy_the_turtle = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0 , 255)
    g = random.randint(0 , 255)
    b = random.randint(0 , 255)
    color = (r , g , b)
    return color


timmy_the_turtle.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)
draw_spirograph(5)
    # for _ in range(150):


#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.circle(100)
#     timmy_the_turtle.setheading(timmy_the_turtle.heading() + 10)
# for _ in range(150):

# timmy_the_turtle.color(random.choice(color))

# def random_color():
#     r = random.randint(0 , 255)
#     g = random.randint(0 , 255)
#     b = random.randint(0 , 255)
#     random_color = (r , g , b)
#     return random_color
#
#
# for _ in range(8):
#     timmy_the_turtle.color(random_color())
#
#     timmy_the_turtle.right(45)
#     timmy_the_turtle.circle(50)
# timmy_the_turtle.left(0)

# timmy_the_turtle.color("yellow")
# to draw a square
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)
# to draw a dotted line
# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()
#
# import random
# import turtle as t
# from turtle import Turtle , Screen
#
# timmy_the_turtle = t.Turtle()
# t.colormode(255)
#
#
# def random_color():
#     r = random.randint(0 , 255)
#     g = random.randint(0 , 255)
#     b = random.randint(0 , 255)
#     random_color = (r , g , b)
#     return random_color
#
#
# # color = ["green" , "blue" , "yellow" , "black" , "pink" , "grey" , "brown" , "coral"]
#
# directions = [0 , 90 , 180 , 270]
# timmy_the_turtle.pensize(15)
# timmy_the_turtle.speed("fastest")
#
# for _ in range(150):
#     timmy_the_turtle.color(random_color())
#     # timmy_the_turtle.color(random.choice(color))
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(directions))
#
#                                   
# def draw_shape(num_of_sides):
#     angle = 360 / num_of_sides
#     for _ in range(num_of_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
#
#
# for shape_side_n in range(3 , 11):
#     timmy_the_turtle.color(random.choice(color))
#     draw_shape(shape_side_n)


# my code
# # to draw a triangle
# for _ in range(3):
#     timmy_the_turtle.color("red")
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(120)
#
# #to draw a square
# for _ in range(4):
#     timmy_the_turtle.color("yellow")
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
# # to draw a pentagon
# for _ in range(5):
#     timmy_the_turtle.color("blue")
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(72)
#
# # to draw a hexagon
# for _ in range(6):
#     timmy_the_turtle.color("pink")
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(60)
#
# # to draw a heptagon
# for _ in range(7):
#     timmy_the_turtle.color("black")
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(51.43)
#
# # to draw a octagon
# for _ in range(8):
#     timmy_the_turtle.color("brown")
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(45)
#
# # to draw a nonagon
# for _ in range(9):
#     timmy_the_turtle.color("green")
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(40)
#
# # to draw a decagon
# for _ in range(10):
#     timmy_the_turtle.color("orange")
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(36)


# my code
# timmy_the_turtle.right(270)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(-90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(-270)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(-90)
# timmy_the_turtle.forward(100)


screen = Screen()
screen.exitonclick()
