from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024









def handle_events():
    global running
    global x, y
    global sv_x, sv_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            sv_x, sv_y = event.x, KPU_HEIGHT - 1 - event.y



open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image("hand_arrow.png")


running = True
past_x, past_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
ch_x, ch_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
sv_x, sv_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()
dirat = 0


while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    mouse.clip_draw(0, 0, 100, 100, x+40, y-45)
    if (dirat == 0):
        character.clip_draw(frame * 100, 100, 100, 100, ch_x, ch_y)
    if (dirat == 1):
        character.clip_draw(frame * 100, 0, 100, 100, ch_x, ch_y)

    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    if (ch_x < sv_x):
        ch_x += 1
        dirat = 0
    if (ch_x > sv_x):
        ch_x -= 1
        dirat = 1
    if (ch_y < sv_y):
        ch_y += 1
    if (ch_y > sv_y):
        ch_y -= 1
    if (ch_x == sv_y and ch_y == ch_x):
        dirat = 2
    delay(0.02)


close_canvas()




