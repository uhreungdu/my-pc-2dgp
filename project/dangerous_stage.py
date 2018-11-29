from pico2d import *
from dangerous_line import Line
from dangerous_line import cut_sence
import game_framework
import game_world
import main_game
import boss_stage


name = "Dangerous_stage"

play = None
wheel_enemy = None
wheel_enemy2 = None
wheel_enemy3 = None
wave_count = 0
stage = None
wave_time = 0
wave_now_time = 0
wheel_enemys = []
dangerous_image = []
cut_image = None
def enter():
    global play
    global stage
    global wave_time
    global wave_now_time
    global dangerous_image
    global cut_image
    play = main_game.play
    stage = main_game.stage
    game_world.add_object(play, 1)
    game_world.add_object(stage, 0)
    dangerous_image = [Line(i * 288) for i in range(5)]
    cut_image = cut_sence()
    for line_image in dangerous_image:
        game_world.add_object(line_image,1)
    game_world.add_object(cut_image,0)
    play.attack_mode = False
    wave_time = get_time()
    wave_now_time = get_time()



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
    global wave_now_time
    global wave_time
    wave_now_time = get_time()
    if wave_now_time - wave_time >= 10:
        play.attack_mode = True
        game_framework.change_state(boss_stage)
    for game_object in game_world.all_objects():
        game_object.update()




def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()