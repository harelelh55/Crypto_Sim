import pygame as pygame

from Manager import *
from buttons import *
from constants import *

clock = pygame.time.Clock()
fps = 60
pygame.init()
screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Crypto Bird')

manager = Manager(screen)

##start of background
manager.show_home(ground_scroll)

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

        if event.type == pygame.KEYDOWN:
            print("test2")
            BIRD_Y  += 5

    return finish


while not isFinished():
    clock.tick(fps)
    ground_scroll = ground_scroll - scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0
    if manager.page == Pages.main:
        manager.show_home(ground_scroll)
    elif manager.page == Pages.live:
        manager.show_live(ground_scroll)

    pygame.display.flip()

pygame.quit()
