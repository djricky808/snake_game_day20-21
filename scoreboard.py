from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 30 , "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(x=0, y=265)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score: {self.score}",move=False, align=ALIGNMENT, font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font= FONT)

    def add_point(self):
        self.score += 1
        self.clear()
        self.update_score()

