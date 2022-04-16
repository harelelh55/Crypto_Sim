from constants import *
from Button import *


def mouse_in_button(button, mouse_pos):
    if button.x_pos + button.width > mouse_pos[0] > button.x_pos and \
            button.y_pos < mouse_pos[1] < button.y_pos + button.height:
        return True


start_button = Button(START_RECT_X, START_RECT_Y, START_RECT_WIDTH, START_RECT_HEIGHT)
START_RECT_X = 180
START_RECT_Y = 600
START_RECT_WIDTH = 200
START_RECT_HEIGHT = 50
