from pico2d import *
import game_framework
#from charater import player
from boss_enemy import Wizard
import game_world
import game_over
import main_game

import clear_game
from wizard_boss_stage_background import Stage

play = None
wizard_boss = None
stage = None

def enter():
    global play
    global wizard_boss
    global stage
    global bgm
    play = main_game.play
    wizard_boss = Wizard()
    stage = Stage()
    game_world.add_object(play, 1)
    game_world.add_object(wizard_boss,1)
    game_world.add_object(stage,0)
    stage.bgm.repeat_play()

def exit():
    global wave_count
    global stage
    stage.bgm.stop()
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
    for game_object in game_world.all_objects():
        game_object.update()
    if play.hp <= 0:
        game_world.remove_object(play)
        game_framework.change_state(game_over)
    if wizard_boss.hp <= 0:
        game_framework.change_state(clear_game)




def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()