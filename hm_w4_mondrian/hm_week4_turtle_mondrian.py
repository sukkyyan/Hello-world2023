-# This is Suuky Yan Week 4 Assignment

# Part 1
# <Disorder>

# This is a generative artwork saluted to Mondiran which using loop


# Experiement 1
# At first, I tried to uese generate radom rectangles to mimic Mondrian style
# However, the outcome is not ideal since the lower right corner of all rectangles is the origin. 

#________________________________________________________________________________________________
# import turtle
# import random


# turtle.screensize(1000,1000)
# turtle.setworldcoordinates(-500,-500,500,500)

# piet = turtle.Turtle()
# piet.speed(100)


# rectangles = 8 #int(input('How many rectangles '))
# rectangle_w = 500 #int(input('Max width of the rectangles? '))
# rectangle_h = 500 #int(input('Max height of the rectangles? '))

# def randomstart():
# 	for n in range (60):
# 		piet.penup()
# 		piet.goto(random.randint(-400, 400), random.randint(-400, 400))
# 		piet.pendown()
		

# def mondrian(t,random_w, random_h):
#     piet.fillcolor(random.choice(('red','blue','yellow')))
#     piet.begin_fill()
#     for box in range(2):
#         t.left(90)
#         t.forward(random_w)
#         t.left(90)
#         t.forward(random_h)
#     piet.end_fill()

# def repeat_mondrian():
#     for i in range(rectangles):
#         mondrian(piet,
#                  random.randint(10, rectangle_w),
#                  random.randint(10, rectangle_h))


# repeat_mondrian()





#________________________________________________________________________________________________     
# Experiement 2
# Then I drew the color blocks in modularization
# One point is that I add the 'collection' function

import turtle as turtle_graphics
import random
import collections

borderColor = '#000000'  # black canvas

borderWidth = 7
minimumDivisionPortion = 0.15  # limits recursion

colors = ('white', 'red', 'white', 'blue', 'yellow')  # multiple 'white' to increase probability

Bounds = collections.namedtuple('Bounds', ['x', 'y', 'width', 'height'])

PICTURE_BOUNDS = Bounds(x=-250, y=-300, width=500, height=600)

# Random color 
# Fill a rectangle with the border color (black) and then fill the center with a bright color (r,y,b)
def fill_rectangle(turtle, bounds, color=borderColor):
    turtle.penup()
    turtle.goto(bounds.x, bounds.y)
    turtle.color(color)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(bounds.width)
        turtle.left(90)
        turtle.forward(bounds.height)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()

    if color == borderColor:
        fill_rectangle(turtle, Bounds(bounds.x + borderWidth, bounds.y + borderWidth, bounds.width - borderWidth*2, bounds.height - borderWidth*2), random.choice(colors))


# Random division
# Divide and fill.  Intuitively and recursively
def mondrian(piet, bounds):

    if bounds.width < bounds.height:
        dimension = 'height'
        random_dimension = random.randint(getattr(bounds, dimension) // 5, 2 * getattr(bounds, dimension) // 3)
        bounds_yin = Bounds(bounds.x, y=bounds.y + random_dimension, width=bounds.width, height=bounds.height - random_dimension)
        bounds_yang = Bounds(bounds.x, bounds.y, bounds.width, random_dimension)
    else:
        dimension = 'width'
        random_dimension = random.randint(getattr(bounds, dimension) // 5, 2 * getattr(bounds, dimension) // 3)
        bounds_yin = Bounds(bounds.x, bounds.y, random_dimension, bounds.height)
        bounds_yang = Bounds(x=bounds.x + random_dimension, y=bounds.y, width=bounds.width - random_dimension, height=bounds.height)

    if getattr(bounds_yin, dimension) > getattr(bounds_yang, dimension):
        bounds_paint, bounds_divide = bounds_yang, bounds_yin
    else:
        bounds_paint, bounds_divide = bounds_yin, bounds_yang

    fill_rectangle(piet, bounds_paint)

    if getattr(bounds_divide, dimension) < minimumDivisionPortion * getattr(PICTURE_BOUNDS, dimension):
        fill_rectangle(piet, bounds_divide)
    else:
        mondrian(piet, bounds_divide)


# Runs the program and can be used as an event handler 
def paint_canvas(dummy_x=0, dummy_y=0):
    turtle_graphics.onscreenclick(None)
    fill_rectangle(turtle_graphics, PICTURE_BOUNDS, 'black')
    mondrian(turtle_graphics, PICTURE_BOUNDS)
    turtle_graphics.onscreenclick(paint_canvas)

turtle_graphics.screensize(PICTURE_BOUNDS.width, PICTURE_BOUNDS.height)
turtle_graphics.speed('fastest')
turtle_graphics.hideturtle()

paint_canvas()

turtle_graphics.listen()

turtle_graphics.mainloop()





# #  File: Mondrian.py

# #  Description: Will make random, abstract mondrian influenced art.

# #  Student Name: Sukky Yan

# #  Date Created:10-3-21

# #  Date Last Modified:10-6-21

