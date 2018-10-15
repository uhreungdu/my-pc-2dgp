import game_framework
from pico2d import *
import title_state
import start_state

name = "PauseState"
image = None
logo_time = 0.0
pause = None

class Pause:
    def __init__(self):
        self.image = load_image('pause.png')

    def draw(self):
        self.image.clip_draw(0, 0, 900, 900, 400, 300)


def enter():
    global pause
    pause = Pause()



def exit():     #종료
    global image
    del(image)


def update():
    pass


def draw():
    global image
    clear_canvas()
    pause.draw()
    update_canvas()




def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.type == SDLK_p:
                game_framework.pop_state()



def pause(): pass


def resume(): pass
