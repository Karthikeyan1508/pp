import turtle

def draw_triangle(t, x, y, size, color):
    """Draws a filled triangle with the given color."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

def sierpinski(t, x, y, size, depth, change_depth):
    """Recursively draws the Sierpinski triangle."""
    if depth == 0:
        draw_triangle(t, x, y, size, "black")  # Base color for small triangles
    else:
        new_size = size / 2
        sierpinski(t, x, y, new_size, depth - 1, change_depth)
        sierpinski(t, x + new_size, y, new_size, depth - 1, change_depth)
        sierpinski(t, x + new_size / 2, y + (new_size * (3 ** 0.5) / 2), new_size, depth - 1, change_depth)

        if depth == change_depth:
            draw_triangle(t, x, y, new_size, "red")
            draw_triangle(t, x + new_size, y, new_size, "blue")
            draw_triangle(t, x + new_size / 2, y + (new_size * (3 ** 0.5) / 2), new_size, "magenta")

# Initialize turtle
t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()
screen.bgcolor("white")

change_depth = 2  # Depth level where colors change
sierpinski(t, -200, -200, 400, 4, change_depth)  # Change depth here to see different levels

turtle.done()
