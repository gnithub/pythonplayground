from turtle import *

t = Turtle()


for i in range(0,10):
   t.dot()
   t.forward(50)
   if i%3 == 0:
      t.setheading(90)
      t.forward(50)
      t.setheading(180)
      t.forward(150)
      t.setheading(0)

s = Screen()
s.exitonclick()

