from pico2d import *
import charater
import game_framework

name = "MainGame"

play = None
ballut = None
shoot_count = 0

def enter():
    global play, ballut, shoot_count
    play = charater.player()
    ballut = [charater.Ballut() for i in range(2000)]
    shoot_count = 0

def exit():
    global play, ballut
    del(play)
    del(ballut)

def pause():
    pass

def resume():
    pass

def handle_events():
    global shoot_count
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                play.direction_garo = 1
            elif event.key == SDLK_LEFT:
                play.direction_garo = -1
            elif event.key == SDLK_UP:
                play.direction_sero = 1
            elif event.key == SDLK_DOWN:
                play.direction_sero = -1
            elif event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_x:
                if shoot_count < 2000:
                    ballut[shoot_count].x = play.x
                    ballut[shoot_count].y = play.y
                    ballut[shoot_count].exist = True
                    shoot_count += 1
                else:
                    ballut[shoot_count % 2000].x = play.x
                    ballut[shoot_count % 2000].y = play.y
                    ballut[shoot_count % 2000].exist = True
                    shoot_count += 1



        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                if (play.x < 1230):
                    play.direction_garo = 0
            elif event.key == SDLK_LEFT:
                if (play.x > 50):
                    play.direction_garo = 0
            elif event.key == SDLK_UP:
                if (play.y < 974):
                    play.direction_sero = 0
            elif event.key == SDLK_DOWN:
                if (play.y > 50):
                    play.direction_sero = 0


def update():
    play.update()
    for ba in ballut:
        ba.update()


def draw():
    clear_canvas()
    play.draw()
    for ba in ballut:
        ba.draw()
    update_canvas()

