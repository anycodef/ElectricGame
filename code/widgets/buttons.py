from pygame.font import SysFont
from pygame.mouse import get_pos, get_pressed


# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
class Button:
    def __init__(self, text: str, color_text, color_text_selected, size_text, screen, posy, state, rect_father):
        # text that show under button
        self.__screen = screen
        self.__text = text

        # color for three cases
        self.__color = color_text
        self.__color_text_unselected = color_text
        self.__color_text_selected = color_text_selected

        self.__size = size_text

        self.__font = SysFont("Impact", self.__size)
        self.__text_img = self.__font.render(self.__text, False, self.__color)
        self.__rect = self.__text_img.get_rect()

        self.__rect.y = posy
        self.__rect.x = rect_father.x + (rect_father.width - self.__text_img.get_width()) / 2

        self.state = state  # This is a class
        self.extreme_position = [[self.__rect.x, self.__rect.y + self.__rect.height / 2],
                                 [self.__rect.x + self.__rect.width, self.__rect.y + self.__rect.height / 2]]

        # active
        self.pressed = False
        self.on_top_of = False

    # This function return a new state
    def get_extreme_position(self):
        if self.on_top_of:
            return self.extreme_position
        else:
            return None

    def move_horizontal(self, speed):
        self.__rect.x += speed

    def get_status(self):
        if self.pressed:
            return self.state
        else:
            return None

    def __listen_the_mouse(self):

        # check if the mouse is in the button and if it's pressed

        self.on_top_of = (self.__rect.x <= get_pos()[0] <= self.__rect.x + self.__rect.width) and \
                         (self.__rect.y <= get_pos()[1] <= self.__rect.y + self.__rect.height)

        if self.on_top_of:
            self.__color = self.__color_text_selected
            self.pressed = get_pressed()[0]

        else:
            self.__color = self.__color_text_unselected

    def __show(self):
        # show button in the screen
        self.__text_img = self.__font.render(self.__text, False, self.__color)
        self.__screen.blit(self.__text_img, (self.__rect.x, self.__rect.y))

    def run(self):
        self.__listen_the_mouse()
        self.__show()


# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
class ButtonManager:
    def __init__(self, screen, rect_father):
        self.__list_name_button_and_state = None  # This is a list [name, class_state]
        self.__number_buttons = None

        # style
        self.__padding_y = 10
        self.__size_text = 27
        self.__color_text = 'white'
        self.__color_text_selected = 'red'

        # main surface
        self.__screen = screen
        self.__rect_father = rect_father

        # position
        self.__pos_y = None

        # list buttons for managed
        self.__list_button_obj = []

    def __set_name_buttons(self, name_button_and_state):
        self.__list_name_button_and_state = name_button_and_state
        self.__number_buttons = self.__list_name_button_and_state.__len__()

        self.__pos_y = self.__rect_father.y + (self.__rect_father.height - self.__number_buttons * self.__size_text - (
                self.__number_buttons - 1) * self.__padding_y) / 2

    # Instance class Button and storage on the list button obj
    def init_buttons(self, name_button_and_state):
        self.__set_name_buttons(name_button_and_state)
        self.__list_button_obj.clear()

        for i in range(self.__number_buttons):
            self.__list_button_obj.append(Button(self.__list_name_button_and_state[i][0],
                                                 self.__color_text, self.__color_text_selected,
                                                 self.__size_text, self.__screen, self.__pos_y,
                                                 self.__list_name_button_and_state[i][1], self.__rect_father))

            self.__pos_y += self.__size_text + self.__padding_y

    def move_horizontal(self, speed_x=0):
        for button in self.__list_button_obj:
            button.move_horizontal(speed_x)

    def get_extreme_button_selected(self):
        position_extreme_button = None
        i = 0

        while position_extreme_button is None and i != self.__list_button_obj.__len__():
            position_extreme_button = self.__list_button_obj[i].get_extreme_position()
            i += 1

        return position_extreme_button

    def get_status_selected(self):
        status_selected = None
        i = 0

        while status_selected is None and i != self.__list_button_obj.__len__():
            status_selected = self.__list_button_obj[i].get_status()
            i += 1

        return status_selected

    def run(self):
        for button in self.__list_button_obj:
            button.run()
