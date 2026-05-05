from turtle import Turtle,Screen

screen = Screen()
screen.setup(width=600, height=600)
(screen.bgcolor("black"))
screen.title("My Snake Game")

root = screen.getcanvas().winfo_toplevel()
root.call('wm', 'attributes', '.', '-topmost', '1')

snake_length = 3

for i in range(snake_length):
    sp = Turtle()
    sp.color("white")
    sp.shape("square")
    sp.setx(i*-20)

screen.exitonclick()