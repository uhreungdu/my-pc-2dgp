import game_framework
from pico2d import *
import title_state
import game_world

name = "Clear_Game"
image = None
Game_over_image = None
over_sound = None


def enter():
    global image
    global Game_over_image
    global over_sound
    image = load_image('gameover_back_ground.png')
    Game_over_image = load_image('resource_image\\Info_Clear.png')
    over_sound = load_wav('sound_resource\\game_over.wav')
    over_sound.set_volume(30)
    sound_over()

def exit():
    global image
    global Game_over_image

    del(Game_over_image)
    del(image)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
               game_framework.change_state(title_state)


def draw():
    clear_canvas()
    image.draw(1280 / 2, 1024 / 2)
    Game_over_image.draw(1280 / 2, 1024 / 2)
    update_canvas()




def sound_over():
    over_sound.play()


def update():
    pass


def pause():
    pass


def resume():
    pass
