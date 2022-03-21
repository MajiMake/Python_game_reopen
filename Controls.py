import pygame
import sys
from bullet import Bullet
from ino import Ino

def events(screen,gun, bullets):
    '''Обработка события'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #Вправо
            if event.key == pygame.K_d:
                gun.move_right = True
            #Влево
            elif event.key == pygame.K_a:
                gun.move_left = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # Вправо
            if event.key == pygame.K_d:
                gun.move_right = False
                #Влево
            elif event.key == pygame.K_a:
                gun.move_left = False

def update(bg_color, screen,gun, inos, bullets):
    '''Обновление экрана'''
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(bullets):
    '''Обновлять позиции пуль'''
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def create_army(screen, inos):
    '''Создание армии пришельцев'''
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700-2*ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((250-2*ino_height) / ino_height)

    for row_number in range(number_ino_y):
        for one_ino in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + ino_width * one_ino
            ino.y = ino_height + ino_height * row_number
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row_number
            inos.add(ino)

def update_inos(inos):
    '''Обновляет позицию инопланетян'''
    inos.update()