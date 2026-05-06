from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(x=0, y=265)
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}",move=False, align="center", font= ('Courier', 30, "normal"))

    def add_point(self):
        self.score += 1

