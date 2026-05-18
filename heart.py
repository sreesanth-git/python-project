import turtle

# Create screen
wn = turtle.Screen()
wn.title("Heart Shape with Text")
wn.bgcolor("white")

# Create turtle
pen = turtle.Turtle()
pen.color("black")
pen.pensize(10)
pen.speed(1)

# Function to draw heart
def draw_heart():
    pen.begin_fill()
    pen.left(140)
    pen.forward(180)
    pen.circle(-90, 200)
    pen.left(120)
    pen.circle(-90, 200)
    pen.forward(180)
    pen.end_fill()

# Function to write text
def write_text():
    pen.up()
    pen.setpos(0, 150)
    pen.down()
    pen.color("white")

    pen.write(
        "Vella panikkum poda😁",
        align="center",
        font=("Arial", 20, "italic", "bold")
    )

# Draw heart
draw_heart()

# Write text inside heart
write_text()

# Hide turtle and finish
pen.hideturtle()
wn.mainloop()