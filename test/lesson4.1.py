import turtle as t
window = t.Screen()
t.shape("turtle")
t.color("purple")
t.bgcolor("black")
t.speed(100)
t.pensize(3)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(360):
    t.color(colors[i % len(colors)])
    t.pensize(i/100+1)
    t.forward(i)
    t.left(59)

window.exitonclick()
