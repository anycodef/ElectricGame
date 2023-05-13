from pygame.display import flip
from pygame.time import Clock
from pygame.event import get as get_event
from pygame import QUIT

# for buttons
from pygame.font import SysFont
from pygame.mouse import get_pos, get_pressed

from pygame.display import set_mode


class Button:
    def __init__(self, text: str, color_text, color_text_selected, size_text, screen, posy, state):
        self.text = text
        self.color = color_text
        self.color_text_unselected = color_text
        self.color_text_selected = color_text_selected
        self.size = size_text

        self.font = SysFont("Impact", self.size)
        self.text_img = self.font.render(self.text, False, self.color)

        self.screen = screen
        self.posY = posy
        self.posX = (self.screen.get_size()[0] - self.text_img.get_size()[0]) / 2

        self.state_for_return = None
        self.state = state

    # This function return a new state
    def run(self):
        # initialize state returned
        self.state_for_return = None

        # check if the mouse is in the button and if it's pressed
        if (self.posX <= get_pos()[0] <= self.posX + self.text_img.get_size()[0]) and \
                (self.posY <= get_pos()[1] <= self.posY + self.text_img.get_size()[1]):
            self.color = self.color_text_selected

            if get_pressed()[0]:
                self.state_for_return = self.state
        else:
            self.color = self.color_text_unselected

        # show button in the screen
        self.text_img = self.font.render(self.text, False, self.color)
        self.screen.blit(self.text_img, (self.posX, self.posY))

        return self.state_for_return


class ButtonManager:
    def __init__(self, list_text_button_and_state, color_text, color_text_selected, size_text, screen):
        self.list_text_button_and_state = list_text_button_and_state
        self.number_buttons = self.list_text_button_and_state.__len__()

        # style
        self.padding_y = 10
        self.size_text = size_text
        self.color_text = color_text
        self.color_text_selected = color_text_selected

        # main surface
        self.screen = screen

        # position
        self.pos_y = (self.screen.get_size()[1] - self.number_buttons * self.size_text - (self.number_buttons - 1) * self.padding_y) / 2

        # list buttons for managed
        self.list_button_obj = []

    def init_buttons(self):
        for i in range(self.number_buttons):
            self.list_button_obj.append(Button(self.list_text_button_and_state[i][0],
                                               self.color_text, self.color_text_selected,
                                               self.size_text, self.screen, self.pos_y,
                                               self.list_text_button_and_state[i][1]))

            self.pos_y += self.size_text + self.padding_y

    def run(self):
        state_returned = None

        for button_obj in self.list_button_obj:
            if button_obj.run():
                if not state_returned:
                    state_returned = button_obj.state

        return state_returned


class MenuState:
    def __init__(self, screen):

        self.screen = screen
        self.background_color = "black"

        self.exitState = False

        self.clock = Clock()
        self.FPS = 60

        self.list_for_return = [None, None]

        # style general button
        self.list_text_and_status = [["Play", ['executeState', "GameState"]],
                                     ["Rules", ['executeState', "RulesState"]],
                                     ["Exit", ['exitProgram', None]]]

        self.color_text = "white"
        self.color_selected = "red"
        self.size_text = 30

        # buttons - manager
        self.managerButtons = ButtonManager(self.list_text_and_status, self.color_text, self.color_selected, self.size_text, self.screen)
        self.managerButtons.init_buttons()

    def run(self) -> list:

        # main while of this state
        while not self.exitState:

            # Give a color to background of the menu in this case black
            self.screen.fill(self.background_color)

            # show buttons
            state_selected = self.managerButtons.run()
            if state_selected:
                self.list_for_return = state_selected
                self.exitState = True

            # manage a event under the menu state
            for event in get_event():
                if event.type == QUIT:
                    self.exitState = True
                    self.list_for_return = ['exitProgram', None]

            flip()
            self.clock.tick(self.FPS)

        return self.list_for_return

