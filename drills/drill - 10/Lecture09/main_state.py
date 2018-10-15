import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"

boy = None
grass = None
font = None



class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.dir = 0

    def update(self):
        self.frame = (self.frame + 1) % 8
        if (self.dir == -1):
            self.move_left()

        elif (self.dir == 1):
            self.move_right()

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def move_left(self):
        if(self.x > 0):
            self.x += -1
    def move_right(self):
        if(self.x < 800):
            self.x += 1


def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()


def exit():
    global boy,grass
    del(boy)
    del(grass)


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
            game_framework.change_state(title_state)

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                boy.dir = -1
            elif event.key == SDLK_RIGHT:
                boy.dir = 1
            elif event.key == SDLK_p:
                game_framework.push_state(pause_state)

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                boy.dir = 0
            elif event.key == SDLK_RIGHT:
                boy.dir = 0


def update():
    boy.update()


def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()





