from code.globals.generalState import BasicState
from pygame.event import get as get_queue_event
from pygame.display import flip
from pygame import QUIT


class StateGameLevels(BasicState):
    def __init__(self, screen):
        BasicState.__init__(self, screen)

    def run(self):
        while not self.exitState:
            self.screen.fill(self.background_color)

            for event in get_queue_event():
                if event.type == QUIT:
                    self.exitState = True
                    self.list_for_return = ['exitProgram', None]

            flip()
            self.clock.tick(self.FPS)

        return self.list_for_return
