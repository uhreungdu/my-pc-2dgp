import game_framework
from pico2d import *
import main_game

name = "TitleState"
image = None
title_font = None
title_frame = None
start_button = None

def enter():
    global image
    global title_font
    global title_frame
    global start_button
    image = load_image('title_state.png')
    title_font = load_font('Gilbert Bold-Preview_1004.otf', 200)
    title_frame = load_image('Info.png')
    start_button = load_image('Start.png')


def exit():
    global image
    global title_font
    global title_frame
    global start_button
    del(title_font)
    del(image)
    del(title_frame)
    del(start_button)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.push_state(main_game)


def draw():
    clear_canvas()
    image.draw(1280 / 2, 1024 / 2)
    title_font.draw(250, 650, 'Never Die',(255,255,255))
    start_button.draw(1280/2, 300)
    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass