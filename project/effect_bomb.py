from pico2d import *
import game_framework
import game_world

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class effect:
    image = None
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.frame = 0
        if effect.image == None:
            effect.image = load_image('resource_image\\fight_plane.png')
        self.collide_sound = load_wav('sound_resource\\collide.wav')
        self.collide_sound.set_volume(50)
        self.collide_sound.play(1)

    def draw(self):
        self.image.clip_draw(int(self.frame) * 60,0,60,72,self.x,self.y)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        if int(self.frame) >= 3:
            game_world.remove_object(self)