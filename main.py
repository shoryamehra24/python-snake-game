from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score


screen = Screen()
screen.setup(height=600, width=600)
screen.title("The Python Snake Game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score = Score()

food.refresh()


game_on = True
while game_on:
    score.starting_score()
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Key Commands
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")

    # Collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        score.new_score()

    # Collision with wall
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.game_over()
        game_on = False

    # Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            score.game_over()
            game_on = False




















screen.exitonclick()


