import turtle as t

tim = t.Turtle()
screen = t.Screen()


def move():
    tim.forward(10)


def back():
    tim.backward(10)


def clockwise():
    direction = tim.heading()
    tim.setheading(direction-10)


def counter_clockwise():
    direction = tim.heading()
    tim.setheading(direction+10)


def clear():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move)
screen.onkey(key="s", fun=back)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
