from code.globals.generalState import BasicState

from pygame.event import get as get_queue_event
from pygame import KEYUP, KEYDOWN, K_UP, K_DOWN

from pygame.draw import rect
from pygame import QUIT
from pygame.display import flip

from code.widgets.text import CardText
from code.widgets.images import CardImg

# constants
from code.globals.constanst import EXIT_PROGRAM, description_for_objects

# states for sidebar
from code.states.Game.stateGameLevels import StateGameLevels


class UnitCard:
    def __init__(self, screen, x_unit_card, y_unit_card, width_card, content: dict, size_title,
                 color_title, color_card_title, size_description, color_description, color_card_description):
        self.screen = screen
        self.content = content

        # ------------------------------------- unit card ---------------------------------------
        self.pos_x_unit_card = x_unit_card
        self.pos_y_unit_card = y_unit_card
        self.color_fill_background = 'black'
        self.width_unit_card = width_card
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
        self.pos_x_description_part = self.pos_x_title_part
        self.width_title_and_description_part = \
            self.proportion_width_of_title_description_part * self.width_content_part
        # ------------------------------------- title - description part ---------------------------------------

        # ------------------------------------- title - object ---------------------------------------------
        self.card_title = CardText(self.screen, self.pos_x_title_part, self.pos_y_title_part,
                                   self.width_title_and_description_part,
                                   color_card_title, self.content['name'], size_title, color_title)
        self.height_title_card = self.card_title.height_card
        self.pos_y_description_part = self.pos_y_title_part + self.height_title_card + self.padding

        self.size_title = size_title
        self.color_title = color_title
        self.color_card_title = color_card_title
        # ------------------------------------- title - object ---------------------------------------------
        # ------------------------------------- description - object ---------------------------------------------
        self.card_description = CardText(self.screen, self.pos_x_description_part, self.pos_y_description_part,
                                         self.width_title_and_description_part,
                                         color_card_description, self.content['description'], size_description,
                                         color_description)
        self.height_description_card = self.card_description.height_card
        self.height_img_part = self.height_title_card + self.padding + self.height_description_card
        self.height_unit_card = self.height_img_part + 2 * self.padding
        # ------------------------------------- description - object ---------------------------------------------
        # ------------------------------------- card image - object ---------------------------------------------
        self.card_img = CardImg(self.screen, self.pos_x_img_part, self.pos_y_img_part,
                                content['image']['filename'], self.width_img_part, self.height_img_part)
        # ------------------------------------- card image - object ---------------------------------------------
        # ------------------------------------- list parts - object ---------------------------------------------
        self.list_parts_of_unit_card = [self.card_img, self.card_title, self.card_description]

    def set_pos(self, speed_y):
        if speed_y:
            self.pos_y_unit_card += speed_y

            for obj_part in self.list_parts_of_unit_card:
                # set pos
                obj_part.set_pos(speed_y)

    def show(self):
        # show a rect of background
        rect(self.screen, self.color_fill_background,
             (self.pos_x_unit_card, self.pos_y_unit_card, self.width_unit_card, self.height_unit_card),
             border_radius=self.radius)

        for obj_part in self.list_parts_of_unit_card:
            # show part
            if -obj_part.height_card < obj_part.y_card < self.screen.get_height():
                obj_part.show()


class PackageCardDescription:
    def __init__(self, screen, list_of_contents):
        self.screen = screen

        self.margin = 10
        self.padding = 5
        self.radius = 5

        self.pos_x, self.pos_y = self.margin, self.margin
        self.width = self.screen.get_width() - 2 * self.margin
        self.height = self.padding  # to accumulate, not is only this value

        self.color_fill = 'gray'
        self.list_unit_card = []

        # ---------------- generate list of unit cards for show on the package -------------------------
        x_unit_card = self.pos_x + self.padding
        y_unit_card = self.pos_y + self.padding
        width_unit_card = self.width - 2 * self.padding

        # --------------- style for title - description ------------------------------------
        size_title = 27
        color_title = 'black'
        color_card_title = 'orange'

        size_description = 15
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

    def show(self, component_speed_y=0):
        # show a rect package
        if component_speed_y:
            if self.pos_y + self.height <= self.screen.get_height() - self.margin and component_speed_y < 0:
                component_speed_y = 0
                self.pos_y = self.screen.get_height() - self.margin - self.height
            elif self.pos_y >= self.margin and component_speed_y > 0:
                component_speed_y = 0
                self.pos_y = self.margin

        if component_speed_y:
            self.pos_y += component_speed_y

        rect(self.screen, self.color_fill, (self.pos_x, self.pos_y, self.width, self.height), border_radius=self.radius)

        # show card units
        for unit_card in self.list_unit_card:
            unit_card.set_pos(component_speed_y)
            if -unit_card.height_unit_card < unit_card.pos_y_unit_card < self.screen.get_width():
                unit_card.show()


class StateRule(BasicState):
    def __init__(self, screen, obj_exchanger_interface):
        BasicState.__init__(self, screen)

        self.__list_text_and_status = [['Levels', StateGameLevels],
                                       ['Exit', EXIT_PROGRAM]]

        self.__obj_exchanger_interface = obj_exchanger_interface
        self.__obj_exchanger_interface.set_gui_sidebar()
        self.__obj_exchanger_interface.set_option_available_on_state(self.__list_text_and_status)

        self.__background_color = '#E8AA42'

        self.__package_view_description = PackageCardDescription(screen, description_for_objects)

        self.__speed_y = 0

    def run(self):
        while not self.list_class_obj_return:
            # fill all windows with a color
            self.screen.fill(self.__background_color)

            # execute all cards of description
            self.__package_view_description.show(self.__speed_y)

            # execute sideBar
            self.__obj_exchanger_interface.run()
            # get list [class, obj] for return
            self.list_class_obj_return = self.__obj_exchanger_interface.get_list_class_obj()

            # manager of events
            for event in get_queue_event():
                if event.type == QUIT:
                    self.list_class_obj_return = [EXIT_PROGRAM, None]
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.__speed_y = 4
                    if event.key == K_DOWN:
                        self.__speed_y = -4
                if event.type == KEYUP:
                    self.__speed_y = 0

            flip()
            self.clock.tick(self.FPS)

        return self.list_class_obj_return
