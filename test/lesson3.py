import turtle as t
window = t.Screen()
t.reset()
t.shape("turtle")
t.bgcolor("black")
t.speed(100)
t.pensize(2)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(360):
    t.pensize(i/100 + 1)
    t.color(colors[i % len(colors)])
    t.forward(i)
    t.left(59)
t.exitonclick()
