import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.width, ai_settings.height))
    pygame.display.set_caption("Aline Invasion")
    ship = Ship(screen, ai_settings)

    # 开始时游戏的主循环
    while True:

        #监视键盘和鼠标事件
        gf.check_events(ship)
        
        ship.update()

        gf.update_screen(ai_settings, screen, ship)

run_game()

