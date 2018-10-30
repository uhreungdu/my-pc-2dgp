import game_framework
from pico2d import *
import random

import main_state
import boy
import game_world
import math

class Ghost:
    image = None

    def __init__(self, x=400, y=300, velocity=1, frame=1):
        if Ghost.image == None:
            Ghost.image = load_image('animation_sheet.png')
        self.x, self.y, self.velocity = x, y, velocity

        self.frame = frame
        self.up = True
        self.angle = 270

    def draw(self):
        if self.velocity == 1:
            self.image.clip_draw(int(self.frame) * 100, 300, 100, 100, self.x, self.y)
            self.image.opacify(0.5)

        else:
            self.image.clip_draw(int(self.frame) * 100, 200, 100, 100, self.x, self.y)
            self.image.opacify(0.5)


    def update(self):
        if main_state.boy.cur_state != boy.SleepState:
            game_world.remove_object(self)

        else:
            if(self.up == True):
                self.y += 5
                if (self.y >= 350):
                    self.up = False

            if(self.up == False):
                self.angle += 720 * game_framework.frame_time
                self.x = (main_state.boy.x) + math.cos(math.pi / 180 * self.angle) * 100
                self.y = (main_state.boy.y + 300) + math.sin(math.pi / 180 * self.angle) * 100



