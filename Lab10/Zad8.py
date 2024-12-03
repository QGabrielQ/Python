import turtle
def draw_tree(branch_length, t):
 if branch_length > 30:
   t.color("brown")
 else:
   t.color("green")
 if branch_length > 5: # Base case
# Draw main branch
    t.forward(branch_length)
# Recursive call for the right subtree
    t.right(20)
    draw_tree(branch_length - 15, t)
# Return to the main branch and adjust direction
    t.left(40)
    draw_tree(branch_length - 15, t)
# Reset orientation
    t.right(20)
    t.backward(branch_length)
# Setup Turtle
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.color("green")
t.speed("fastest")
t.left(90) # Start pointing upwards
t.penup()
t.goto(0, -300) # Start near the bottom of the screen
t.pendown()
# Draw fractal tree
draw_tree(100, t)
screen.exitonclick()

# def koch_curve(t, length, level):
#  if level == 0: # Base case
#   t.forward(length)
#  else:
#   length /= 3.0
#   koch_curve(t, length, level - 1)
#   t.left(60)
#   koch_curve(t, length, level - 1)
#   t.right(120)
#   koch_curve(t, length, level - 1)
#   t.left(60)
#   koch_curve(t, length, level - 1)
# # Setup Turtle
# screen = turtle.Screen()
# screen.bgcolor("white")
# t = turtle.Turtle()
# t.speed("fastest")
# # Draw Koch snowflake
# for i in range(3): # 3 sides of the snowflake
#   koch_curve(t, 300, 3) # Level 3 recursion
#   t.right(120)