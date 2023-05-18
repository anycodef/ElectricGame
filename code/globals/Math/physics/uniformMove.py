
from code.globals.Math.vect2d import Vect2d
from code.globals.Math.point import distance_between_two_points


class UniformMove:
    def __init__(self, pos_end, pos_init, time):

        self.FPS = 60

        # define a vector for represent a speed vector
        self.vect_speed = Vect2d()
        # find a displacement vector
        self.vect_speed.gen_vector(point1=pos_init, point2=pos_end)
        # find a constant velocity vector
        self.vect_speed.scalar_mul(1/(self.FPS * time))

        # set a current position as pos_init value and the end pos as pos_end value
        self.current_pos = pos_init
        self.end_pos = pos_end

    # apply a sum of vector with constant velocity vector
    def run(self) -> list:

        # This sum will happen if and only if a position point is close to end position
        if distance_between_two_points(self.current_pos, self.end_pos) <= self.vect_speed.module():
            self.current_pos = self.end_pos
        else:
            self.current_pos = (self.vect_speed + Vect2d(*self.current_pos)).vector

        # return a new current position for use it
        return self.current_pos

