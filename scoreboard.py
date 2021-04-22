from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.count = 0

    def starting_score(self):
        self.write(f"Score: {self.count}", align=ALIGNMENT, font=FONT)

    def new_score(self):
        self.clear()
        self.count += 1
        self.write(f"Score: {self.count}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.color("red")
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)


