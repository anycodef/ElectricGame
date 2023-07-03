from code.states.Game.Level1.Resources.GiftAndCurses.Curse import Curse
from code.states.Game.Level1.Resources.GiftAndCurses.Gift import Gift

from code.states.Game.Level1.Resources.weapon import AbstractArcVoltaicWeaponCollision


class ManagerGiftCurse:
    def __init__(self, screen):
        self.__list_gift = [Gift(screen) for i in range(2)]
        self.__list_curse = [Curse(screen) for i in range(2)]

    def run(self):
        for gift in self.__list_gift:
            gift.exe()

        for curse in self.__list_curse:
            curse.exe()


