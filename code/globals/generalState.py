from pygame.time import Clock


class BasicState:
    def __init__(self, screen):

        self.screen = screen
        self.background_color = "black"

        self.class_for_return = None

        self.clock = Clock()
        self.FPS = 60
