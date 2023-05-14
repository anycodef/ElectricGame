from pygame.time import Clock


class BasicState:
    def __init__(self, screen):

        self.screen = screen
        self.background_color = "black"

        self.exitState = False

        self.list_for_return = [None, None]

        self.clock = Clock()
        self.FPS = 60
