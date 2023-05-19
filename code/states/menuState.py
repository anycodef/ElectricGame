# import of the library pygame
from pygame.display import flip
from pygame.event import get as get_event
from pygame import QUIT

# buttons and basic class for state
from code.widgets.buttons import ButtonManager
from code.globals.generalState import BasicState
from code.globals.constanst import EXIT_PROGRAM

# class for the effects of arc voltaic and cables
from code.globals.Effects.childOfArchVoltaic import CableWithArcVoltaicForMenu

# other states
from code.states.stateRule import StateRule
from code.states.Game.stateGameLevels import StateGameLevels


# This state define an interface where
class MenuState(BasicState):
    def __init__(self, screen):
        BasicState.__init__(self, screen)

        # style general button
        self.list_text_and_status = [['Play', StateGameLevels],
                                     ['Rules', StateRule],
                                     ['Exit', EXIT_PROGRAM]]

        self.log_class_status = []

        self.color_text = "white"
        self.color_selected = "blue"
        self.size_text = 30

        # buttons - manager
        self.managerButtons = ButtonManager(self.list_text_and_status, self.color_text, self.color_selected, self.size_text, self.screen, self.screen.get_rect())
        self.managerButtons.init_buttons()

        # arc voltaic object for do effect
        self.effect_arc_voltaic = CableWithArcVoltaicForMenu(screen)

    def run(self):  # return a state class

        # main while of this state
        while not self.class_for_return:

            # Give a color to background of the menu in this case black
            self.screen.fill(self.background_color)

            # show buttons
            self.class_for_return, two_points_beside_button = self.managerButtons.run()

            # show a voltaic arc with your cables
            self.effect_arc_voltaic.run(two_points_beside_button)

            # manage an event under the menu state
            for event in get_event():
                if event.type == QUIT:
                    self.class_for_return = EXIT_PROGRAM

            # update screen
            flip()
            self.clock.tick(self.FPS)

        return self.class_for_return
