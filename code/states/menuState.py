from pygame.display import flip
from pygame.time import Clock
from pygame.event import get as get_event
from pygame import QUIT

from code.widgets.buttons import ButtonManager


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

            # manage an event under the menu state
            for event in get_event():
                if event.type == QUIT:
                    self.exitState = True
                    self.list_for_return = ['exitProgram', None]

            flip()
            self.clock.tick(self.FPS)

        return self.list_for_return
