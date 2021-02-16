from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal", "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.color("white")
        self.speed("fastest")
        self.score = 0
        self.goto(0, 260)
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score}",
                   align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER",
                   align=ALIGNMENT, font=FONT)