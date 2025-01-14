import turtle
def draw_tree(t):
 length = 600
 colors = ["red","blue","green","black"]
 i = 0
 while(length >= 0):
  if(i > 3):
   i = 0
  else:
   t.color(colors[i])
   i += 1
  t.forward(length)
  t.right(90)
  length -= 1
  
 
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed("fastest")
t.left(90) # Start pointing upwards
t.penup()
t.goto(-300, -300) # Start near the bottom of the screen
t.pendown()
# Draw fractal tree
draw_tree(t)
screen.exitonclick()