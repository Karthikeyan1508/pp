import turtle

num_sides = int(input("Enter the number of sides: "))
side_length = int(input("Enter the length of each side: "))
pen_color = input("Enter the pen color: ")
fill_color = input("Enter the fill color: ")

t = turtle.Turtle()
t.color(pen_color)
t.fillcolor(fill_color)

angle = 360 / num_sides
t.begin_fill()
for i in range(num_sides):
    t.forward(side_length)
    t.right(angle)
t.end_fill()

turtle.done()
