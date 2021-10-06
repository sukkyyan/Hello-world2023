#for loops for循环
#range表示数列
# for x in range(1,10):
#     print(x)

#for loop, array/ for经常与array数列一起使用
# fruits =["mango", "watermelon", "strawberry", "banana", "apple"]
# for fruit in fruits:
#     print(fruit)

# #while loops/ 若不定义global则无法 def increaseCount
# global x
# x = 0

# def increaseCount():
#     global x
#     x += 1

# while x < 10:
#     increaseCount()
#     print(x)



# # break
# for x in range(1,10):
#     if (x>5):
#         break
#     else:
#         print(x)

# # recursion 递增
# # The most common application is in mathematics and computer science,
# # where a function being defined is applied within its own definition.
# # 
# # draw





# #turtle
# from turtle import *

# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)



# # turtle 2
# from turtle import *
# for i in range(500):
#     forward(i)
#     left(91)



# # a blue flower program
# from turtle import *
# import random



# for n in range(60):
#     penup()
#     goto(random.randint(-400, 400), random.randint(-400, 400)) 
#     pendown() #random下笔位置，画布xy轴400范围里

#     red_amount   = random.randint( 0,  30) / 100.0
#     blue_amount  = random.randint(50, 100) / 100.0
#     green_amount = random.randint( 0,  30) / 100.0
#     pencolor((red_amount, green_amount, blue_amount)) #random颜色值

#     circle_size = random.randint(10, 40)
#     pensize(random.randint(1, 5))  #random圆的大小，笔画的粗细

#     for i in range(6):
#         circle(circle_size)
#         left(60) #开始绘画circle



#turtle 基本function列表
# forward()
# backward()
# right()
# left()
# goto(x,y)
# setx(x)
# sety(y)
# setheading(heading)
# undo()
# home()
# pendown()
# penup()
# pensize(size)
# pencolor()
# clear() 清空drawing但turtle不回到原点
# reset() 清空并回到原点
# fillcolor()
# stamp()







# go to 去到坐标里的那个位置
# from turtle import *
# goto(50, 50)
# goto(-50, 50)
# goto(100, -50)
# goto(-50, -50)

# #setheading 中心发射角度
# from turtle import *

# for angle in range(0, 360, 15):
#     setheading(angle)
#     forward(100)
#     write(str(angle) + '°')
#     backward(100)





# #undo 撤销 原路返回
# from turtle import *

# for i in range(10):
#     forward(100)
#     left(90)
#     forward(10)
#     left(90)
#     forward(100)
#     right(90)
#     forward(10)
#     right(90)

# for i in range(30):
#     undo()


# #home() 回到初始位置
# from turtle import *

# forward(100)
# right(90)
# forward(100)
# home()





# # pencolor()  画笔颜色
# from turtle import *

# pensize(20)
# pencolor('red')
# forward(50)
# pencolor(0, 1.0, 0)
# forward(50)
# pencolor((0, 0.5, 0.5))
# forward(50)

# pensize(10)
# goto(-400, 50)

# for red in range(4):
#     for green in range(4):
#         for blue in range(4):
#             pencolor(red / 4.0, green / 4.0, blue / 4.0)
#             forward(10)




# # filling in shapes 填充颜色
# from  turtle  import  * 

# fillcolor('purple')
# pensize(10)
# pencolor('black')
# forward(100)

# begin_fill()
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# end_fill()


# # Stamping
# from turtle import *

# penup()

# for i in range(30, -1, -1):
#     stamp()
#     left(i)
#     forward(20)



# import turtle 

# smart = turtle.Turtle()

# # Loop 4 times. Everything I want to repeat is 
# # *indented* by four spaces.
# for i in range(4):
#     smart.forward(50)
#     smart.right(90)
    
# # This isn't indented, so we aren't repeating it.
# turtle.done()


# print("start test")

# for i in range(4):
#     print(i)
#     print("test")
    
# print("end test 1")

# for banana in range(20):
#     print(banana)
#     print(banana * 2)



# # drawing a star 绘制五角星
# import turtle 

# star = turtle.Turtle()

# for i in range(50):
#     star.forward(50)  #边长
#     star.right(144)   #angle
    
# turtle.done()


# # spiraling star
# import turtle 

# spiral = turtle.Turtle()

# for i in range(20):
#     spiral.forward(i * i)      #间距变化
#     spiral.right(144)           #angle 五角星的角度
    
# turtle.done()



# Changing line color
# import turtle 

# painter = turtle.Turtle()

# painter.pencolor("blue")

# for i in range(50):
#     painter.forward(50)
#     painter.left(133) # Let's go counterclockwise this time 
    
# painter.pencolor("red")
# for i in range(50):
#     painter.forward(100)
#     painter.left(123)
    
# turtle.done()


# # Nested loops
# import turtle 

# seurat = turtle.Turtle()

# dot_distance = 25
# width = 5
# height = 7

# seurat.penup()

# for y in range(height):
#     for i in range(width):
#         seurat.dot()
#         seurat.forward(dot_distance)
#     seurat.backward(dot_distance * width)
#     seurat.right(90)
#     seurat.forward(dot_distance)
#     seurat.left(90)
    
# turtle.done()



# # Jumping around and changing speed
# import turtle 

# ninja = turtle.Turtle()

# ninja.speed(1)

# for i in range(180):
#     ninja.forward(100)
#     ninja.right(30)
#     ninja.forward(20)
#     ninja.left(60)
#     ninja.forward(50)
#     ninja.right(30)
    
#     ninja.penup()
#     ninja.setposition(0, 0)
#     ninja.pendown()
    
#     ninja.right(2)
    
# turtle.done()



