from pico2d import *


class ballut:
    pass

class player:
    def __init__(self):
        self.x, self.y = 100, 500
        self.character = load_image('fight_plane.png')
        self.direction = 1
        self.direction_sero = 0
        self.direction_garo = 0

    def draw(self):
        self.character.clip_draw(0,150,60,50,self.x,self.y)

    def move_left(self):
        self.x -= (100 *0.05)
    def move_right(self):
        self.x += (100 *0.05)
    def move_up(self):
        self.y += (100 *0.05)
    def move_down(self):
        self.y -= (100 *0.05)

    def update(self):
        if(self.direction_sero == -1):
            self.move_down()
        elif(self.direction_sero == 1):
            self.move_up()


        if(self.direction_garo == -1):
            self.move_left()
        elif(self.direction_garo == 1):
            self.move_right()




open_canvas(1280,1024)
moving = True
play = player()





def handle_events():
    global moving
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            moving = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                if(play.x <1230):
                    play.direction_garo = 1
            elif event.key == SDLK_LEFT:
                if(play.x > 50):
                    play.direction_garo = -1
            elif event.key == SDLK_UP:
                if(play.y < 974):
                    play.direction_sero = 1
            elif event.key == SDLK_DOWN:
                if(play.y > 50):
                    play.direction_sero = -1
            elif event.key == SDLK_ESCAPE:
                moving = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                if(play.x <1230):
                    play.direction_garo = 0
            elif event.key == SDLK_LEFT:
                if(play.x > 50):
                    play.direction_garo = 0
            elif event.key == SDLK_UP:
                if(play.y < 974):
                    play.direction_sero = 0
            elif event.key == SDLK_DOWN:
                if(play.y > 50):
                    play.direction_sero = 0



while moving:
    handle_events()
    play.update()
    clear_canvas()
    play.draw()


    update_canvas()

    delay(0.05)