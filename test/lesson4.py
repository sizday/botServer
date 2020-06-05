import turtle as t
window = t.Screen()
t.shape("turtle")
t.color("red")
t.bgcolor("white")
t.speed(10)
t.pensize(3)
count = int(input("Введите кол-во углов которое хочешь?"))
for i in range(count):
    t.forward(50)
    t.left(360/count)

window.exitonclick()
