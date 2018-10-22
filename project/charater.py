from pico2d import *





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
        self.x -= (200 *0.01)
    def move_right(self):
        self.x += (200 *0.01)
    def move_up(self):
        self.y += (200 *0.01)
    def move_down(self):
        self.y -= (200 *0.01)

    def update(self):
        if(self.direction_sero == -1):
            if (play.y > 50):
                self.move_down()
        elif(self.direction_sero == 1):
            if (play.y < 974):
                self.move_up()


        if(self.direction_garo == -1):
            if (play.x > 50):
                self.move_left()
        elif(self.direction_garo == 1):
            if (play.x < 1230):
                self.move_right()


class Ballut:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = load_image('fight_plane.png')
        self.exist = False


    def draw(self):
        if(self.exist ==True):
            self.image.clip_draw(113, 120, 40, 20, self.x, self.y)

    def update(self):
        if(self.exist == True):
            self.x += (200 * 0.01)
            if(self.x > 1280):
                self.exist == False


open_canvas(1280,1024)
moving = True
play = player()


balluts = [Ballut() for i in range(2000)]
shoot_count = 0

def handle_events():
    global moving
    global shoot_count
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            moving = False
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
                moving = False
            elif event.key == SDLK_x:
                if shoot_count < 2000:
                    balluts[shoot_count].x = play.x
                    balluts[shoot_count].y = play.y
                    balluts[shoot_count].exist = True
                    shoot_count += 1
                else:
                    balluts[shoot_count % 2000].x = play.x
                    balluts[shoot_count % 2000].y = play.y
                    balluts[shoot_count % 2000].exist = True
                    shoot_count += 1



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


    for ball in balluts:
        ball.update()


    clear_canvas()
    play.draw()
    for ball in balluts:
        ball.draw()

    update_canvas()

    delay(0.01)