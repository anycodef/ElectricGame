# dependents for screen
from pygame.display import set_mode, set_caption
from pygame import quit, init as init_pygame
from sys import exit

# states for default
from code.states.menuState import MenuState

# class exchange interface
from code.widgets.ExchangerInterface import ExchangerInterface

# code for to standardized mode of return
from code.globals.constanst import EXIT_PROGRAM

# flag to modify the dimension of the screen to full-screen
from pygame import FULLSCREEN


# This class is a main surface where put all graphics.
class Screen:
    def __init__(self):
        # This object is the windows
        self.obj = set_mode(flags=FULLSCREEN)
        set_caption("ElectricGame")  # Title of windows


# This class execute all state of game.
# Manage your instance, execute, delete and change to another state.
# The main state is a menu state.
# Too, manage a screen that is a platform where all happen.

class StateManager:
    def __init__(self):
        # initialize all modulo
        init_pygame()

        # to manage a classes state
        self.__class_state = MenuState  # save a class for instance.
        self.__objet_state = None  # Save of obj of class.
        self.__objet_state_next = None

        self.__screen = Screen()  # object that content an obj windows

        self.__exchanger_interface = ExchangerInterface(self.__screen.obj)

    def run(self):
        # main loop
        while self.__class_state != EXIT_PROGRAM:

            # Instance a class state
            if self.__class_state:
                self.__objet_state = self.__class_state(self.__screen.obj, self.__exchanger_interface)
                self.__class_state = None

            # Run state and wait for a new class state
            self.__class_state, self.__objet_state_next = self.__objet_state.run()
            if self.__objet_state_next:
                self.__objet_state = self.__objet_state_next
                self.__objet_state_next = None

        quit()
        exit()
