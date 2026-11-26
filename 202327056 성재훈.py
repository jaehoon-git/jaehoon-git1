# 구구단

def print_gugudan(dan):
    for i in range(1, 10):
        print(f"{dan} × {i} = {dan * i}")

dan = int(input("몇 단을 출력할까요? "))
print_gugudan(dan)


#스마일그리기

import turtle

turtle.setup(400, 400)
turtle.title("스마일")
turtle.speed(2)
turtle.hideturtle()
turtle.penup()


turtle.goto(0, 0)
turtle.dot(240, "#FFDF35")


turtle.goto(-33, 35)
turtle.dot(24, "black")

turtle.goto(33, 35)
turtle.dot(24, "black")


turtle.goto(-56, -20)
turtle.setheading(-70)
turtle.pencolor("black")
turtle.pensize(12)
turtle.pendown()
turtle.circle(60, 140)

turtle.done()