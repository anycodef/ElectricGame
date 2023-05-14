
class Vect2d:
    def __init__(self, x=0, y=0):
        self.vector = [x, y]
        self.history_of_vector = []

    def gen_vector(self, point1: list, point2: list):
        """
        For this compute is considered the vector point1->point2
        :param point1: initial point
        :param point2: end point
        :return: None
        """
        if not self.vector:
            self.history_of_vector.append(self.vector)

        for i in range(2):
            self.vector[i] = point2[i] - point1[i]

    def __add__(self, other):
        result_vector = [None, None]
        for i in range(2):
            result_vector[i] = self.vector[i] + other.vector[i]
        return Vect2d(result_vector[0], result_vector[1])

    def __sub__(self, other):
        result_vector = [None, None]
        for i in range(2):
            result_vector[i] = self.vector[i] - other.vector[i]
        return Vect2d(result_vector[0], result_vector[1])

    def dot_product(self, other):
        result_int = 0
        for i in range(2):
            result_int += self.vector[i] * other.vector[i]
        return result_int

    def find_initial_point(self, end_point: list[float, float]) -> list[float, float]:
        initial_point = [None, None]
        for i in range(2):
            initial_point[i] = self.vector[i] + end_point[i]

        return initial_point

    def find_end_point(self, initial_point: list[float, float]) -> list[float, float]:
        end_point = [None, None]
        for i in range(2):
            end_point[i] = self.vector[i] + initial_point[i]

        return end_point

    def scalar_mul(self, scalar: float, only_return=False):

        new_vector = self.vector
        for i in range(2):
            new_vector[i] *= scalar

        if only_return:
            return new_vector
        else:
            self.history_of_vector.append(self.vector)
            self.vector = new_vector


