import game_framework
from pico2d import *

import game_world
import resource_manage
import main_game

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



class Wizard:
    image = None
    def __init__(self):
        if Wizard.image == None:
            Wizard.image = resource_manage.resouse.spri_wizard_boss
        self.x, self.y = 1100, 500
        self.hp = 1000
        self.frame = 0
        self.cur_time = get_time()
        self.now_time = get_time()
        self.second_time = 0
        self.count = 0
        self.dir = 0
        self.paturn = 0
        self.round = 100


    def update(self):
        if self.dir == 0:
            self.y += 0.5
            if self.y >= 550:
                self.dir = 1
        if self.dir == 1:
            self.y -= 0.5
            if self.y <= 450:
                self.dir = 0
        pass





    def draw(self):
        resource_manage.resouse.spri_wizard_boss.clip_composite_draw(624, 0, 624, 726, 0, 'h', self.x, self.y, 208, 242)





    def handle_event(self, event):
        pass

