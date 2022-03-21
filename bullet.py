import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self,screen,gun):
        '''СОздаем пулю в позиции пушки'''
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 5, 12)
        self.color = 0, 187, 212
        self.speed = 5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        '''Перемещение пули вверх'''
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        '''рисуем пулю на экране'''
        pygame.draw.rect(self.screen,color = self.color, rect = self.rect)

