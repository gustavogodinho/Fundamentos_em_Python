import turtle
import random
def draw_square():
    window = turtle.Screen()
    brad = turtle.Turtle()
    window.bgcolor("black")
    brad.shape("turtle")
    distance = 120
    colors = ["white", "yellow", "green", "blue", "red", "purple"]
    brad.speed(2)
    for laps in range(0,150):
        for in_laps in range(0,3):
             brad.color(colors[int(random.randrange(0,len(colors)))])
             brad.forward(distance + laps*2)
             brad.right(90 + in_laps*3)  
    window.exitonclick()
draw_square()
