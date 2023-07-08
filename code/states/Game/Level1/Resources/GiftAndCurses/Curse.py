from code.globals.constanst import path_root_project, join
from code.states.Game.Level1.Resources.GiftAndCurses.AbstractsGiftAndCurse import AbstractGiftCurse
from code.states.Game.Level1.Resources.Battery import ModifierPercentageCharge
from code.states.Game.Level1.Resources.weapon import AbstractArcVoltaicWeaponCollision


class Curse(AbstractGiftCurse):
    def __init__(self, screen):
        self.__path_img = join(path_root_project, 'src', 'giftAndCurse', 'curse.png')
        AbstractGiftCurse.__init__(self, screen, self.__path_img)
        self.__fired = False

        self.__width_parent_surface = screen.get_width()

    @staticmethod
    def __less_charge_battery():
        ModifierPercentageCharge.decrease_level_battery()

    def listen_fired(self):  # This function is the function which will be to execute when the
        # weapon is shooting
        self.__fired = True
        self.set_reposition(self.__fired)
        return [self.get_rect().x, self.get_rect().y]

    def __available_for_fired(self):
        if self.get_rect().x + self.get_rect().width < self.__width_parent_surface and \
                self.listen_fired not in AbstractArcVoltaicWeaponCollision.list_function_shoot:
            AbstractArcVoltaicWeaponCollision.list_function_shoot.append(self.listen_fired)

    def exe(self):
        if self.is_collision():
            self.__less_charge_battery()
            self.end_collision()

        self.__available_for_fired()

        self.run()
