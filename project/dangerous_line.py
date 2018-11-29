from pico2d import *
import game_framework
import game_world
import resource_manage

class Line:
    line_image = None
    bgm = None
    def __init__(self,x =  144,num = 1):
        self.x, self.y, self.num = x, 800, num
        self.move = 0
        if Line.line_image == None:
            Line.line_image = load_image('resource_image\\danger.png')



    def draw(self):
        self.line_image.clip_draw(0,0,288,24,self.x + self.move,self.y,288,96)
        self.line_image.clip_draw(0, 0, 288, 24, self.x + self.move, self.y - 700, 288, 96)
        pass
    def update(self):
        self.move -= 0.5
        if(self.x + self.move <= -144):
            self.x = 1296
            self.move = 0
class cut_sence:
    boss_image = None
    def __init__(self):
        self.x, self.y, self.move = 980, 450, 0


    def draw(self):
        resource_manage.resouse.spri_wizard_boss.clip_composite_draw(0, 351, 592, 351, 0, 'h', self.x + self.move,
                                                                     self.y, 592, 351)

    def update(self):
        self.move -= 0.5
        if self.move <= -200:
            self.move = -200