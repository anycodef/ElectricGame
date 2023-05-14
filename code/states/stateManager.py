# dependents for screen
from pygame.display import set_mode, set_caption
from pygame import quit, init as init_pygame
from sys import exit

# states
from .menuState import MenuState
from .stateRule import StateRule
from .Game.stateGameLevels import StateGameLevels

# code for to standardized mode of return
from code.globals.codeReturn import code_return


# This class is a main surface where put all graphics.
class Screen:
    def __init__(self):
        # These are dimensions for screen
        self.__width = 900
        self.__height = 600

        # This object is the windows
        self.obj = set_mode((self.__width, self.__height))
        set_caption("ElectricGame")  # Title of windows


# This class execute all state of game.
# Manage your instance, execute, delete and change to another state.
# The main state is a menu state.
# Too, manage a screen that is a platform where all happen.

class StateManager:
    def __init__(self):
        # initialize all modulo
        init_pygame()

        # These are a states of game
        self.__states = {
            "MenuState": MenuState,
            "GameState": StateGameLevels,
            "RuleState": StateRule
        }

        self.__class_state = self.__states["MenuState"]  # save a class for instance.
        self.__instance_new_state = True  # flag which indicate if action of instance will do
        self.__objet_state = None  # Save of obj of class.

        self.__exitState = False
        self.__list_mode_and_value_return_state = None  # This list returned a list with mode that is a

        self.__screen = Screen()  # object that content an obj windows

    def run(self):
        while not self.__exitState:

            # Instance a class state
            if self.__instance_new_state:
                self.__objet_state = self.__class_state(self.__screen.obj)
                self.__instance_new_state = False

            # Run state and way for list return. This list must have two elements
            self.__list_mode_and_value_return_state = self.__objet_state.run()

            # check the key and value returned
            if code_return[self.__list_mode_and_value_return_state[0]] == 1:
                self.__exitState = True
            elif code_return[self.__list_mode_and_value_return_state[0]] == 2:
                self.__instance_new_state = True
                self.__class_state = self.__states[self.__list_mode_and_value_return_state[1]]

        quit()
        exit()
