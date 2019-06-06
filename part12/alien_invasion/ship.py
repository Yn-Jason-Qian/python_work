import pygame

class Ship():
    def __init__(self, screen, settings):
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.settings = settings

        # 控制移动
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

        # 飞船的坐标
        self.centerx = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.settings.ship_speed_factor_x
            self.rect.centerx = self.centerx

        if self.move_left and self.rect.left > 0:
            self.centerx -= self.settings.ship_speed_factor_x
            self.rect.centerx = self.centerx

        if self.move_up and self.rect.top > 0:
            self.bottom -= self.settings.ship_speed_factor_y
            self.rect.bottom = self.bottom

        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.settings.ship_speed_factor_y
            self.rect.bottom = self.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    
