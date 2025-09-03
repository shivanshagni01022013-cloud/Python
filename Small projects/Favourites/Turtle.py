import turtle
import colorsys

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # fastest
turtle.bgcolor("black")  # black background for rainbow pop
turtle.colormode(1)      # allows RGB in 0-1 range

# Rainbow settings
hue = 0
t.pensize(10)

# Infinite rainbow drawing
while True:
    # Convert hue to RGB
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    t.color(r, g, b)

    # Draw the pattern
    t.forward(400)
    t.left(345)
    t.right(50)
    

    t.left(345)
    t.right(50)
    t.left(345)
    t.right(50)
    t.left(345)
    t.right(50)
    t.left(345)
    t.right(50)
    t.left(345)
    t.right(50)
    t.right(50)
    t.left(345)
    t.right(50)
    t.left(345)
    t.right(50)
    t.left(345)
    t.right(50)
    t.left(345)
    t.right(50)
    t.right(50)
    t.left(345)
    t.right(50)
    t.left(345)
    t.right(50)
    t.left(345)
    t.right(50)
    t.left(345)
    t.right(50)
    t.right(50)
    t.left(345)
    t.right(50)
    t.left(345)
    t.right(50)
    t.left(345)
    t.right(50)
    t.left(345)
    t.right(50)
    t.right(50)
    t.left(345)
    t.right(50)
    t.left(345)
    t.right(50)
    t.left(345)
    t.right(50)
    t.left(345)
    t.right(50)
    t.right(50)
    t.left(345)
    t.right(50)
    t.left(345)
    t.right(50)
    t.left(345)
    t.right(50)
    t.left(345)
    t.right(50)
    
    # Increment hue slightly for smooth rainbow shift
    hue += 0.01
    if hue > 1:
        hue = 0
