from code.states.Game.Level1.Resources.Portals.PortalVertical import PortalVertical


class ManagerPortals:
    def __init__(self, screen):
        self.amount_vertical_portals = 1

        self.__list_vertical_portal = [PortalVertical(screen) for i in range(self.amount_vertical_portals)]

    def run(self):
        for p_v in self.__list_vertical_portal:
            p_v.exe()

