import turtle

def koch_curve(t, x1, y1, x2, y2, depth):
    """Recursively draws a Koch curve between two points."""
    if depth == 0:
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.goto(x2, y2)
    else:
        # Calculate the three dividing points
        xa = x1 + (x2 - x1) / 3
        ya = y1 + (y2 - y1) / 3
        xb = x1 + 2 * (x2 - x1) / 3
        yb = y1 + 2 * (y2 - y1) / 3

        # Calculate the peak of the equilateral triangle
        xc = (x1 + x2) / 2 - (y2 - y1) * (3**0.5) / 6
        yc = (y1 + y2) / 2 + (x2 - x1) * (3**0.5) / 6

        # Recursive calls for each segment
        koch_curve(t, x1, y1, xa, ya, depth - 1)
        koch_curve(t, xa, ya, xc, yc, depth - 1)
        koch_curve(t, xc, yc, xb, yb, depth - 1)
        koch_curve(t, xb, yb, x2, y2, depth - 1)

def koch_snowflake(t, depth, size):
    """Draws a Koch snowflake of a given depth and size."""
    # Calculate initial equilateral triangle coordinates
    x1, y1 = -size / 2, size * (3**0.5) / 6
    x2, y2 = size / 2, size * (3**0.5) / 6
    x3, y3 = 0, -size * (3**0.5) / 3

    # Draw the three Koch curves forming the snowflake
    koch_curve(t, x1, y1, x2, y2, depth)
    koch_curve(t, x2, y2, x3, y3, depth)
    koch_curve(t, x3, y3, x1, y1, depth)

# Initialize Turtle
t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()
screen.bgcolor("white")

# Set recursion depth and size of the snowflake
depth = 3  # Change this to adjust complexity
size = 300  # Overall size of the snowflake

koch_snowflake(t, depth, size)

turtle.done()
