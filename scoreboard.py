from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.highscore = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.write(f"score: {self.score} ; hi score: {self.highscore}", align="center", font=("arial", 22, "normal"))
        # if food.refresh_():
        #     self.SCORE += 1
        # self.update()

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"score: {self.score} ; hi score: {self.highscore}", align="center", font=("arial", 22, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update()

    def game_over(self):
        self.penup()
        self.goto((0, 0))
        self.write("GAME OVER", align="center", font=("arial", 22, "normal"))


