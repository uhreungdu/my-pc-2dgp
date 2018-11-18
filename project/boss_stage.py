from pico2d import *
import game_framework
from charater import player
from boss_enemy import Wizard
import game_world
import game_over
import main_game


play = None
wizard_boss = None



def enter():
    global play
    global wizard_boss
    play = player()
    wizard_boss = Wizard()
    game_world.add_object(play, 1)
    game_world.add_object(wizard_boss,1)

def exit():
    global wave_count
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




def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()