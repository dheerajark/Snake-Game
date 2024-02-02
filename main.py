from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()                      # when this line trigger it initialize the (__init__) function.
# so that it crates a 3 block of square(snake).


scoreboard = Score()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# y_position =
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    if snake.head.distance(food) < 15:
        scoreboard.update()
        snake.extend()
        food.refresh_()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        is_game_on = False
        scoreboard.game_over()

    # detect collision with tail
    # for segment in snake.segment[1:]:
    #     if snake.head.distance(segment) < 10:
    #         scoreboard.game_over()
    # if head collide with any of the segment
    #     trigger game over
screen.exitonclick()
