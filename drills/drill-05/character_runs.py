from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')
past_spot = []

def save_spot(x,y):
    sx, sy = x , y

def move_to_spot(x, y):
    cx, cy, cl= x, y, 0
    frame = 0
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame * 100, 100, 100, 100, cx, cy)
    update_canvas()
    delay(0.05)
    save_spot(cx,cy)


def move_first(x,y):
    cx, cy = x, y


while True:
    move_to_spot(203, 535)
    move_to_spot(132,243)
    move_to_spot(535,470)
    move_to_spot(477, 203)
    move_to_spot(715, 136)
    move_to_spot(316,225)
    move_to_spot(510, 92)
    move_to_spot(692, 518)
    move_to_spot(682, 336)
    move_to_spot(712,349)

    move_first(203, 535)

close_canvas()

