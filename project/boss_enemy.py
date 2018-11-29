import game_framework
from pico2d import *

import game_world
import resource_manage
import random
#import main_game
from boss_paturn import Boss_wave

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
    hp_frame = None
    hp_gauge = None
    def __init__(self):
        if Wizard.image == None:
            Wizard.image = resource_manage.resouse.spri_wizard_boss
        if Wizard.hp_frame == None:
            Wizard.hp_frame = load_image('8frame (doubleres).png')
        if Wizard.hp_gauge == None:
            Wizard.hp_gauge = load_image('Danger (stretch).png')

        self.x, self.y = 1100, 500
        self.hp = 1000
        self.frame = 0
        self.cur_time = get_time()
        self.now_time = get_time()
        self.second_time = 0
        self.nexw_time = 0
        self.count = 0
        self.dir = 0
        self.paturn = 0
        self.round = 100
        self.immortal = True





    def update(self):
        self.now_time = get_time()
        if self.dir == 0:
            self.y += 0.1
            if self.y >= 510:
                self.dir = 1
        if self.dir == 1:
            self.y -= 0.1
            if self.y <= 490:
                self.dir = 0

        if (self.now_time - self.cur_time) >= 0 and (self.now_time - self.cur_time) <= 5:
            self.immortal = True
            if (self.now_time - self.second_time) >= 0.25:
                ball_up = Boss_wave(self.x, self.y + 100, -RUN_SPEED_PPS, 1, 1)
                game_world.add_object(ball_up, 1)
                ball_mid = Boss_wave(self.x, self.y, -RUN_SPEED_PPS, 1, 1)
                game_world.add_object(ball_mid, 1)
                ball_bottom = Boss_wave(self.x, self.y - 100, -RUN_SPEED_PPS, 1, 1)
                game_world.add_object(ball_bottom, 1)
                self.second_time = get_time()

        if (self.now_time - self.cur_time) >= 4 and (self.now_time - self.cur_time) <= 12:
            self.immortal = False

        if (self.now_time - self.cur_time) >= 10 and (self.now_time - self.cur_time) <= 15:
            self.immortal = True
            if (self.now_time - self.second_time) >= 2:
                ball = Boss_wave(self.x, self.y, -RUN_SPEED_PPS, 1,0)
                game_world.add_object(ball, 1)
                self.second_time = get_time()

        if (self.now_time - self.cur_time) >= 14 and (self.now_time - self.cur_time) <= 22:
            self.immortal = False


        if (self.now_time - self.cur_time) >= 20 and (self.now_time - self.cur_time) <= 25:
            self.immortal = True

    def draw_hp(self):
        self.hp_gauge.clip_draw(0, 0, 454, 26, 645 - int(720*((1000-self.hp)/2000)), 850,
                                720 * (self.hp/1000), 40)
        #print(self.hp)
        self.hp_frame.draw(1280/2, 850)
        pass

    def draw(self):
        resource_manage.resouse.spri_wizard_boss.clip_composite_draw(0, 0, 592, 702, 0, 'h', self.x, self.y, 208, 242)
        if self.immortal == True:
            resource_manage.resouse.spri_wizard_boss_immotral_ring.clip_draw(0,0, 654,639,self.x,self.y,240,272)
        self.draw_hp()




    def handle_event(self, event):
        pass

