from code.globals.generalState import BasicState
from pygame.event import get as get_queue_event
from pygame.draw import rect
from pygame import QUIT
from pygame.display import flip

from code.widgets.text import CardText

# constants
from code.globals.constanst import EXIT_PROGRAM, description_for_objects

# test ------------------------------------------------------
from code.globals.Math.physics.uniformMove import UniformMove
# test ------------------------------------------------------


class UnitCard:
    def __init__(self, screen, x, y, width_card, height_card, content: dict, ):

        self.screen = screen
        # ------------------------------------- unit card ---------------------------------------
        self.pos_x_unit_card, self.pos_y_unit_card = x, y   # only axes x will be no constant

        self.color_fill_background = 'black'
        self.width_unit_card = width_card
        self.height_unit_card = height_card
        self.radius = 5
        self.padding = 10
        self.proportion_width_of_image_part = .3
        self.proportion_width_of_title_description_part = .7
        # ------------------------------------- unit card ---------------------------------------

        # ------------------------------------- part content ---------------------------------------
        self.pos_x_content_part, self.pos_y_content_part = self.pos_x_unit_card + self.padding, self.pos_y_unit_card + self.padding
        self.width_content_part = self.width_unit_card - 3 * self.padding
        # ------------------------------------- unit card ---------------------------------------

        # ------------------------------------- image part ---------------------------------------
        self.pos_x_img_part, self.pos_y_img_part = self.pos_x_content_part, self.pos_y_content_part
        self.width_img_part = self.proportion_width_of_image_part * self.width_content_part
        # ------------------------------------- image part ---------------------------------------

        # ------------------------------------- title - description part ---------------------------------------
        self.pos_x_title_part = self.pos_x_img_part + self.width_img_part + self.padding
        self.pos_y_title_part = self.pos_y_content_part
        self.pos_x_description_part = self.
        self.width_title_and_description_part = {self.proportion_width_of_title_description_part * self.width_content_part
        # ------------------------------------- title - description part ---------------------------------------


        self.card_text_content = CardText(screen, self.width)

    def run(self):

        # show a rect of background
        rect(self.screen, self.color_fill_background, (self.pos_x, self.pos_y, self.width, self.height), self.radius)

        # show cardText
        # show cardTitle
        # show cardImg


class PackageCardDescription:
    def __init__(self, screen):

        self.margin = 10
        self._pos_x, self.pos_y = self.margin, self.margin
        self.color_fill = 'gray'
        self.width = screen.get_width() - 2 * self.margin


class StateRule(BasicState):
    def __init__(self, screen):
        BasicState.__init__(self, screen)
        self.background_color = 'red'

        # test --------------------------------------------
        self.current_pos = [screen.get_width() + 10, 100]
        self.pos_end = [10, 100]
        self.moveMode = UniformMove(self.pos_end, self.current_pos, 1)
        self.card1 = CardText(screen, 300, self.current_pos, 'white', "This is my fantastic creation until today.", 20, "black")
        # test --------------------------------------------

    def run(self):
        while not self.class_for_return:
            # fill all windows with a color
            self.screen.fill(self.background_color)

            # test --------------------------------------------
            self.card1.show(new_pos=self.current_pos)
            if self.current_pos != self.pos_end:
                current_pos_aux = self.moveMode.run()
                self.current_pos = current_pos_aux
            elif self.moveMode:
                self.moveMode = None
            # test --------------------------------------------

            # manager of events
            for event in get_queue_event():
                if event.type == QUIT:
                    self.class_for_return = EXIT_PROGRAM

            flip()
            self.clock.tick(self.FPS)

        return self.class_for_return

