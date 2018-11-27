from pico2d import *
import game_framework
import game_world
import main_game


class Stage:
    image = None
    image_reverse = None
    font = None
    gauge_font = None
    gauge_bar = None
    gauge_fill = None
    state_window = None
    bgm = None
    def __init__(self, num = 1):
        self.x, self.y, self.num = 1280 / 2, 1024 / 2, num
        self.move = 0
        self.like_scroll = 850
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
        if Stage.bgm == None:
            Stage.bgm = load_music('sound_resource\\[SDVX] Nostalgic Blood of the Strife [NOFX].mp3')
            Stage.bgm.set_volume(64)
            Stage.bgm.repeat_play()



    def draw(self):
        self.image.draw(self.x + self.like_scroll, self.y)
        self.state_window.clip_draw(0, 0, 400, 92, 1280/2, 940, 1280,175)
        self.font.draw(30, 970,'HP : %d' % main_game.play.hp,(255,0,0))
        self.font.draw(30, 920, 'Damge : %d' % main_game.play.power, (0, 0, 255))
        self.font.draw(500, 970, 'BossGauge', (255, 0, 255))
        if self.move <8:
            self.gauge_fill.clip_draw(0, 0, 57 * self.move, 26, 452 + (self.move * 38), 920, 72 * self.move + 10, 40)
        if self.move >= 8:
            self.gauge_fill.clip_draw(0, 0, 454, 26, 755, 920, 720, 40)
        self.gauge_bar.draw(750,920)

    def update(self):
       self.move = main_game.wave_count
       self.like_scroll -= 0.5