from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')
past_spot = [10]



def save_spot(x,y,count):
    sx, sy = x , y
    past_spot[count] = sx + sy

def move_to_spot(x, y, count):
    cx, cy, cl= x, y, 0
    frame = 0
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame * 100, 100, 100, 100, cx, cy)
    update_canvas()
    delay(0.05)
    save_spot(cx,cy,count)
    count += 1


def move_first(x,y):
    cx, cy = x, y


while True:
    count = 0
    move_to_spot(203, 535,count)
    move_to_spot(132,243,count)
    move_to_spot(535,470,count)
    move_to_spot(477, 203,count)
    move_to_spot(715, 136,count)
    move_to_spot(316,225,count)
    move_to_spot(510, 92,count)
    move_to_spot(692, 518,count)
    move_to_spot(682, 336,count)
    move_to_spot(712,349,count)

    move_first(203, 535)

close_canvas()

