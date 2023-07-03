from code.globals.constanst import path_root_project, join
from code.states.Game.Level1.Resources.GiftAndCurses.AbstractsGiftAndCurse import AbstractGiftCurse
from code.states.Game.Level1.Resources.Battery import ModifierPercentageCharge


class Curse(AbstractGiftCurse):
    def __init__(self, screen):
        self.__path_img = join(path_root_project, 'src', 'giftAndCurse', 'curse.png')
        AbstractGiftCurse.__init__(self, screen, self.__path_img)

    @staticmethod
    def __less_charge_battery():
        ModifierPercentageCharge.decrease_level_battery()

    def exe(self):
        if self.is_collision():
            self.__less_charge_battery()

        self.run()

    



