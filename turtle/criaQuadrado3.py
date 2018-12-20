import turtle
import random


def draw_turtle():
    

    window = turtle.Screen()
    window.bgcolor("#82B2FF") #cor da tela 
    rishi = turtle.Turtle()
    rishi.shape("turtle")
    rishi.color("#FFFFFF")
    rishi.width(2)
    rishi.speed(8)
    rishi.pos(100,500)
    
    for i in range(4,10):
        
        rishi.forward(100)
        rishi.right(90)
        rishi.forward(100)
        rishi.right(90)
        rishi.forward(100)
        rishi.right(90)
        rishi.forward(100)
        rishi.right(100)
        rishi.speed(1)
        rishi.forward(200)


    window.exitonclick()


draw_turtle()
