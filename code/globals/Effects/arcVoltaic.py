from pygame.draw import lines
from ..Math.point import Point
from ..Math.vect2d import Vect2d
from ..Math.coordinateSystem import CoordSys

from random import choice


class ArcVoltaic:
    def __init__(self, screen):

        # surface
        self.__screen = screen

        # math
        self.__endpoint1 = Point()
        self.__endpoint2 = Point()

        self.__turning_points = []

        # style
        self.__list_color = ["light blue", "blue", "orange", "green"]

        # layout coordinate system
        self.__layout_coord_system = CoordSys(self.__screen.get_width(), self.__screen.get_height())

    def show(self, number_intermediate_points, endpoint1: Point, endpoint2: Point, radio=10, intensity=1):

        # find intermediate points
        if not self.__endpoint1.is_equal(other=endpoint1) or not self.__endpoint2.is_equal(other=endpoint2):
            self.__turning_points.clear()
            vector_intermediate = Vect2d()
            vector_intermediate.gen_vector(point1=endpoint1.point, point2=endpoint2.point)
            vector_intermediate.scalar_mul(scalar=1/(number_intermediate_points + 1))

            self.__endpoint1.assign(endpoint1)
            self.__endpoint2.assign(endpoint2)

            i_point = endpoint1
            for i in range(number_intermediate_points):
                e_point = Point(*vector_intermediate.find_end_point(initial_point=i_point.point))
                e_point.fixed_points = False
                self.__turning_points.append(e_point)

                i_point = e_point
                del e_point

            del vector_intermediate

        points_for_draw = [self.__layout_coord_system.coord_system_to_coord_pygame(*self.__endpoint1.point)]
        for point in self.__turning_points:
            point_intermediate_list = point.choose_other_point_random(radio=radio, only_return=True)
            points_for_draw.append(self.__layout_coord_system.coord_system_to_coord_pygame(*point_intermediate_list))
        points_for_draw.append(self.__layout_coord_system.coord_system_to_coord_pygame(*self.__endpoint2.point))

        # draw the linea with points on surface screen
        lines(self.__screen, choice(self.__list_color), closed=False, points=points_for_draw, width=intensity)
