from pico2d import *
import game_framework
import resource_manage
from bullet import Bullet
import game_world


name = "charater"
play = None
moving = True
image = None

PIXEL_PER_METER = (1.0 / 0.3)
RUN_SPEED_KMPH = 2
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8



RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, FIRE, UP_UP, UP_DOWN, DOWN_UP, DOWN_DOWN = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYDOWN, SDLK_x): FIRE
}
class PlayState:
    @staticmethod
    def enter(play, event):
        if event == RIGHT_DOWN:
            play.velocity_x += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            play.velocity_x -= RUN_SPEED_PPS
        elif event == UP_DOWN:
            play.velocity_y += RUN_SPEED_PPS
        elif event == DOWN_DOWN:
            play.velocity_y -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            play.velocity_x -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            play.velocity_x += RUN_SPEED_PPS
        elif event == UP_UP:
            play.velocity_y -= RUN_SPEED_PPS
        elif event == DOWN_UP:
            play.velocity_y += RUN_SPEED_PPS
        play.direction = clamp(-0.5, play.velocity_x, 0.5)
        play.direction = clamp(-0.5, play.velocity_y, 0.5)

    @staticmethod
    def exit(play, event):
        if event == FIRE:
            play.fire_shoting()



    @staticmethod
    def do(play):
        play.x += play.velocity_x
        play.x = clamp(50, play.x, 1280 - 50)
        play.y += play.velocity_y
        play.y = clamp(50, play.y, 1024 - 200)


    @staticmethod
    def draw(play):
        play.character.clip_draw(0, 150, 60, 50, play.x, play.y)
        play.character.opacify(play.opacity)


next_state_table = {
    PlayState:{RIGHT_UP: PlayState, LEFT_UP: PlayState, RIGHT_DOWN: PlayState, LEFT_DOWN: PlayState,
                FIRE: PlayState, UP_UP: PlayState, UP_DOWN: PlayState, DOWN_DOWN:PlayState, DOWN_UP: PlayState}
}

class player:


    def __init__(self):
        self.x, self.y = 100, 500
        self.character = resource_manage.resouse.spri_charater
        self.hp = 200
        self.direction = 1
        self.velocity_x = 0
        self.velocity_y = 0
        self.frame = 0
        self.round = 0
        self.opacity = 1
        self.power = 10
        self.event_que = []
        self.cur_state = PlayState
        self.cur_state.enter(self, None)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def fire_shoting(self):
        ball = Bullet(self.x, self.y, 10, 1,0)
        game_world.add_object(ball,1)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
    def draw(self):
        self.cur_state.draw(self)
        self.round = 5
        #print(self.hp)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)



