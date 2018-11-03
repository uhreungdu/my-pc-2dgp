import game_framework
from pico2d import *

import game_world
import resource_manage
import random
from bullet import Bullet

PIXEL_PER_METER = (1.0 / 0.3)
RUN_SPEED_KMPH = 10
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8



class Wheel:
    image = None
    def __init__(self):
        if Wheel.image == None:
            Wheel.image = resource_manage.resouse.spri_Wheel_enemy
        self.x, self.y = 1350, 500 + random.randint(-100, 100)
        self.velocity = 0
        self.frame = 0
        self.popup = True
        self.fire = False
        self.cur_time = game_framework.frame_time
        self.count = 0
        self.dir = 0


    def update(self):
        self.velocity += 0.05
        if self.velocity > 10 and self.popup == True:
            self.x -= 0.5
            if self.x <= 900:
                self.popup = False
                self.x += 0
        if self.popup == False:
            self.x += 0
            self.count += 0.5
            if((self.count) % 50 == 0):
                if(self.count <= 400):
                    self.fire = True
                if(self.fire == True):
                    ball = Bullet(self.x, self.y, -2, 2)
                    game_world.add_object(ball, 1)
                else:
                    pass
            if((self.count) >= 400):
                self.fire = False
                self.dir = 1
                self.x += 0.5
                if self.x >= 1350:
                    self.popup = True
                    self.y += random.randint(-200,200)
                    self.count = 0
                    self.velocity = 0
                    self.dir = 0





    def draw(self):
        if self.dir == 0:
            resource_manage.resouse.spri_Wheel_enemy.clip_composite_draw(0, 516, 50, 50, 0, 'h', self.x, self.y, 50, 50)
        if self.dir == 1:
            resource_manage.resouse.spri_Wheel_enemy.clip_composite_draw(0, 516, 50, 50, 0, '', self.x, self.y, 50, 50)





    def handle_event(self, event):
        pass





