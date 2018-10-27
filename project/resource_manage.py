from pico2d import *


resouse = None

def loading_resouce():
    global resouse
    resouse = Rm()



class Rm:
    spri_charater = None
    spri_bullut = None

    def __init__(self):
        Rm.spri_charater = load_image('fight_plane.png')
        Rm.spri_bullut = load_image('fight_plane.png')





