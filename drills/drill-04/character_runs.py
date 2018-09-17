from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')





while(True):
    def move_left():
        frame, x = 0, 0
        while (x < 800 - 25):
            clear_canvas()
            grass.draw(400, 30)
            character.clip_draw(frame * 100, 100, 100, 100, x, 90)
            update_canvas()
            frame = (frame + 1) % 8
            x += 5
            delay(0.05)
            get_events()


    def move_right():
        frame, x = 0, 800 - 25
        while (x > 0 + 25):
            clear_canvas()
            grass.draw(400, 30)
            character.clip_draw(frame * 100, 0, 100, 100, x, 90)
            update_canvas()
            frame = (frame + 1) % 8
            x -= 5
            delay(0.05)
            get_events()
    move_left()

    move_right()

close_canvas()

