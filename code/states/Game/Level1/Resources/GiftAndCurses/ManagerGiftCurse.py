from code.states.Game.Level1.Resources.GiftAndCurses.Curse import Curse
from code.states.Game.Level1.Resources.GiftAndCurses.Gift import Gift


class ManagerGiftCurse:
    def __init__(self, screen):
        self.amount_gift = 2
        self.amount_curse = 4
        self.__list_gift = [Gift(screen) for i in range(self.amount_gift)]
        self.__list_curse = [Curse(screen) for i in range(self.amount_curse)]

    def run(self):
        for gift in self.__list_gift:
            gift.exe()

        for curse in self.__list_curse:
            curse.exe()


