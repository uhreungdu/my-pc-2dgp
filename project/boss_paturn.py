from pico2d import *
import game_framework
import game_world
import resource_manage
import math
import main_game
import boss_stage
import random

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 30
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8



class Boss_wave:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1, ID = 1, patruns = 0):
        self.ID = ID
        self.x, self.y, self.velocity = x, y, velocity
        self.angle = 0
        self.rad = 0
        self.base_x = x
        self.base_y = y

        self.cur_time = get_time()
        self.spread_time = get_time()

        self.circle_x = 0
        self.circle_y = 0
        self.damage = 0
        self.round = 0
        self.deltaX = 0
        self.deltaY = 0
        self.length = 0
        self.paturn = patruns
        self.type = 0
        self.check = True



    def draw(self):
        if self.y <= 850:
            resource_manage.resouse.spri_wizard_boss_attack_phase1.clip_draw(0, 0, 485, 483, self.x, self.y, 50,
                                                                             50)


        if self.type == 1:
            if self.ID == 1:
                up_type = Boss_wave(self.x, self.y, -RUN_SPEED_PPS, 2)
                game_world.add_object(up_type, 1)
                down_type = Boss_wave(self.x, self.y, -RUN_SPEED_PPS, 3)
                game_world.add_object(down_type, 1)
                self.type = 0
            if self.ID == 2:
                self.type = 0
            if self.ID == 3:
                up_type = Boss_wave(self.x, self.y, -RUN_SPEED_PPS, 2)
                game_world.add_object(up_type, 1)
                self.type = 0
        if self.paturn == 1:
            resource_manage.resouse.spri_wizard_boss_attack_phase1.clip_draw(0, 0, 485, 483, self.x, self.y - 100, 50,
                                                                             50)
            resource_manage.resouse.spri_wizard_boss_attack_phase1.clip_draw(0, 0, 485, 483, self.x, self.y + 100, 50,
                                                                             50)



        self.round = 50
        self.damage = 20
    def update(self):
        self.cur_time = get_time()
        #패턴 1
        if self.paturn == 0:
            if self.ID == 1:
                self.x -= RUN_SPEED_PPS * game_framework.frame_time * 0.75
            if self.ID == 2:
                self.x -= RUN_SPEED_PPS * game_framework.frame_time * 0.5
                self.y -= RUN_SPEED_PPS * game_framework.frame_time * 0.5

            if self.ID == 3:
                self.x -= RUN_SPEED_PPS * game_framework.frame_time * 0.5
                self.y += RUN_SPEED_PPS * game_framework.frame_time * 0.5

            if (self.cur_time - self.spread_time) >= 1:
                self.type = 1
                self.spread_time = get_time()


        #패턴 2
        if self.paturn == 1:
            if self.ID == 1:
                self.x -= RUN_SPEED_PPS * game_framework.frame_time * 0.5
                self.type = 2



        #충돌체크
        self.deltaX = self.x - main_game.play.x
        self.deltaY = self.y - main_game.play.y

        self.length = math.sqrt(self.deltaX * self.deltaX + self.deltaY * self.deltaY)

        if (self.length < self.round + main_game.play.round):
            game_world.remove_object(self)
            main_game.play.hp -= self.damage


        if self.x < 50 or self.x > 1280 - 50:
            game_world.remove_object(self)