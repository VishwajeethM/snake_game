from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
with open("data.txt", mode="r") as file:
    HIGHSCORE = file.read()

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = int(HIGHSCORE)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        global HIGHSCORE
        if self.score > self.highscore:
            self.highscore = self.score
            HIGHSCORE = self.highscore
            with open("../../Desktop/data.txt", mode="w") as file:
                file.write(f"{HIGHSCORE}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)

    def inc_score(self):
        self.score += 1
        self.update_scoreboard()
