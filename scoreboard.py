from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')

    def set_score(self):
        self.write(arg=f"Score: {self.score}",move=False, align="center", font= ('Courier', 8, "bold"))
