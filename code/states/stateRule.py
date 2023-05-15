from code.globals.generalState import BasicState
from pygame.event import get as get_queue_event
from pygame import QUIT

# delete
from pygame.display import flip


class StateRule(BasicState):
    def __init__(self, screen):
        BasicState.__init__(self, screen)
        self.background_color = "red"

    def run(self):
        while not self.exitState:
            # fill all windows with a color
            self.screen.fill(self.background_color)

            # manager of events
            for event in get_queue_event():
                if event.type == QUIT:
                    self.exitState = True
                    self.list_for_return = ['exitProgram', None]

            flip()
            self.clock.tick(self.FPS)

        return self.list_for_return
