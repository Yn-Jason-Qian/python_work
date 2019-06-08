import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, settings, screen):
        super().__init__()

        self.screen = screen
        self.settings = settings

        # 加载图片
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 设置初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 保存位置
        self.x = float(self.rect.x)


    def biltme(self):
        self.screen.blit(self.image, self.rect)
