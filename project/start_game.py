import game_framework
import pico2d
import resource_manage
import main_game


pico2d.open_canvas(1280,1024,sync = True)
resource_manage.loading_resouce()
game_framework.run(main_game)
pico2d.close_canvas()