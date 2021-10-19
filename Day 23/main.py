import random
import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    random_chance = random.randint(1, 6)
    time.sleep(0.1)
    screen.update()
    if random_chance == 1:
        car_manager.create_car()
    car_manager.move()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.GAME_OVER()
            game_is_on = False

    if player.ycor() > 280:
        player.finish()
        car_manager.change_speed()
        scoreboard.update_score()

screen.exitonclick()
