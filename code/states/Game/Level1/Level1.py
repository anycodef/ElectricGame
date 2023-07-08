from code.states.Game.Level1.Resources.Character import CharacterUser
from code.states.Game.BasicStateLevel import BasicStateLevel
from code.states.Game.Level1.Resources.Platform import Platform
from code.states.Game.Level1.Resources.GiftAndCurses.ManagerGiftCurse import ManagerGiftCurse
from code.states.Game.Level1.Resources.Battery import Battery
from code.states.Game.Level1.Resources.Portals.ManagerPortals import ManagerPortals

from pygame.display import flip


class StateLevel1(BasicStateLevel):
    def __init__(self, screen, obj_exchanger_interface):
        BasicStateLevel.__init__(self, screen, obj_exchanger_interface)
        self.character1 = CharacterUser(screen, self.clock.get_fps)
        self.battery = Battery(screen)

        self.platform = Platform(screen)
        self.manager_gift_curse = ManagerGiftCurse(screen)
        self.manager_portals = ManagerPortals(screen)

    def run(self):
        while self.list_class_obj_return == [None, None]:
            self.update_event()
            self.screen.fill(self.background_color)

            self.character1.execution(self.queue_event)
            self.platform.run()

            self.manager_gift_curse.run()
            self.manager_portals.run()

            self.battery.run()

            self.list_class_obj_return = self.get_list_class_obj_return_and_exe_exchanger_interface()

            flip()
            self.clock.tick(self.FPS)

        return self.list_class_obj_return









