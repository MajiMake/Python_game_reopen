import pygame, Controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats

def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 350))
    pygame.display.set_caption('Space guardian')
    bg_color  = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    Controls.create_army(screen, inos)
    stats = Stats()

    while True:
        Controls.events(screen,gun,bullets)
        gun.update_gun()
        Controls.update(bg_color, screen, gun, inos, bullets)
        Controls.update_bullets(inos,bullets)
        Controls.update_inos(stats,screen,gun, inos, bullets)


run()


