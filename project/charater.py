from pico2d import *
import game_framework
import resource_manage

name = "charater"
play = None
moving = True
image = None
shoot_count = 0

class player:


    def __init__(self):
        self.x, self.y = 100, 500
        self.character = resource_manage.resouse.spri_charater
        self.direction = 1
        self.direction_sero = 0
        self.direction_garo = 0
        self.hp = 100

    def draw(self):
        resource_manage.resouse.spri_charater.clip_draw(0,150,60,50,self.x,self.y)

    def move_left(self):
        self.x -= (100 *0.01)
    def move_right(self):
        self.x += (100 *0.01)
    def move_up(self):
        self.y += (100 *0.01)
    def move_down(self):
        self.y -= (100 *0.01)

    def update(self):
        if(self.direction_sero == -1):
            if (self.y > 50):
                self.move_down()
        elif(self.direction_sero == 1):
            if (self.y < 974):
                self.move_up()


        if(self.direction_garo == -1):
            if (self.x > 50):
                self.move_left()
        elif(self.direction_garo == 1):
            if (self.x < 1230):
                self.move_right()


class Ballut:
    image = None
    def __init__(self):
        self.x = 0
        self.y = 0
        self.exist = False
        if(Ballut.image == None):
            Ballut.image = resource_manage.resouse.spri_bullut


    def draw(self):
        if(self.exist ==True):
            resource_manage.resouse.spri_bullut.clip_draw(113, 120, 40, 20, self.x, self.y)

    def update(self):
        if(self.exist == True):
            self.x += (200 * 0.01)
            if(self.x > 1280):
                self.exist = False





balluts = None
shoot_count = 0

def handle_events():
    pass
