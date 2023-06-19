from pygame.time import Clock


class BasicState:
    def __init__(self, screen):

        self.screen = screen
        self.background_color = "white"

        self.list_class_obj_return = [None, None]

        self.clock = Clock()
        self.FPS = 60
