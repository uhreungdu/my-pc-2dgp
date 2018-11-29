import game_framework
import pico2d
import resource_manage
import main_game
import title_state

pico2d.open_canvas(1280,1024)
pico2d.hide_lattice()
resource_manage.loading_resouce()
game_framework.run(title_state)
pico2d.close_canvas()