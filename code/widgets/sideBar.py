from pygame import Rect

from code.states.menuState import MenuState
from code.states.Game.stateGameLevels import StateGameLevels
from code.widgets.buttons import ButtonManager


class SideBar:
    def __init__(self, screen, x_bar, y_bar, width_bar, height_bar, back_status, list_button_depending_status=None):
        # main surface
        self.screen = screen

        # style sideBar
        self.color_background = 'gray'
        self.color_words = 'blue'
        self.color_words_selected = 'red'
        self.size_word_button = 20

        # rect
        self.rect = Rect(x_bar, y_bar, width_bar, height_bar)

        # list buttons
        self.list_text_and_status = [['Play', StateGameLevels],
                                     ['Menu', MenuState]]

        if list_button_depending_status:
            self.list_text_and_status += list_button_depending_status

        self.list_text_and_status += [['Back', back_status]]

        self.manager_buttons = ButtonManager(self.list_text_and_status, self.color_words, self.color_words_selected,
                                             self.size_word_button, self.screen, self.rect)

        self.speed_x = 0

    def set_pos(self):

        if self.speed_x:
            self.rect.x += self.speed_x



