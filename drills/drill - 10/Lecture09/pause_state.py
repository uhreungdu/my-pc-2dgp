import game_framework
from pico2d import *
import title_state
import start_state
import main_state

name = "PauseState"
image = None
logo_time = 0.0
pause = None
boy = None
grass = None

class Pause:
    def __init__(self):
        self.image = load_image('round-pause-button.png')

    def draw(self):
        self.image.clip_draw(0, 0, 64, 64, 400, 300)
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.dir = 0

    def update(self):
        self.frame = (self.frame + 1) % 8
        if (self.dir == -1):
            self.move_left()

        elif (self.dir == 1):
            self.move_right()

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def move_left(self):
        if(self.x > 0):
            self.x += -1
    def move_right(self):
        if(self.x < 800):
            self.x += 1



def enter():
    global pause
    pause = Pause()
    global boy
    boy = main_state.boy
    global grass
    grass = main_state.grass




def exit():     #종료
    global pause
    del(pause)
    global boy
    del(boy)
    global grass
    del(grass)

def update():
    pass

def draw():
    global image
    clear_canvas()
    pause.draw()
    boy.draw()
    grass.draw()
    update_canvas()




def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_p:
                game_framework.pop_state()



def pause(): pass


def resume(): pass
