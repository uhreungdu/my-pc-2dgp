from pico2d import *
import game_framework
import game_world
import resource_manage
import math
import main_game


class Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1, ID = 1):
        self.ID = ID
        if Bullet.image == None:
            if self.ID == 1:
                Bullet.image = resource_manage.resouse.spri_bullut
            if self.ID == 2:
                Bullet.image = resource_manage.resouse.spri_wheel_bullut


        self.x, self.y, self.velocity = x, y, velocity
        self.angle = 0
        self.rad = 0
        self.base_x = x
        self.base_y = y
        self.circle_x = 0
        self.circle_y = 0
        self.damage = 0
        self.round = 0
        self.deltaX = 0
        self.deltaY = 0
        self.length = 0



    def draw(self):
        if self.ID == 1:
            resource_manage.resouse.spri_bullut.clip_draw(113, 120, 40, 20, self.x, self.y)
        if self.ID == 2:
            resource_manage.resouse.spri_wheel_bullut.clip_composite_draw(0,20,30,30,0,'h',self.x,self.y,30,30)
            self.round = 15
            self.damage = 10

    def update(self):
        if self.ID == 1:
            self.x += self.velocity / 2
        if self.ID == 2:
            self.angle += 2
            self.rad = self.angle * math.pi / 180

            self.base_x += self.velocity / 2

            self.circle_x = 30 * math.cos(self.rad)
            self.circle_y = 30 * math.sin(self.rad)

            self.x = self.circle_x +self.base_x
            self.y = self.circle_y +self.base_y

            self.deltaX = self.x-main_game.play.x
            self.deltaY = self.y-main_game.play.y

            self.length = math.sqrt(self.deltaX * self.deltaX + self.deltaY * self.deltaY)

            if( self.length < self.round + main_game.play.round):
                game_world.remove_object(self)
                main_game.play.hp -= self.damage




        if self.x < 50 or self.x > 1280 - 50:
            game_world.remove_object(self)
