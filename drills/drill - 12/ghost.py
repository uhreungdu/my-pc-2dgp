from pico2d import *
import game_framework
import game_world
import random

class Ghost:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1, frame = 1):
        if Ghost.image == None:
            Ghost.image = load_image('animation_sheet.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.frame = frame
        self.alpha = (random.randint(1, 10) / 10)

    def draw(self):
        if self.velocity == 1:
            self.image.clip_draw(int(self.frame) * 100, 300, 100, 100, self.x, self.y)
            self.image.opacify(0.5)

        else:
            self.image.clip_draw(int(self.frame) * 100, 200, 100, 100, self.x, self.y)

    def update(self):
        if(self.y < 250):
            self.y += 5

