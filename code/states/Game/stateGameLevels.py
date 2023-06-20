from code.globals.generalState import BasicState
from pygame.event import get as get_queue_event
from pygame.display import flip
from pygame import QUIT

from code.globals.constanst import EXIT_PROGRAM


class Levels:
    pass


class StateGameLevels(BasicState):
    def __init__(self, screen, obj_exchanger_interface):
        BasicState.__init__(self, screen)

        self.__list_names_buttons = ['Menu', 'Rules', 'Exit']

        self.__obj_exchanger_interface = obj_exchanger_interface
        self.__obj_exchanger_interface.set_gui_side_bar()
        self.__obj_exchanger_interface.set_option_available_on_state(self.__list_names_buttons)

    def run(self):
        while self.list_class_obj_return == [None, None]:
            self.screen.fill(self.background_color)

            # execute menu buttons
            self.__obj_exchanger_interface.run()
            # get list [class, obj] for return
            self.list_class_obj_return = self.__obj_exchanger_interface.get_list_class_obj()

            # manage an event under the menu state
            for event in get_queue_event():
                if event.type == QUIT:
                    self.list_class_obj_return = [EXIT_PROGRAM, None]

            # update screen
            flip()
            self.clock.tick(self.FPS)

        return self.list_class_obj_return
