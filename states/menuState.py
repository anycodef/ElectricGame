from pygame.display import flip
from pygame.time import Clock


class MenuState:
    def __init__(self, screen):
        self.screen = screen()
        self.background_color = "black"

        self.exitState = False

        self.clock = Clock()
        self.FPS = 60

    def run(self):
        while not self.exitState:
            self.screen.fill(self.background_color)

            flip()
            self.clock.tick(self.FPS)

