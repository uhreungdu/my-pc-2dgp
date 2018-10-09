from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

class Ball:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.image2 = load_image('ball41x41.png')
        self.x, self.y = random.randint(100, 700), 600
        self.speed = random.randint(5, 20)
        self.size_choose = random.randint(1, 2)

    def draw(self):
        if (self.size_choose == 1):
            self.image.draw(self.x, self.y)
        else:
            self.image2.draw(self.x, self.y)

    def fall(self):
        self.y -= self.speed


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas(800,600)
grass = Grass()
running = True
team = [Boy() for i in range(11)]
balls = [Ball() for i in range(20)]

# game main loop code
while running:
    handle_events()
    for boy in team:
        boy.update()

    for ball in balls:
        if(ball.size_choose == 1):
            if (ball.y >= 65):
                ball.fall()
            else:
                ball.y = 60
        else:
            if(ball.y  >= 75):
                ball.fall()
            else:
                ball.y = 70

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()

    for ball in balls:
        ball.draw()

    update_canvas()
    delay(0.05)



# finalization code

close_canvas()
