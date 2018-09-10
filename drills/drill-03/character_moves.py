
from pico2d import *
import math


open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=0
y=90
th = 0
while(True):
    while(x < 800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x = x+2
    while(y<600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(800,y)
        y=y+2
    while(x >0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,600)
        x=x-2
    while(y>90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(0,y)
        y=y-2
    while(x<400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x = x+2
    while(th<30):
        clear_canvas_now()
        grass.draw_now(400,30)
        x = 400+200*math.sin(th)
        y = 300+200*math.cos(th)
        character.draw_now(x,y)
        th = th + (math.pi/36)
    x = 400
    y = 90
    th = 0


close_canvas()
