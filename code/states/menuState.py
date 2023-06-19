# import of the library pygame
from pygame.display import flip
from pygame.event import get as get_event
from pygame import QUIT

# buttons and basic class for state
from code.globals.generalState import BasicState
from code.globals.constanst import EXIT_PROGRAM

# class for the effects of arc voltaic and cables
from code.globals.Effects.childOfArchVoltaic import CableWithArcVoltaicForMenu

# other states
from code.states.stateRule import StateRule
from code.states.Game.stateGameLevels import StateGameLevels


# This state define an interface where
class MenuState(BasicState):
    def __init__(self, screen, obj_exchanger_interface):
        BasicState.__init__(self, screen)

        # style general button
        self.__list_text_and_status = [['Play', StateGameLevels],
                                       ['Rules', StateRule],
                                       ['Exit', EXIT_PROGRAM]]

        self.__obj_exchanger_interface = obj_exchanger_interface
        self.__obj_exchanger_interface.set_gui_full_screen()
        self.__obj_exchanger_interface.set_option_available_on_state(self.__list_text_and_status)

        # arc voltaic object for do effect
        self.effect_arc_voltaic = CableWithArcVoltaicForMenu(screen)

    def run(self):  # return a state class

        # main while of this state
        while not self.list_class_obj_return:

            # Give a color to background of the menu in this case black
            self.screen.fill(self.background_color)

            # execute menu buttons
            self.__obj_exchanger_interface.run()
            # get list [class, obj] for return
            self.list_class_obj_return = self.__obj_exchanger_interface.get_list_class_obj()

            # manage an event under the menu state
            for event in get_event():
                if event.type == QUIT:
                    self.list_class_obj_return = [EXIT_PROGRAM, None]

            # update screen
            flip()
            self.clock.tick(self.FPS)

        return self.list_class_obj_return
