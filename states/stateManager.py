# states
from menuState import MenuState

# dependents
from pygame.display import set_mode, set_caption


# This class is a main surface where put all graphics.
class Screen:
    def __init__(self):
        self.__width = 900
        self.__height = 700

        self.obj = set_mode((self.__width, self.__height))
        set_caption("ElectricGame")


# This class execute all state of game.
# Manage your instance, execute, delete and change to another state.
# The main state is a menu state.
# Too, manage a screen that is a platform where all happen.

class StateManager:
    def __init__(self):
        self.states = {
            "menu": MenuState
        }

        self.class_state = self.states["menu"]
        self.instance_new_state = True
        self.objet_state = None

        self.exitState = False

        self.screen = Screen()

    def run(self):
        while not self.exitState:
            if self.instance_new_state:
                self.objet_state = self.class_state(self.screen)
                self.instance_new_state = False


