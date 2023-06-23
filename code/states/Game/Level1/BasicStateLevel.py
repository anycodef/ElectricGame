from code.globals.generalState import BasicState
from pygame.event import get as get_queue_event


class BasicStateLevel(BasicState):
    def __init__(self, screen, obj_exchanger_interface):
        BasicState.__init__(self, screen)

        self.__list_names_buttons = ['Menu', 'Levels', 'Rules', 'Exit']

        self.__obj_exchanger_interface = obj_exchanger_interface
        self.__obj_exchanger_interface.set_gui_side_bar()
        self.__obj_exchanger_interface.set_option_available_on_state(self.__list_names_buttons)

        self.queue_event = None

        self.background_color = 'dark gray'

        self.FPS = 120

    def get_list_class_obj_return_and_exe_exchanger_interface(self):
        self.__obj_exchanger_interface.run()
        return self.__obj_exchanger_interface.get_list_class_obj()

    def update_event(self):
        self.queue_event = get_queue_event().copy()




