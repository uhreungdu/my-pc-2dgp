import turtle
import random
from pico2d import *


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


def prepare_move_canvas():
    pass


def draw_big_point(p):
    pass

def draw_character(p):
    pass


def draw_line(p1, p2):
    draw_big_point(p1)
    draw_big_point(p2)

    for i in range(0,100+1,2):
        t = i/100
        x = (1-t) * p1[0] + t*p2[0]
        y = (1-t) * p1[1] + t*p2[1]
        draw_character((x,y))
    draw_character(p2)








count = 0
while True:





close_canvas()




turtle.done()