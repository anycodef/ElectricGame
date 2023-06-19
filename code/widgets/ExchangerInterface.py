from pygame import Rect
from pygame.draw import rect

from pygame.mouse import get_pos, get_pressed

from code.widgets.buttons import ButtonManager


def get_last_index(list_, value):
    index = None
    list_copy = list_.copy()

    if value in list_copy:
        list_copy.reverse()
        index = list_copy.__len__() - list_copy.index(value) - 1

    return index


class ManagerLog:
    def __init__(self):
        self.queue_class_events = []
        self.__object_pause = []

        self.current_class = None

    def add_object_pause(self, obj):
        self.__object_pause.append(obj)

    def remove_object_pause(self, obj):
        self.__object_pause.remove(obj)

    def get_all_object_pause(self):
        return self.__object_pause


class LauncherRect:
    def __init__(self, screen):
        self.__screen = screen

        self.__color_on_top_of = 'light red'
        self.__color_normal = 'red'
        self.__color_pressed = 'blue'
        self.__color = self.__color_normal

        self.__rect = Rect(0, 0, 10, 100)

        # to move
        self.is_active = False

    def __listen_for_active(self):
        if self.is_active:
            self.is_active = False

        if (self.__rect.x <= get_pos()[0] <= self.__rect.x + self.__rect.width) or \
                (self.__rect.y <= get_pos()[1] <= self.__rect.y + self.__rect.height):
            self.__color = self.__color_on_top_of

            if get_pressed()[0]:
                self.__color = self.__color_pressed
                self.is_active = True
        else:
            self.__color = self.__color_normal

    def __show(self):
        rect(self.__screen, self.__color, self.__rect)

    def move_horizontal(self, speed):
        self.__rect.x += speed

    def run(self):
        self.__show()
        self.__listen_for_active()


class MenuGui:
    def __init__(self, screen):
        # main surface
        self.__screen = screen
        self.__rect_father = screen.get_rect()

        # rect default for sideBar
        self.__rect = Rect(0, 0, 300, self.__rect_father.height)

        # style
        self.__background_color = 'light blue'

        # moving sideBar
        self.__speed_x = 10
        self.__moving = False
        self.__is_active = False
        self.__limit_move = self.__rect.width

        # rect launcher
        self.__launcher = LauncherRect(self.__screen)

        # manager buttons
        self.__manager_buttons = ButtonManager(screen, self.__rect)

    def set_full_screen(self):
        self.__rect.width = self.__rect_father.width

    def set_gui_sidebar(self):
        self.__rect.width = 300

    def update_list_of_name_buttons(self, text_state):
        self.__manager_buttons.init_buttons(text_state)

    def __listen_move(self):  # ready
        # switch to convert of moving to no moving and vice verse
        if not self.__moving and self.__launcher.is_active:
            self.__moving = self.__launcher.is_active
            self.__is_active = self.__is_active * self.__is_active

        if self.__moving:
            # move all in gui
            self.__rect.x += self.__speed_x
            self.__launcher.move_horizontal(self.__speed_x)
            self.__manager_buttons.move_horizontal(self.__speed_x)

            # verify if the moving end or not
            if -self.__limit_move >= self.__rect.x or self.__rect.x >= 0:
                if self.__rect.x >= 0:
                    self.__rect.x = 0
                else:
                    self.__rect.x = -self.__limit_move

                self.__speed_x *= -1
                self.__moving = False

    def __show(self):
        rect(self.__screen, self.__background_color, self.__rect)

    def get_status_select(self):
        return self.__manager_buttons.get_status_selected()

    def run(self):
        self.__show()
        self.__listen_move()
        self.__launcher.run()
        self.__manager_buttons.run()


class ExchangerInterface:
    def __init__(self, screen):

        # gui interface
        self.__gui_interface = MenuGui(screen)

        # manage queue event objet
        # self.__manager_log_status_class = ManagerLog()

    def set_gui_full_screen(self):
        self.__gui_interface.set_full_screen()

    def set_option_available_on_state(self, list_states_available):
        self.__gui_interface.update_list_of_name_buttons(list_states_available)

    def get_list_class_obj(self):
        if self.__gui_interface.get_status_select():
            return None
        else:
            return [self.__gui_interface.get_status_select(), None]

    def run(self):
        self.__gui_interface.run()


