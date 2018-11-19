from pico2d import *
import game_framework
import game_world
import main_game


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
                Stage.image = load_image('resource_image\\main_stage_back_ground.jpg')\

        if Stage.state_window == None:
            Stage.state_window = load_image('resource_image\\Info.png')
        if Stage.font == None:
            if self.num == 1:
                Stage.font = load_font('netmarbleB.ttf', 45)
        if Stage.gauge_bar == None:
            Stage.gauge_bar = load_image('8frame (doubleres).png')
        if Stage.gauge_fill == None:
            Stage.gauge_fill = load_image('Danger (stretch).png')
        if Stage.gauge_font == None:
            Stage.gauge_font = load_font('netmarbleB.ttf', 45)



    def draw(self):
        self.image.draw(self.x, self.y)
        self.state_window.clip_draw(0, 0, 400, 92, 1280/2, 940, 1280,175)
        self.font.draw(25, 970,'HP : %d' % main_game.play.hp,(255,255,255))
        self.font.draw(25, 920, 'Damge : %d' % main_game.play.power, (255, 255, 255))
        self.font.draw(750, 920, 'Gauge : %d' % main_game.wave_count, (255, 255, 255))
        self.gauge_bar.draw(750,920)
        #self.gauge_bar.clip_draw(0,0,50,26)
    def update(self):
       pass