from turtle import Turtle, Screen
import random
import turtle as tr

def randomColor():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  rc = (r,g,b)
  return rc

t = Turtle()
t.speed("slow")

tr.colormode(255)
t.shape("turtle")

t.color("Green")

dir = [90,180,270]

t.pensize(10)

for i in range(1,100):
   t.pencolor(randomColor())
   t.left(random.choice(dir))
   t.forward(100)

s = Screen()

s.exitonclick()
