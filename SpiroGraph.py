import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

repeat_num = 100
gap = 360/repeat_num
for _ in range(repeat_num):
    tim.pencolor(random_color())
    tim.circle(100)
    tim.setheading(gap)
    gap += (360/repeat_num)

screen = t.Screen()
screen.exitonclick()
