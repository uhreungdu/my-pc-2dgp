from pico2d import *
from charater import player
from enemy import Wheel
from Stage_background import Stage
import game_framework
import game_world
import random
import game_over

name = "MainGame"

play = None
wheel_enemy = None
wheel_enemy2 = None
wheel_enemy3 = None
shoot_count = 0
stage = None

def enter():
    global play
    global wheel_enemy
    global wheel_enemy2
    global wheel_enemy3
    global stage
    play = player()
    wheel_enemy = Wheel()
    wheel_enemy2 = Wheel()
    wheel_enemy3 = Wheel()
    stage = Stage()
    game_world.add_object(play, 1)
    game_world.add_object(wheel_enemy, 1)
    game_world.add_object(wheel_enemy2, 1)
    game_world.add_object(wheel_enemy3, 1)
    game_world.add_object(stage, 0)



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
    if play.hp == 0:
        game_world.remove_object(play)
        #game_framework.change_state(game_over)
    update_canvas()

