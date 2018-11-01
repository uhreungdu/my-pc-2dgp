from pico2d import *
import game_framework
import game_world
import resource_manage

class Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Bullet.image == None:
            Bullet.image = resource_manage.resouse.spri_bullut
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        resource_manage.resouse.spri_bullut.clip_draw(113, 120, 40, 20, self.x, self.y)

    def update(self):
        self.x += self.velocity

        if self.x < 50 or self.x > 1280 - 50:
            game_world.remove_object(self)
