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
    def __init__(self, screen, x, y, width_card, content: dict, size_title,
                 color_title, color_card_title, size_description, color_description, color_card_description):
        self.screen = screen
        # ------------------------------------- unit card ---------------------------------------
        self.pos_x_unit_card, self.pos_y_unit_card = x, y  # only axes x will be no constant

        self.color_fill_background = 'black'
        self.width_unit_card = width_card
        self.radius = 5
        self.padding = 10
        self.proportion_width_of_image_part = .3
        self.proportion_width_of_title_description_part = .7
        # ------------------------------------- unit card ---------------------------------------

        # ------------------------------------- part content ---------------------------------------
        self.pos_x_content_part, self.pos_y_content_part = self.pos_x_unit_card + self.padding, \
                                                           self.pos_y_unit_card + self.padding
        self.width_content_part = self.width_unit_card - 3 * self.padding
        # ------------------------------------- unit card ---------------------------------------

        # ------------------------------------- image part ---------------------------------------
        self.pos_x_img_part, self.pos_y_img_part = self.pos_x_content_part, self.pos_y_content_part
        self.width_img_part = self.proportion_width_of_image_part * self.width_content_part
        # ------------------------------------- image part ---------------------------------------

        # ------------------------------------- title - description part ---------------------------------------
        self.pos_x_title_part = self.pos_x_img_part + self.width_img_part + self.padding
        self.pos_y_title_part = self.pos_y_content_part
        self.pos_x_description_part = self.pos_x_title_part
        self.width_title_and_description_part = \
            self.proportion_width_of_title_description_part * self.width_content_part
        # ------------------------------------- title - description part ---------------------------------------

        # ------------------------------------- title - object ---------------------------------------------
        self.card_title = CardText(screen, self.width_title_and_description_part,
                                   [self.pos_x_title_part, self.pos_y_title_part],
                                   color_card_title, content['name'], size_title, color_title)
        self.height_title_card = self.card_title.height_card
        self.pos_y_description_part = self.pos_y_title_part + self.height_title_card + self.padding
        # ------------------------------------- title - object ---------------------------------------------
        # ------------------------------------- description - object ---------------------------------------------
        self.card_description = CardText(screen, self.width_title_and_description_part,
                                         [self.pos_x_description_part, self.pos_y_description_part],
                                         color_card_description, content['description'], size_description,
                                         color_description)
        self.height_description_card = self.card_description.height_card
        self.height_img_part = self.height_title_card + self.padding + self.height_description_card
        self.height_unit_card = self.height_img_part + 2 * self.padding

    def show(self):
        # show a rect of background
        rect(self.screen, self.color_fill_background,
             (self.pos_x_unit_card, self.pos_y_unit_card, self.width_unit_card, self.height_unit_card), self.radius)

        # show cardTitle
        self.card_title.show()
        # show cardText
        self.card_description.show()
        # show cardImg


class PackageCardDescription:
    def __init__(self, screen, list_of_contents):
        self.margin = 10
        self.padding = 5
        self.radius = 5
        self.pos_x, self.pos_y = self.margin, self.margin
        self.width = screen.get_width() - 2 * self.margin
        self.height = self.padding  # to accumulate, not is only this value
        self.color_fill = 'gray'
        self.list_unit_card = []
        self.screen = screen

        # ---------------- generate list of unit cards for show on the package -------------------------
        x_unit_card = self.pos_x + self.padding
        y_unit_card = self.pos_y + self.padding
        width_unit_card = self.width - 2 * self.padding

        # --------------- style for title - description ------------------------------------
        size_title = 27
        color_title = 'gray'
        color_card_title = 'orange'

        size_description = 20
        color_description = 'black'
        color_card_description = 'dark gray'

        for dict_content in list_of_contents:
            unit_card = UnitCard(self.screen, x_unit_card, y_unit_card, width_unit_card, dict_content,
                                 size_title, color_title, color_card_title, size_description,
                                 color_description, color_card_description)
            self.list_unit_card.append(unit_card)
            self.height += unit_card.height_unit_card + self.padding
            y_unit_card += unit_card.height_unit_card + self.padding

        # ---------------- generate list of unit cards for show on the package -------------------------

    def show(self):
        # show a rect package
        rect(self.screen, self.color_fill, (self.pos_x, self.pos_y, self.width, self.height), border_radius=self.radius)

        # show card units
        for unit_card in self.list_unit_card:
            # unit_card.calculate_pos()
            if -unit_card.height_unit_card < unit_card.pos_y_unit_card < self.screen.get_width():
                unit_card.show()


class StateRule(BasicState):
    def __init__(self, screen):
        BasicState.__init__(self, screen)
        self.background_color = 'red'

        self.package_view_description = PackageCardDescription(screen, description_for_objects)

    def run(self):
        while not self.class_for_return:
            # fill all windows with a color
            self.screen.fill(self.background_color)

            self.package_view_description.show()

            # manager of events
            for event in get_queue_event():
                if event.type == QUIT:
                    self.class_for_return = EXIT_PROGRAM

            flip()
            self.clock.tick(self.FPS)

        return self.class_for_return
