from pygame.display import flip
from pygame.time import Clock
from pygame.event import get as get_event
from pygame import QUIT

# for buttons
from pygame.font import SysFont
from pygame.mouse import get_pos, get_pressed


class Button:
    def __init__(self, text: str, color_text, color_text_selected, size_text, screen, posy, state):
        self.text = text
        self.color = color_text
        self.color_text_unselected = color_text
        self.color_text_selected = color_text_selected
        self.size = size_text

        self.font = SysFont("arial", self.size)
        self.text = self.font.render(self.text, False, self.color)

        self.screen = screen
        self.posY = posy
        self.posX = (self.screen.get_size()[0] - self.text.get_size()[0]) / 2

        self.state_for_return = None
        self.state = state

    # This function return a new state
    def run(self):

        # check if the mouse is in the button and if it's pressed
        if (self.posX <= get_pos()[0] <= self.posX + self.text.get_size()[0]) and \
                (self.posY <= get_pos()[1] <= self.posY + self.text.get_size()[1]):
            self.color = self.color_text_selected

            if get_pressed()[0]:
                self.state_for_return = self.state
        else:
            self.color = self.color_text_unselected

        # show button in the screen
        self.screen.blit(self.text, (self.posX, self.posY))

        return self.state_for_return


class ButtonManager:
    def __init__(self, list_text_button):
        self.list_text_button = list_text_button
        self.number_buttons = self.list_text_button.__len__()

        # style
        self.padding_y = 5
        self.list_pos_y = []

    def init_buttons(self):
        pass

    def run(self):
        pass


class MenuState:
    def __init__(self, screen):
        self.screen = screen
        self.background_color = "black"

        self.exitState = False

        self.clock = Clock()
        self.FPS = 60

        self.list_for_return = [None, None]

    def run(self) -> list:

        # main while of this state
        while not self.exitState:

            # Give a color to background of the menu in this case black
            self.screen.fill(self.background_color)

            # manage a event under the menu state
            for event in get_event():
                if event.type == QUIT:
                    self.exitState = True
                    self.list_for_return = ['exitProgram', None]

            flip()
            self.clock.tick(self.FPS)

        return self.list_for_return

