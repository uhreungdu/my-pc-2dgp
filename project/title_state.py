import game_framework
from pico2d import *
import main_game

name = "TitleState"
image = None
title_font = None
title_frame = None
start_button = None
effect_left = None
effect_right = None
effect_frame = 0
bgm = None

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

def enter():
    global image
    global title_font
    global title_frame
    global start_button
    global effect_left
    global effect_right
    global effect_frame
    global bgm
    image = load_image('resource_image\\title_state.png')
    title_font = load_font('Gilbert Bold-Preview_1004.otf', 200)
    title_frame = load_image('resource_image\\Info.png')
    start_button = load_image('resource_image\\Start.png')
    effect_left = load_image('resource_image\\effect.png')
    effect_right = load_image('resource_image\\effect_r.png')
    bgm = load_music('sound_resource\\back_ground.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()
    effect_frame = 0

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
    effect_left.clip_draw(int(effect_frame) * 200, 0, 200, 448, 250, 0, 500, 896)
    effect_right.clip_draw(int(effect_frame) * 200, 0, 200, 448, 1050, 0, 500, 896)
    title_font.draw(250, 650, 'Never Die',(255,255,255))

    start_button.draw(1280/2, 300)
    update_canvas()







def update():
    global effect_frame
    effect_frame = (effect_frame +  FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8


def pause():
    pass


def resume():
    pass