import game_framework
from pico2d import *
import main_game

name = "How_to_play"
image = None
font = None
title_font = None
explan_font = None
title_frame = None
start_button = None
effect_left = None
effect_right = None
effect_frame = 0
bgm = None
start_gam = None

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

def enter():
    global image
    global title_font
    global explan_font
    image = load_image('resource_image\\help.png')
    title_font = load_font('netmarbleB.ttf', 70)
    explan_font = load_font('netmarbleB.ttf', 45)

def exit():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_game)


def draw():
    global title_font
    global explan_font
    clear_canvas()
    image.draw(1280/2,1024/2)
    title_font.draw(400, 950, '<how to play>',(255,0,0))
    explan_font.draw(50, 850,'조작법',(0,0,0))
    explan_font.draw(100, 800, '이동 : 방향키 ', (0, 0, 0))
    explan_font.draw(100, 750, '캐릭터는  8방향으로 움직일 수 있다.', (0, 0, 0))
    explan_font.draw(100, 700, '공격 : x ', (0, 0, 0))
    explan_font.draw(100, 650, '캐릭터는  보스전에서만 공격할 수 있다', (0, 0, 0))
    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass