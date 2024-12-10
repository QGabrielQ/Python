import turtle
def draw_tree(t):
 length = 500
 while(length >= 0):
  t.forward(length)
  t.right(90)
  t.forward(length)
  t.right(90)
  length -= 5
 
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.color("green")
t.speed("fastest")
t.left(90) # Start pointing upwards
t.penup()
t.goto(-300, -300) # Start near the bottom of the screen
t.pendown()
# Draw fractal tree
draw_tree(t)
screen.exitonclick()