import pygame
import sys
from bullet import Bullet

def check_events(settings, screen, ship, bullets):
    """检查事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)

def check_keydown_event(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_UP:
        ship.move_up = True
    elif event.key == pygame.K_DOWN:
        ship.move_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)

def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False
    elif event.key == pygame.K_UP:
        ship.move_up = False
    elif event.key == pygame.K_DOWN:
        ship.move_down = False


def update_screen(ai_settings, screen, ship, bullets):

    #设置背景颜色
    screen.fill(ai_settings.bg_color)

    #画子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 构建飞船
    ship.blitme()

    # 刷新屏幕
    pygame.display.flip()

def fire_bullet(settings, screen, ship, bullets):
    bullets.add(Bullet(settings, screen, ship))

def update_bullets(bullets):
    bullets.update()

    # 删除已经出屏幕的子弹
    for bullet in bullets.copy():
        if bullet.rect.y < 0:
            bullets.remove(bullet)

