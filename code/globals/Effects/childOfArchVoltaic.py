from ..constanst import path_root_project
from pygame.image import load as load_img
from pygame.transform import scale

from .arcVoltaic import ArcVoltaic
from random import randint, uniform
from ..Math.point import Point

from pygame.mouse import get_pos
from ..Math.coordinateSystem import CoordSys


class CableWithArcVoltaicForMenu:
    def __init__(self, screen):
        # original image
        self.image_cable_right_top = load_img(f'{path_root_project}\\src\\menuImg\\cable-right-top.png')
        self.pos_relative_end_cable_right_top = [[218, 3], [294, 23], [253, 108]]

        self.image_cable_left_bottom = load_img(f'{path_root_project}\\src\\menuImg\\cable-left-bottom.png')
        self.pos_relative_end_cable_left_bottom = [[140, 400], [66, 372], [4, 296]]

        self.size_image = self.image_cable_left_bottom.get_size()

        # scale image
        self.scale_factor = 0.5

        # to scale
        self.size_image_scale = [dimension * self.scale_factor for dimension in self.image_cable_left_bottom.get_size()]

        self.image_cable_right_top_scale = scale(self.image_cable_right_top, self.size_image_scale)
        self.pos_end_cable_right_top_scale = []
        for pos in self.pos_relative_end_cable_right_top:
            for w, h in pos:
                self.pos_end_cable_right_top_scale.append([w * self.scale_factor, h * self.scale_factor])

        self.image_cable_left_bottom_scale = scale(self.image_cable_left_bottom, self.size_image_scale)
        self.pos_end_cable_left_bottom_scale = []
        for pos in self.pos_relative_end_cable_left_bottom:
            for w, h in pos:
                self.pos_end_cable_left_bottom_scale.append([w * self.scale_factor, h * self.scale_factor])

        # absolute position of cables and image
        self.pos_pygame_image_cable_right_top = [screen.get_width() - self.size_image_scale[0], self.size_image_scale[1]]
        self.pos_pygame_image_cable_left_bottom = [self.size_image_scale[0], screen.get_height() - self.size_image_scale[1]]

        self.pos_absolute_pygame_end_cable_right_top = []     # use it for an initial position of cables
        for pos in self.pos_end_cable_right_top_scale:
            for w, h in pos:
                self.pos_absolute_pygame_end_cable_right_top.append(
                    [w + self.pos_pygame_image_cable_right_top[0], h + self.pos_pygame_image_cable_right_top[1]])

        self.pos_absolute_pygame_end_cable_left_bottom = []     # use it for an initial position of cables
        for pos in self.pos_end_cable_left_bottom_scale:
            for w, h in pos:
                self.pos_absolute_pygame_end_cable_left_bottom.append(
                    [w + self.pos_pygame_image_cable_left_bottom[0], h + self.pos_pygame_image_cable_left_bottom[1]])

        # arc voltaic
        self.arc_voltaic_cable_right_top = [ArcVoltaic(screen) for i in range(3)]
        self.arc_voltaic_cable_left_bottom = [ArcVoltaic(screen) for i in range(3)]

        # system coordinate
        self.coord_system = CoordSys(screen.get_width(), screen.get_height())

    def run(self):
        # show arcs voltaic
        for arc, pos_initial in \
            list(zip(self.arc_voltaic_cable_left_bottom + self.arc_voltaic_cable_right_top,
                     self.pos_absolute_pygame_end_cable_left_bottom + self.pos_absolute_pygame_end_cable_right_top)):
            arc.show(number_intermediate_points=randint(1, 5),
                     endpoint1=Point(*self.coord_system.coord_pygame_to_coord_system(*get_pos())),
                     endpoint2=Point(*self.coord_system.coord_pygame_to_coord_system(*pos_initial)),
                     radio=randint(5, 20), intensity=randint(1, 4))







