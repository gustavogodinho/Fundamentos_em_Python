import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("blue")

    brad = turtle.Turtle()
    brad.shape("turtle") 
    brad.color("red")
    brad.speed(1)
    
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

 
    window.exitonclick()
    
draw_square()
