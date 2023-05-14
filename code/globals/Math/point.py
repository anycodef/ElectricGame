from random import uniform
from turtle import onkey


class Point:
    def __init__(self, x=0, y=0):
        self.point = [x, y]
        self.history_points = []
        self.fixed_points = True

    def choose_other_point_random(self, radio, only_return=False):
        new_point = [None, None]

        for i in range(2):
            new_point[i] = uniform(self.point[i] + radio, self.point[i] - radio)

        if only_return:
            return new_point
        else:
            self.history_points.append(self.point)
            self.point = new_point

    def assign(self, other):
        if isinstance(other, list):
            self.point = other
        elif isinstance(other, Point):
            self.point = other.point

    def is_equal(self, other) -> bool:
        if isinstance(other, Point):
            is_equal_value = self.point == other.point
        else:
            is_equal_value = False

        return is_equal_value



