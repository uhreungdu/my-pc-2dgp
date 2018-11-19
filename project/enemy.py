import game_framework
from pico2d import *

import game_world
import resource_manage
import random
import main_game
from bullet import Bullet

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 15
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)



Bullet_SPEED_KMPH = 0.1
Bullet_SPEED_MPM = (Bullet_SPEED_KMPH * 1000.0 / 60.0)
Bullet_SPEED_MPS = (Bullet_SPEED_MPM / 60.0)
Bullet_SPEED_PPS = (Bullet_SPEED_MPS * PIXEL_PER_METER)

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
        self.popup = 0
        self.fire = False
        self.cur_time = get_time()
        self.now_time = get_time()
        self.second_time = 0
        self.count = 0
        self.dir = 0
        self.paturn = 0


    def update(self):
        self.velocity += 0.05
        self.now_time = get_time()
        if (self.now_time - self.cur_time) > 2 and self.popup == 0:
            self.x -= RUN_SPEED_PPS * game_framework.frame_time
            if self.x <= 900:
                self.second_time = get_time()
                self.cur_time = get_time()
                self.popup = 1

        if self.popup == 1:
            self.x += 0
            self.count += 0.5

            if (self.now_time - self.second_time) >= 0.25:
                ball = Bullet(self.x, self.y, -RUN_SPEED_PPS, 2, self.paturn)
                game_world.add_object(ball, 1)
                self.second_time = get_time()
            if (self.now_time - self.cur_time) >= 2:
                self.popup = 2
        if self.popup == 2:
            self.dir = 1
            self.x += RUN_SPEED_PPS * game_framework.frame_time
            if self.x >= 1350:
                self.x = 1320
                self.popup = 0
                if self.y <= 900:
                    self.y += random.randint(-200, 150)
                if self.y >= 900:
                    self.y += random.randint(-400, -200)
                self.count = 0
                self.velocity = 0
                self.dir = 0
                self.paturn = random.randint(0, 3)






    def draw(self):
        if self.dir == 0:
            resource_manage.resouse.spri_Wheel_enemy.clip_composite_draw(0, 516, 50, 50, 0, 'h', self.x, self.y, 50, 50)
        if self.dir == 1:
            resource_manage.resouse.spri_Wheel_enemy.clip_composite_draw(0, 516, 50, 50, 0, '', self.x, self.y, 50, 50)





    def handle_event(self, event):
        pass





