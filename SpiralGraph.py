import turtle as t
import random as ran

def random_color():
    r = ran.randint(0,255)
    g = ran.randint(0,255)
    b = ran.randint(0,255)
    return (r,g,b)

t.colormode(255)
t.speed("slowest")

bun = t.Turtle()

for _ in range(100):
   t.color(random_color())
   t.setheading(t.heading()+5)
   t.circle(100)
screen = t.Screen()
screen.exitonclick()


