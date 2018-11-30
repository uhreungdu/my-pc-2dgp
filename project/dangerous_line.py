from pico2d import *
import game_framework
import game_world
import resource_manage

class Line:
    line_image = None
    image_stage = None
    bgm = None
    def __init__(self,x =  144,num = 1):
        self.x, self.y, self.num = x, 800, num
        self.move = 0
        if Line.line_image == None:
            Line.line_image = load_image('resource_image\\danger.png')
        if Line.image_stage == None:
            Line.image_stage = load_image('resource_image\\Stage Final (doubleres).png')



    def draw(self):
        self.line_image.clip_draw(0,0,288,24,self.x + self.move,self.y,288,96)
        self.line_image.clip_draw(0, 0, 288, 24, self.x + self.move, self.y - 700, 288, 96)
        self.image_stage.clip_draw(0,0,1180,240,1280/2,700,590,120)
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
        self.opa = 1
        self.op_bool = True


    def draw(self):
        resource_manage.resouse.spri_wizard_boss.clip_composite_draw(0, 351, 592, 351, 0, 'h', self.x + self.move,
                                                                     self.y, 592, 351)
        resource_manage.resouse.spri_wizard_boss.opacify(self.opa)
    def update(self):
        self.move -= 0.5
        if self.move <= -150:
            self.move = -150
        if self.op_bool == True:
            self.opa -= 0.001
            if self.opa <= 0.5:
                self.opa = 0.5
                self.op_bool = False
        if self.op_bool == False:
            self.opa += 0.001
            if self.opa >= 1:
                self.opa = 1
                self.op_bool = True