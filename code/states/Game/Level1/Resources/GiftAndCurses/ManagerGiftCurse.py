from code.states.Game.Level1.Resources.GiftAndCurses.Curse import Curse
from code.states.Game.Level1.Resources.GiftAndCurses.Gift import Gift


class ManagerGiftCurse:
    def __init__(self, screen):
        self.__list_gift = [Gift(screen) for i in range(5)]
        self.__list_curse = [Curse(screen) for i in range(5)]

    def run(self):
        for obj12 in self.__list_gift, self.__list_curse:
            for obj in obj12:
                obj.exe()







