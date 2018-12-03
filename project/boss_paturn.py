from pico2d import *
import game_framework
import game_world
import resource_manage
import math
import main_game
import boss_stage
import random
from effect_bomb import effect
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

count = 0

class Boss_wave:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1, ID = 1, patruns = 0, exist = 0):
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
        self.exist = exist
        self.thread = True
        self.count = 0


    def draw(self):
        global  count
        if self.paturn == 0 or self.paturn == 1:
            if self.y <= 850:
                if self.exist == 0:
                    resource_manage.resouse.spri_wizard_boss_attack_phase1.clip_draw(0, 0, 485, 483, self.x, self.y, 50,
                                                                                     50)
                if self.exist == 1:
                    resource_manage.resouse.spri_wizard_boss_attack_fake.clip_draw(0, 0, 502, 502, self.x, self.y, 100,
                                                                                   100)

            if self.paturn == 0:
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

        if self.paturn == 2:
            resource_manage.resouse.spri_wizard_boss_last_paturn.clip_draw(0, 0, 1122, 1119, self.x, self.y, 200,
                                                                           200)
            if self.x <= 1280/2 and self.thread == True:
                up = Boss_wave(self.x,self.y,-RUN_SPEED_PPS,0,3,0)
                game_world.add_object(up, 1)
                up_left = Boss_wave(self.x, self.y, -RUN_SPEED_PPS, 1, 3, 0)
                game_world.add_object(up_left, 1)
                left = Boss_wave(self.x, self.y, -RUN_SPEED_PPS, 2, 3, 0)
                game_world.add_object(left, 1)
                down_left = Boss_wave(self.x, self.y, -RUN_SPEED_PPS, 3, 3, 0)
                game_world.add_object(down_left, 1)
                down = Boss_wave(self.x, self.y, -RUN_SPEED_PPS, 4, 3, 0)
                game_world.add_object(down, 1)
                down_right = Boss_wave(self.x, self.y, -RUN_SPEED_PPS, 5, 3, 0)
                game_world.add_object(down_right, 1)
                right = Boss_wave(self.x, self.y, -RUN_SPEED_PPS, 6, 3, 0)
                game_world.add_object(right, 1)
                up_right = Boss_wave(self.x, self.y, -RUN_SPEED_PPS, 7, 3, 0)
                game_world.add_object(up_right, 1)
                self.thread = False
        if self.paturn == 3:
            if self.y <= 850:
                resource_manage.resouse.spri_wizard_boss_attack_fake.clip_draw(0, 0, 502, 502, self.x, self.y, 100,
                                                                               100)

        self.round = 25
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

        #마지막 패턴 3
        if self.paturn == 2:
            if self.x >= 1280 / 2:
                self.type = 1
                self.exist = 1
                self.x -= RUN_SPEED_PPS * game_framework.frame_time * 0.5
            if self.x <= 1280 /  2 and (self.cur_time - self.spread_time) >= 0.5:
                self.thread = True
                self.count += 1
                self.spread_time = get_time()
            if self.count >= 20:
                game_world.remove_object(self)

        if self.paturn == 3:
            if self.ID == 0:
                self.y += RUN_SPEED_PPS * game_framework.frame_time * 0.5
            if self.ID == 1:
                self.y += RUN_SPEED_PPS * game_framework.frame_time * 0.5
                self.x -= RUN_SPEED_PPS * game_framework.frame_time * 0.5
            if self.ID == 2:
                self.x -= RUN_SPEED_PPS * game_framework.frame_time * 0.5
            if self.ID == 3:
                self.y -= RUN_SPEED_PPS * game_framework.frame_time * 0.5
                self.x -= RUN_SPEED_PPS * game_framework.frame_time * 0.5
            if self.ID == 4:
                self.y -= RUN_SPEED_PPS * game_framework.frame_time * 0.5
            if self.ID == 5:
                self.y -= RUN_SPEED_PPS * game_framework.frame_time * 0.5
                self.x += RUN_SPEED_PPS * game_framework.frame_time * 0.5
            if self.ID == 6:
                self.x += RUN_SPEED_PPS * game_framework.frame_time * 0.5
            if self.ID == 7:
                self.y += RUN_SPEED_PPS * game_framework.frame_time * 0.5
                self.x += RUN_SPEED_PPS * game_framework.frame_time * 0.5

        #충돌체크
        if(self.exist == 0):
            self.deltaX = self.x - main_game.play.x
            self.deltaY = self.y - main_game.play.y

            self.length = math.sqrt(self.deltaX * self.deltaX + self.deltaY * self.deltaY)

            if (self.length < self.round + main_game.play.round):
                # print('cr')
                bomb_effect = effect(self.x, self.y)
                game_world.add_object(bomb_effect, 1)
                game_world.remove_object(self)
                main_game.play.hp -= self.damage


        if self.x < 50 or self.x > 1280 - 50:
            game_world.remove_object(self)