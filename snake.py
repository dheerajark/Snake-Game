from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40,0)]
MOVE_FORWARD = 20
# X_POSITION = [-40, -20, 0]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for snake_index in STARTING_POSITION:
            self.add_segment(snake_index)

    def add_segment(self, snake_index):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        # new_segment.goto(x=X_POSITION[snake_index], y=0)
        self.segment.append(new_segment)

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            ney_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, ney_y)
        self.head.forward(MOVE_FORWARD)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
