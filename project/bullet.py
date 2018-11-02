from pico2d import *
import game_framework
import game_world
import resource_manage
import math


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


    def draw(self):
        if self.ID == 1:
            resource_manage.resouse.spri_bullut.clip_draw(113, 120, 40, 20, self.x, self.y)
        if self.ID == 2:
            resource_manage.resouse.spri_wheel_bullut.clip_composite_draw(0,20,50,50,0,'h',self.x,self.y,50,50)

    def update(self):
        if self.ID == 1:
            self.x += self.velocity / 2
        if self.ID == 2:
            self.angle += 0.5
            self.rad = self.angle * math.pi / 180

            self.x += self.velocity / 2 * math.cos(self.rad)
            #self.y += (self.velocity / 2) * math.sin(self.rad)

            self.x += self.velocity / 2

        if self.x < 50 or self.x > 1280 - 50:
            game_world.remove_object(self)
