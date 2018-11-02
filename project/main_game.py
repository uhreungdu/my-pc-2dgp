from pico2d import *
from charater import player
from enemy import Wheel

import game_framework
import game_world
import random

name = "MainGame"

play = None
wheel_enemy = None
shoot_count = 0

def enter():
    global play
    global wheel_enemy
    play = player()
    wheel_enemy = Wheel()
    game_world.add_object(play, 1)
    game_world.add_object(wheel_enemy, 1)



def exit():
    game_world.clear()

def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            play.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

