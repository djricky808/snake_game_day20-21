from turtle import Turtle,Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
(screen.bgcolor("black"))
screen.title("My Snake Game")
screen.tracer(0) #Keeps the screen from automatically updated unless being told to.

root = screen.getcanvas().winfo_toplevel()
root.call('wm', 'attributes', '.', '-topmost', '1')

# snake_length = 3
#
# for i in range(snake_length):
#     sp = Turtle()
#     sp.color("white")
#     sp.shape("square")
#     sp.setx(i*-20)

starting_positions = [(0,0), (-20,0), (-40,0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position) #set the turtles to the X,Y coordinate designated
    segments.append(new_segment)


game_is_on = True
while game_is_on:
    screen.update() #updates the turtle screen, kept outside the for loop so that the snake updates when all the segments already moved
    time.sleep(0.1) #updates the speed of which the code runs, a higher number means a higher pause.

    for seg_num in range (len(segments) -1, 0, -1 ): #range(start, stop, increment) this how to loop backwards LIFO
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y) #This sets the segments to take the place of the previous segment. 3 moves to where 2 is, 2 to where 1 is, etc.
    segments[0].forward(20)


screen.exitonclick()