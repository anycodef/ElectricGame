from code.globals.generalState import BasicState
from pygame.event import get as get_queue_event
from pygame import QUIT
from pygame.display import flip

from code.widgets.text import CardText

# constants
from code.globals.constanst import EXIT_PROGRAM


class StateRule(BasicState):
    def __init__(self, screen):
        BasicState.__init__(self, screen)
        self.background_color = "red"

        # test --------------------------------------------
        self.card1 = CardText(screen, 300, "white", "This is my fantastic creation until today.", 20, "black")
        # test --------------------------------------------

    def run(self):
        while not self.class_for_return:
            # fill all windows with a color
            self.screen.fill(self.background_color)

            # test --------------------------------------------
            self.card1.show()
            # test --------------------------------------------

            # manager of events
            for event in get_queue_event():
                if event.type == QUIT:
                    self.class_for_return = EXIT_PROGRAM

            flip()
            self.clock.tick(self.FPS)

        return self.class_for_return

