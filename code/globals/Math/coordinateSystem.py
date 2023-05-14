

class CoordSys:
    def __init__(self, width_windows, height_windows):
        # windows setting
        self.width_windows = width_windows
        self.height_windows = height_windows
        self.percentage_y_positive_axes = .5

    def coord_system_to_coord_pygame(self, x, y) -> list[float, float]:
        pygame_x = x + self.width_windows * 0.5
        pygame_y = y + self.height_windows * self.percentage_y_positive_axes

        return [pygame_x, pygame_y]



