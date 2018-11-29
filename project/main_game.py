from pico2d import *
from charater import player
from enemy import Wheel
from Stage_background import Stage
import game_framework
import game_world
import random
import game_over
#import boss_stage
import dangerous_stage

name = "MainGame"

play = None
wheel_enemy = None
wheel_enemy2 = None
wheel_enemy3 = None
wave_count = 0
stage = None
wave_time = 0
wave_now_time = 0
wheel_enemys = []
def enter():
    global play
    global wheel_enemy
    global wheel_enemy2
    global wheel_enemy3
    global stage
    global wave_time
    global wave_now_time
    global wheel_enemys
    play = player()
    wheel_enemys = [Wheel((i * 75) + 100) for i in range(10)]
    stage = Stage()
    game_world.add_object(play, 1)
    for wheel in wheel_enemys:
        game_world.add_object(wheel,1)
    game_world.add_object(stage, 0)
    play.attack_mode = False
    wave_time = get_time()
    wave_now_time = get_time()



def exit():
    global wave_count
    Stage.bgm.stop()
    game_world.clear()
    wave_count = 0

def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_state()
        else:
            play.handle_event(event)


def update():
    global wave_count
    global wave_now_time
    global wave_time
    global play
    for game_object in game_world.all_objects():
        game_object.update()
    if play.hp <= 0:
        game_world.remove_object(play)
        game_framework.change_state(game_over)
    wave_now_time = get_time()

    if(wave_now_time - wave_time) >= 9 and play.hp > 0:
        wave_count += 10
        wave_time = get_time()

    if wave_count >= 9:
        play.attack_mode = True
        game_framework.change_state(dangerous_stage)




def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()

