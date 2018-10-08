import turtle
import random
from pico2d import *
KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

frame = 0
size = 20
points = [(random.randint(0, KPU_WIDTH), random.randint(0, 1024)) for
        i in range(size)]
n = 1

direction = 0
def draw_character(p):
    global direction

    if (direction == 0):
        character.clip_draw(frame * 100, 100, 100, 100, p[0], p[1])
    if (direction == 1):
        character.clip_draw(frame * 100, 0, 100, 100, p[0], p[1])









temp = 0
def draw_line(p1, p2):
    global direction
    global temp
    global n
    temp += 2

    i = temp

    t = i/100
    x = (1-t) * p1[0] + t*p2[0]
    y = (1-t) * p1[1] + t*p2[1]
    if (p1[0] < p2[0]):
        direction = 0
    if (p1[0] > p2[0]):
        direction = 1
    draw_character((x,y))
    if (temp > 100):
        temp = 0
        n = (n + 1) % size


while True:
    print(n)
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    draw_line(points[n-1], points[n])

    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)









close_canvas()




turtle.done()