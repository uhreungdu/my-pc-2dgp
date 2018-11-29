from pico2d import *
import game_framework
import game_world
import main_game
import boss_stage


class Stage:
    image = None
    font = None
    gauge_font = None
    gauge_bar = None
    gauge_fill = None
    state_window = None
    bgm = None
    def __init__(self, num = 1):
        self.x, self.y, self.num = 1280 / 2, 1024 / 2, num
        self.opa = 1
        self.op_bool = True
        if Stage.image == None:
            if self.num == 1:
                Stage.image = load_image('resource_image\\wizard_background.png')

        if Stage.state_window == None:
            Stage.state_window = load_image('resource_image\\Info.png')
        if Stage.font == None:
            if self.num == 1:
                Stage.font = load_font('netmarbleB.ttf', 45)
        if Stage.gauge_bar == None:
            Stage.gauge_bar = load_image('8frame (doubleres).png')
        if Stage.gauge_fill == None:
            Stage.gauge_fill = load_image('Danger (stretch).png')
        if Stage.bgm == None:
            Stage.bgm = load_music('sound_resource\\dj TAKA - Shooting Fireball.mp3')
            Stage.bgm.set_volume(50)
            Stage.bgm.repeat_play()


    def draw(self):
        self.image.clip_draw(0,653,639,428,self.x,self.y,1280,1024)
        self.image.opacify(self.opa)
        self.state_window.clip_draw(0, 0, 400, 92, 1280/2, 960, 1280,85)
        self.font.draw(25, 970,'HP : %d' % main_game.play.hp,(255, 0, 0))
        self.font.draw(1000, 970, 'Damge : %d' % main_game.play.power, (0, 0, 255))
    def update(self):
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
