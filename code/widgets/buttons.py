from pygame.font import SysFont
from pygame.mouse import get_pos, get_pressed


class Button:
    def __init__(self, text: str, color_text, color_text_selected, size_text, screen, posy, state, rect_father):
        self.text = text

        self.color = color_text
        self.color_text_unselected = color_text
        self.color_text_selected = color_text_selected

        self.size = size_text

        self.font = SysFont("Impact", self.size)
        self.text_img = self.font.render(self.text, False, self.color)
        self.rect = self.text_img.get_rect()

        self.screen = screen

        self.rect.y = posy
        self.rect.x = rect_father.x + (rect_father.width - self.text_img.get_width()) / 2

        self.state = state  # This is a class

    # This function return a new state
    def run(self):
        # initialize state returned
        state_class_for_return = None
        two_points_beside_button_return = None

        # check if the mouse is in the button and if it's pressed
        if (self.rect.x <= get_pos()[0] <= self.rect.x + self.rect.width) and \
                (self.rect.y <= get_pos()[1] <= self.rect.y + self.rect.height):
            self.color = self.color_text_selected

            two_points_beside_button_return = [
                [self.rect.x, self.rect.y + self.rect.height/2],
                [self.rect.x + self.rect.width, self.rect.y + self.rect.height/2]]

            if get_pressed()[0]:
                state_class_for_return = self.state
        else:
            self.color = self.color_text_unselected

        # show button in the screen
        self.text_img = self.font.render(self.text, False, self.color)
        self.screen.blit(self.text_img, (self.rect.x, self.rect.y))

        return state_class_for_return, two_points_beside_button_return


class ButtonManager:
    def __init__(self, list_name_button_and_state, color_text, color_text_selected, size_text, screen, rect_father):
        self.list_name_button_and_state = list_name_button_and_state  # This is a list [name, class_state]
        self.number_buttons = self.list_name_button_and_state.__len__()

        # style
        self.padding_y = 10
        self.size_text = size_text
        self.color_text = color_text
        self.color_text_selected = color_text_selected

        # main surface
        self.screen = screen
        self.rect_father = rect_father

        # position
        self.pos_y = rect_father.y + (rect_father.height - self.number_buttons * self.size_text - (
                    self.number_buttons - 1) * self.padding_y) / 2

        # list buttons for managed
        self.list_button_obj = []

    def init_buttons(self):
        for i in range(self.number_buttons):
            self.list_button_obj.append(Button(self.list_name_button_and_state[i][0],
                                               self.color_text, self.color_text_selected,
                                               self.size_text, self.screen, self.pos_y,
                                               self.list_name_button_and_state[i][1], self.rect_father))

            self.pos_y += self.size_text + self.padding_y

    def set_pos_side_bar(self, speed_x=0):
        if speed_x:
            self.list_button_obj

            # here implement a code for do effects move on the any status that implement a bar side

    def run(self):
        state_returned = None
        two_point_return = None

        for button_obj in self.list_button_obj:
            state, two_points_beside_button = button_obj.run()

            if two_points_beside_button:
                if not two_point_return:
                    two_point_return = two_points_beside_button

            if state:
                if not state_returned:
                    state_returned = button_obj.state

        return state_returned, two_point_return
