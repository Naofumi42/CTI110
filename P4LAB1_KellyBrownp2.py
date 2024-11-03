import turtle as t

# Function to draw the letter 'K'
def draw_initial_k():

    t.pen()
    t.pendown()
    t.pensize(3)
    t.right(90)
    t.forward(200)
    t.backward(100)
    t.left(45)
    t.forward(100)
    t.backward(100)
    t.left(80)
    t.forward(100)
    
# Function to draw the letter 'B'
def draw_initial_b():
    t.pendown()
    t.left(90)
    t.forward(50)  
    t.right(90)
    t.circle(-15, 180)  
    t.right(180)
    t.circle(-15, 180)  
    t.penup()

# Set up the turtle
t.speed(1)  
t.color("green")  

# Draw the initials
draw_initial_k()
t.penup() 
t.goto(70, 0)  
t.pendown()  
draw_initial_b()

# Complete the drawing
t.done()

