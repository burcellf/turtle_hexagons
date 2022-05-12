from random import randint
import turtle


# Pen settings
t = turtle.Pen()
turtle.colormode(255)
t.pensize(2)
t.speed(10)

# Canvas settings
wn = turtle.Screen()
wn.bgcolor(0, 0, 0)

# Objectively accurate title
wn.title("Generating 120fps, 4k masterpiece...")

# Loop for drawing shapes
for i in range(50):

    # Generate a new color for each loop
    a = randint(80,130)     # deep purple
    b = randint(0,1)
    c = randint(55,105)
    
    t.color(a, b, c)
    t.forward(randint(70,105))
    
    # Draw a small square
    for j in range(4):
        t.forward(8)
        t.right(90)
    
    # Draw a hexagon
    t.forward(randint(21,73))
    t.left(60)
    
    # Add a white square
    if a % 4 == 0:
        t.color(255, 255, 255)
        
        for j in range(4):
            t.forward(8)
            t.right(90)
        t.forward(10)
            
            
t.done()
