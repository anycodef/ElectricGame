# dependents
from pygame.display import set_mode, set_caption
from pygame import quit, init as init_pygame
from sys import exit

# states
from .menuState import MenuState

# code
from code.globals.codeReturn import code_return


# This class is a main surface where put all graphics.
class Screen:
    def __init__(self):
        self.__width = 900
        self.__height = 600

        self.obj = set_mode((self.__width, self.__height))
        set_caption("ElectricGame")


# This class execute all state of game.
# Manage your instance, execute, delete and change to another state.
# The main state is a menu state.
# Too, manage a screen that is a platform where all happen.

class StateManager:
    def __init__(self):
        init_pygame()

        self.__states = {
            "MenuState": MenuState,
            "GameState": None,
            "RuleState": None
        }

        self.__class_state = self.__states["MenuState"]  # save a class for instance.
        self.__instance_new_state = True  # flag which indicate if action of instance will do
        self.__objet_state = None  # Save of obj of class.

        self.__exitState = False
        self.__list_key_and_value_return_state = None

        self.__screen = Screen()

    def run(self):
        while not self.__exitState:

            # Instance a class state
            if self.__instance_new_state:
                self.__objet_state = self.__class_state(self.__screen.obj)
                self.__instance_new_state = False

            # Run state and way for list return. This list must have two elements
            self.__list_key_and_value_return_state = self.__objet_state.run()

            # check the key and value returned
            if code_return[self.__list_key_and_value_return_state[0]] == 1:
                self.__exitState = True
            elif code_return[self.__list_key_and_value_return_state[0]] == 2:
                self.__instance_new_state = True
                self.__class_state = self.__states[self.__list_key_and_value_return_state[1]]

        quit()
        exit()
