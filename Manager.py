import pygame

from constants import *

ground_scroll = 0
scroll_speed = 4


class Manager:

    def __init__(self, screen):
        self.background_img = None
        self.screen = screen
        self.page = Pages.main
        background_img = pygame.image.load(BACKGROUND_PATH)
        self.background_img = pygame.transform.scale(background_img, (WINDOW_WIDTH, WINDOW_HEIGHT))
        ground_img = pygame.image.load(GROUND_PATH)
        self.ground_img = ground_img
        bird_img = pygame.image.load(BIRD_PATH).convert_alpha()
        self.bird_img = pygame.transform.scale(bird_img, (BIRD_WIDTH, BIRD_HEIGHT))

    def show_home(self, ground_scroll):
        self.screen.blit(self.background_img, (HOME_LOCATION_X, HOME_LOCATION_Y))

        header_font = pygame.font.SysFont(FONT_NAME, MAIN_HEADER_TEXT_SIZE)
        self.screen.blit(header_font.render('Crypto Bird', True, MAIN_HEADER_COLOR),
                         (MAIN_HEADER_X, MAIN_HEADER_Y))
        pygame.draw.rect(self.screen, START_RECT_COLOR,
                         pygame.Rect(START_RECT_X, START_RECT_Y, START_RECT_WIDTH, START_RECT_HEIGHT))
        start_font = pygame.font.SysFont(FONT_NAME, START_TEXT_SIZE)
        self.screen.blit(header_font.render('START', True, START_COLOR),
                         (START_X, START_Y))
        self.screen.blit(self.ground_img, (ground_scroll, GROUND_Y))
        self.screen.blit(self.bird_img, (BIRD_X, BIRD_Y))

    def show_live(self, ground_scroll):
        self.screen.blit(self.background_img, (HOME_LOCATION_X, HOME_LOCATION_Y))
        self.screen.blit(self.ground_img, (ground_scroll, GROUND_Y))
        self.screen.blit(self.bird_img, (BIRD_X, BIRD_Y))

    def make_bird_fly(self, bird_x):
        bird_x += 5
