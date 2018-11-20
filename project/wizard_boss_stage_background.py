from pico2d import *
import game_framework
import game_world
import main_game
import boss_enemy


class Stage:
    image = None
    font = None
    gauge_font = None
    gauge_bar = None
    gauge_fill = None
    state_window = None
    def __init__(self, num = 1):
        self.x, self.y, self.num = 1280 / 2, 1024 / 2, num
        if Stage.image == None:
            if self.num == 1:
                Stage.image = load_image('resource_image\\wizard_background.png')\

        if Stage.state_window == None:
            Stage.state_window = load_image('resource_image\\Info.png')
        if Stage.font == None:
            if self.num == 1:
                Stage.font = load_font('netmarbleB.ttf', 45)



    def draw(self):
        self.image.clip_draw(0,653,639,428,self.x,self.y,1280,1024)
        self.state_window.clip_draw(0, 0, 400, 92, 1280/2, 940, 1280,175)
        self.font.draw(25, 970,'HP : %d' % main_game.play.hp,(255,255,255))
    def update(self):
       pass