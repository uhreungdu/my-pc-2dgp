import random
from pico2d import *
import game_world
import game_framework
import background

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(50, 1800 - 50),\
                                          random.randint(20, 1100 - 50), 0
        self.cx, self.cy = 0,0

    def get_bb(self):
        return self.cx - 10, self.cy - 10, self.cx + 10, self.cy + 10



    def set_background(self,bg):
        self.bg = bg
        self.x = random.randint(50, 1800 - 50)
        self.y = random.randint(20, 1100 - 25)

    def draw(self):
        self.cx = self.x - self.bg.window_left
        self.cy = self.y - self.bg.window_bottom
        self.image.draw(self.cx, self.cy)
        draw_rectangle(*self.get_bb())
    def update(self):
        self.x = clamp(50, self.x, 1800-50)
        self.y = clamp(20,self.y, 1100-25)
        self.y -= self.fall_speed * game_framework.frame_time

