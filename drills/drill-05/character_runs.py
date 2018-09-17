from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')
past_spot = [[203, 535], [132, 243], [535, 470], [477, 203], [715, 136], [316, 225], [510, 92], [692, 518], [682, 336], [712,349]]





def move_to_spot(count):
    cx, cy= past_spot[count][0], past_spot[count][1]
    frame = 0

    while (cx != past_spot[count+1][0] & cy != past_spot[count + 1][1]):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, cx, cy)
        if (cx < past_spot[count + 1][0]):
            cx += 1
        if (cx > past_spot[count + 1][0]):
            cx -= 1
        if (cy < past_spot[count + 1][1]):
            cy += 1
        if (cy > past_spot[count + 1][1]):
            cy -= 1
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)


    count += 1


def move_first(x,y):
    cx, cy = x, y


while True:
    count = 0
    move_to_spot(count)
    move_to_spot(count)
    #move_to_spot(count)
    #move_to_spot(count)
    #move_to_spot(count)
    #move_to_spot(count)
    #move_to_spot(count)
    #move_to_spot(count)
    #move_to_spot(count)
    #move_to_spot(count)

    #move_first(203, 535)

close_canvas()
