from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')
past_spot = [[203, 535], [132, 243], [535, 470], [477, 203], [715, 136], [316, 225], [510, 92], [692, 518], [682, 336], [712,349]]

#과제 완성- 다시 커밋

def move_to_spot(count):
    cx, cy= past_spot[count][0], past_spot[count][1]
    frame = 0
    diration = 0
    if(count != 9):
        while (cx != past_spot[count + 1][0] or cy != past_spot[count + 1][1]):
            clear_canvas()
            grass.draw(400, 30)
            if (cx < past_spot[count + 1][0]):      #작을시 오른쪽으로
                cx += 1
                diration = 0
            if (cx > past_spot[count + 1][0]):      #cx값이 더 클시 왼쪽으로
                cx -= 1
                diration = 1
            if (cy < past_spot[count + 1][1]):      #cy값이 더 작을시 위로
                cy += 1
            if (cy > past_spot[count + 1][1]):      #cy값이 더 클시 아래로
                cy -= 1
            if (diration == 0):
                character.clip_draw(frame * 100, 100, 100, 100, cx, cy)
            if (diration == 1):
                character.clip_draw(frame * 100, 0, 100, 100, cx, cy)

            update_canvas()
            frame = (frame + 1) % 8
            delay(0.01)

def move_first(count):      # 마지막일시 처음점으로 돌아감
    cx, cy = past_spot[9][0], past_spot[9][1]
    frame = 0
    diration = 0
    while (cx != past_spot[count][0] or cy != past_spot[count][1]):
        clear_canvas()
        grass.draw(400, 30)
        if (cx < past_spot[count][0]):
            cx += 1
            diration = 0
        if (cx > past_spot[count][0]):
            cx -= 1
            diration = 1
        if (cy < past_spot[count][1]):
            cy += 1
        if (cy > past_spot[count][1]):
            cy -= 1
        if (diration == 0):
            character.clip_draw(frame * 100, 100, 100, 100, cx, cy)
        if (diration == 1):
            character.clip_draw(frame * 100, 0, 100, 100, cx, cy)

        update_canvas()
        frame = (frame + 1) % 8
        delay(0.01)



count = 0
while True:
    if (count < 9):
        move_to_spot(count)
        count = count + 1
    else:
        count = 0
        move_first(count)




close_canvas()

