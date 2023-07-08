from code.globals.constanst import path_root_project, join
from code.states.Game.Level1.Resources.Portals.AbstractPortal import Portal
from code.states.Game.Level1.Resources.Portals.AbstractPortalVerticalHorizontal import AbstractPortalHorizontal


class PortalHorizontal(Portal):
    def __init__(self, screen):
        self.__pathfile = join(path_root_project, 'src', 'portal', 'portal_horizontal.png')
        Portal.__init__(self, screen, self.__pathfile)

    @staticmethod
    def __for_collision():
        for method in AbstractPortalHorizontal.list_method_of_the_object_affect:
            method()

    def exe(self):
        if self.is_collision():
            self.__for_collision()
            self.end_collision()

        self.run()



