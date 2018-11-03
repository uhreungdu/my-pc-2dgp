from pico2d import *
import game_framework
import game_world

class Stage:
    image = None

    def __init__(self, num = 1):
        self.x, self.y, self.num = 1280 / 2, 1024 / 2, num
        if Stage.image == None:
            if self.num == 1:
                Stage.image = load_image('stage1.png')


    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
       pass