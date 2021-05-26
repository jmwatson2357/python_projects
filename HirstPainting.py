import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.hideturtle()
tim.penup()
tim.setposition(-250, -250)
tim.speed("fastest")
color_list = [(192, 172, 108), (131, 173, 185), (153, 62, 82), (56, 109, 155), (228, 217, 123), (126, 96, 80), (139, 181, 130), (207, 151, 164), 
                (69, 120, 77), (86, 159, 95), (94, 120, 176), (143, 33, 46), (61, 50, 47), (183, 80, 98), (73, 59, 56), (197, 117, 54), (222, 173, 180), 
                (143, 119, 115), (174, 205, 178), (165, 200, 209), (95, 17, 26)
                ]

def draw_line():
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
        
def turn(second_turn):
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(second_turn)
    tim.forward(50)

for _ in range(5):
    draw_line()
    turn(180)
    draw_line()
    turn(0)

screen = t.Screen()
screen.exitonclick()
