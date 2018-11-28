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
    spri_wizard_boss_attack_phase1 = None
    spri_wizard_boss_immotral_ring = None
    def __init__(self):
        Rm.spri_charater = load_image('resource_image\\fight_plane.png')
        Rm.spri_bullut = load_image('resource_image\\fight_plane.png')

        Rm.spri_Wheel_enemy = load_image('resource_image\\Wheel Enemy.png')
        Rm.spri_wheel_bullut = load_image('resource_image\\wheel_attack.png')

        Rm.spri_wizard_boss = load_image('resource_image\\wiard_boss_phase1.png')
        Rm.spri_wizard_boss_attack_phase1 = load_image('resource_image\\attack_circle.png')
        Rm.spri_wizard_boss_immotral_ring = load_image('resource_image\\immortal.png')






