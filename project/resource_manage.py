from pico2d import *


resouse = None

def loading_resouce():
    global resouse
    resouse = Rm()



class Rm:
    spri_charater = None
    spri_bullut = None
    spri_Wheel_enemy = None
    spri_wheel_bullut = None
    spri_wizard_boss = None

    def __init__(self):
        Rm.spri_charater = load_image('resource_image\\fight_plane.png')
        Rm.spri_bullut = load_image('resource_image\\fight_plane.png')
        Rm.spri_Wheel_enemy = load_image('resource_image\\Wheel Enemy.png')
        Rm.spri_wheel_bullut = load_image('resource_image\\Wheel Enemy.png')
        Rm.spri_wizard_boss = load_image('resource_image\\wizard_boss.png')






