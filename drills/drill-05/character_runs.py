from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')




def move_to_spot(x, y):
    cx, cy= x, y
    frame = 0
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame * 100, 100, 100, 100, cx, cy)
    update_canvas()

def move_first():
    pass


while True:
    move_to_spot(203, 535)
    move_first()

close_canvas()

