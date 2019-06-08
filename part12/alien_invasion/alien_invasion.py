import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.width, ai_settings.height))
    pygame.display.set_caption("Aline Invasion")
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, aliens, ship)
    # 开始时游戏的主循环
    while True:

        #监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        
        gf.update_bullets(bullets)
        ship.update()
        
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)

run_game()

