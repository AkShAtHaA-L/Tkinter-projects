from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.high_score = 0
        self.color("white")
        self.write_score()

    def write_score(self):
        score = "Score: "+str(self.current_score)+"  High Score: "+str(self.high_score)
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.clear()
        self.write(score, False, "center", ('Arial', 20, 'normal'))

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score

        self.current_score = 0

    #
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!", False, "center", ('Arial', 20, 'normal'))