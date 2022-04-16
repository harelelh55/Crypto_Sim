import pygame as pygame

from Manager import *
from buttons import *
from constants import *

pygame.init()
screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Crypto Bird')

manager = Manager(screen)

##start of background
manager.show_home()


pygame.display.flip()


def isFinished():
    finish = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if manager.page == Pages.main:
                if mouse_in_button(start_button, pos):
                    manager.page = Pages.live

    return finish


while not isFinished():
    ground_scroll = ground_scroll - scroll_speed
    if manager.page == Pages.main:
        manager.show_home()
    elif manager.page == Pages.live:
        manager.show_live()
    pygame.display.flip()

pygame.quit()
