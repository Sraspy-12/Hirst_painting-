'''USING COLORGRAM TO EXTRACT SPECIFIC COLORS FROM HIRST PAINTING AND APPEND IT INTO A LIST IN RGB FORMAT'''

# import colorgram
# list = []
# colors = colorgram.extract("hirst.jpg",30)
# for extracted_color in colors:
#
#     r = extracted_color.rgb.r
#     g = extracted_color.rgb.g
#     b = extracted_color.rgb.b
#     new_color = (r,g,b)
#     list.append(new_color)
# print(list)

import turtle
from random import choice
from turtle import Turtle,Screen

turtle.colormode(255)
hirst_colors = [(234, 226, 211), (193, 61, 19), (212, 154, 93), (217, 218, 226), (141, 144, 155), (97, 105, 137), (230, 212, 107), (193, 158, 26), (234, 216, 224), (208, 150, 177), (91, 113, 181), (35, 38, 15), (19, 28, 71), (226, 233, 227), (224, 168, 199), (25, 42, 23), (194, 23, 3), (36, 49, 106), (207, 94, 64), (234, 205, 9), (236, 173, 158), (111, 97, 106), (181, 186, 212), (90, 101, 91), (155, 164, 156), (210, 88, 115), (73, 72, 39), (43, 26, 41), (53, 71, 54), (109, 40, 53)]

saras = Turtle()
saras.speed(0)
saras.setheading(225)
saras.penup()
saras.hideturtle()
saras.forward(300)
saras.setheading(0)
print(saras.xcor())
print(saras.ycor())
p = -212.13203435596427


for x in range(10):
    for y in range(10):
        saras.dot(25, choice(hirst_colors))
        saras.penup()
        saras.forward(50)
        p += 5
    saras.setpos(x=-212.13203435596424,y=p)
    # saras.dot(20,choice(hirst_colors))
    # saras.penup()
    # saras.left(90)
    # saras.forward(50)
    # saras.pendown()












my_screen = Screen()
my_screen.exitonclick()