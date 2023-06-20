from code.states.Game.Resources.Character import CharacterUser
from code.states.Game.Level1.BasicStateLevel import BasicStateLevel

from pygame.display import flip


class StateLevel1(BasicStateLevel):
    def __init__(self, screen, obj_exchanger_interface):
        BasicStateLevel.__init__(self, screen, obj_exchanger_interface)
        self.character1 = CharacterUser(screen)

    def run(self):
        while self.list_class_obj_return == [None, None]:
            self.update_event()
            self.screen.fill(self.background_color)

            self.character1.execution(self.queue_event)

            self.list_class_obj_return = self.get_list_class_obj_return_and_exe_exchanger_interface()

            flip()
            self.clock.tick(self.FPS)

        return self.list_class_obj_return




