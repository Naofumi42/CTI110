import turtle as t

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Function to draw a triangle
def draw_triangle(size):
    for _ in range(3):
        t.forward(size)
        t.right(120)

# Set up the turtle
t.speed(1)
t.color("blue")  
draw_square(100)  

# Move the turtle to a new position for the triangle
t.penup()  
t.goto(50, 100)  
t.pendown()  
t.color("red")  
draw_triangle(100) 

# Complete the drawing
t.done()
