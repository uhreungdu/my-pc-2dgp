from pico2d import *




class player:
    def __init__(self):
        self.x, self.y = 100, 500
        self.character = load_image('fight_plane.png')
        self.direction = 1

    def draw(self):
        self.character.clip_draw(0,150,60,50,self.x,self.y)

    def move_left(self):
        self.x -= (10 *0.05)
    def move_right(self):
        self.x += (10 *0.05)
    def move_up(self):
        self.y += (10 *0.05)
    def move_down(self):
        self.y -= 10

open_canvas(1280,1024)
moving = True
play = player()
direction = True

def handle_events():
    global moving
    global direction
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            moving = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                if(play.x <1230):
                    play.move_right()
            elif event.key == SDLK_LEFT:
                if(play.x > 50):
                    play.move_left()
            elif event.key == SDLK_UP:
                if(play.y < 974):
                    play.move_up()
            elif event.key == SDLK_DOWN:
                if(play.y > 50):
                    play.move_down()
            elif event.key == SDLK_ESCAPE:
                moving = False


while moving:
    clear_canvas()


    play.draw()


    update_canvas()
    handle_events()
    delay(0.05)