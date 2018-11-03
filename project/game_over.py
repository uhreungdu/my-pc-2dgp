import game_framework
from pico2d import *
import title_state
import game_world

name = "Game_Over"
image = None
Game_over_image = None

def enter():
    global image
    global Game_over_image
    image = load_image('bg.png')
    Game_over_image = load_image('GAMEOVER Banner (doubleres).png')
    game_world.clear()


def exit():
    global image
    global Game_over_image

    del(Game_over_image)
    del(image)
    game_world.clear()

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







def update():
    pass


def pause():
    pass


def resume():
    pass
