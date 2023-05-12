from pygame.display import flip
from pygame.time import Clock
from pygame.event import get as get_event
from pygame import KEYDOWN, K_ESCAPE
from pygame.mouse import get_pos, get_pressed


class MenuState:
    def __init__(self, screen):
        self.screen = screen
        self.background_color = "black"

        self.exitState = False

        self.clock = Clock()
        self.FPS = 60

        self.list_for_return = [None, None]

    def run(self) -> list:

        while not self.exitState:
            self.screen.fill(self.background_color)

            for event in get_event():
                if event == KEYDOWN:
                    if event.type == K_ESCAPE:
                        self.exitState = True
                        self.list_for_return[0] = 'exitProgram'

            flip()
            self.clock.tick(self.FPS)

        return self.list_for_return

