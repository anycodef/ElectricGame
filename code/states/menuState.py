from pygame.display import flip
from pygame.event import get as get_event
from pygame import QUIT

from code.widgets.buttons import ButtonManager
from code.globals.generalState import BasicState

from pygame.image import load as load_img
from code.globals.constanst import path_root_project

# test --------------------------------------
from code.globals.Effects.arcVoltaic import ArcVoltaic
from code.globals.Math.point import Point
from code.globals.Math.coordinateSystem import CoordSys
from random import randint
from pygame.mouse import get_pos
from pygame.transform import scale
# test --------------------------------------


# This state define an interface where
class MenuState(BasicState):
    def __init__(self, screen):
        BasicState.__init__(self, screen)

        # style general button
        self.list_text_and_status = [["Play", ['executeState', "GameStateLevels"]],
                                     ["Rules", ['executeState', "RuleState"]],
                                     ["Exit", ['exitProgram', None]]]

        self.color_text = "white"
        self.color_selected = "blue"
        self.size_text = 30

        # buttons - manager
        self.managerButtons = ButtonManager(self.list_text_and_status, self.color_text, self.color_selected, self.size_text, self.screen)
        self.managerButtons.init_buttons()

        # test --------------------------------------
        self.arc1 = ArcVoltaic(self.screen)
        self.coord = CoordSys(self.screen.get_width(), self.screen.get_height())
        # test --------------------------------------

    def run(self) -> list:

        # main while of this state
        while not self.exitState:

            # Give a color to background of the menu in this case black
            self.screen.fill(self.background_color)

            # show buttons
            state_selected = self.managerButtons.run()
            if state_selected:  # check whether a button is selected and therefore is returned a list
                self.list_for_return = state_selected
                self.exitState = True

            # test --------------------------------------
            self.arc1.show(2, endpoint1=Point(x=-100, y=100), endpoint2=Point(*self.coord.coord_pygame_to_coord_system(*get_pos())), radio=randint(10, 40), intensity=randint(1, 3))
            # test --------------------------------------

            self.screen.blit(self.image_cable_left_bottom, (10, 10))

            # manage an event under the menu state
            for event in get_event():
                if event.type == QUIT:
                    self.exitState = True
                    self.list_for_return = ['exitProgram', None]

            flip()
            self.clock.tick(self.FPS)

        return self.list_for_return
