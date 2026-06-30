import turtle

screen = turtle.Screen()
turtle.setup(1000, 1000)
turtle.title("Game Of Life")
turtle.hideturtle()
turtle.speed(0)
turtle.tracer(0, 0)

n = 25
def draw_line(x1,x2,y1,y2):
    turtle.up()
    turtle.goto(x1, y1)
    turtle.down()
    turtle.goto(x2, y2)

def draw_grid():
    turtle.pencolor('gray')
    turtle.pensize(3)
    x = -400
    for i in range(n+1):
        draw_line(x, -400, x, 400)
        x += 800/n
    y = -400
    for i in range(n+1):
        draw_line(-400, y, 400, y)
        y += 800/n
draw_grid()
screen.update()
screen.exitonclick()