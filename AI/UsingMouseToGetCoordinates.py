from re import T
import turtle as tur
import tkinter as tk

pen = tur.Turtle()
head = tur.Turtle()
screen = tur.Screen()
screen.bgcolor("cyan")
canvas = screen.getcanvas()
head.penup()
head.hideturtle()
head.goto(0, 260)
head.write("This is to display the coordinates of the position where mouse is clicked", align = "center", font = ("times new roman", 12, "normal"))

pen.shape("turtle")
pen.speed(5)
pen.color("black")
pen.dot(20, "#FFA500")

def btnclick(x, y):
	pen.goto(x, y)
	head.clear()
	head.write(f"x coordinate = {x}, y coordinate = {y}", align = "center", font = ("times new roman", 16, "normal"))
	pen.dot(20, "#FFA500")

def stop_pen(t):
	if t == True:
		t = False
		return t
	t = True
	return t
t = True
while(t):
	tur.onscreenclick(btnclick, 1)
	tur.listen()

B = tk.Button(canvas.master, text = "Stop", command = stop_pen(t))
canvas.create_window(-200, -200, window=B)
B.pack()
tur.mainloop()