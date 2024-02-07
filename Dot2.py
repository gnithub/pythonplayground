import turtle as t

teddy = t.Turtle()
for i in range(0,10):
   t.forward(50)
   t.dot()
   if i%3==0:
      t.setheading(180)
      t.forward(150)
      t.setheading(90)

screen = t.Screen()
screen.exitonclick()

