from turtle import Turtle

SCOREBOARD_COLOR = "white"
SCORE_POSITION = (0, 240)
ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color(SCOREBOARD_COLOR)
        self.penup()
        self.goto(SCORE_POSITION)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.l_score}/{self.r_score}", align=ALIGNMENT, font=FONT)

    def add_score_l(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def add_score_r(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()
