from pygame.image import load
from pygame.transform import scale

from code.globals.constanst import path_root_project, join


def scale_images(list_images: list, width: int):
    height = width / list_images[0].get_width() * list_images[0].get_height()

    for index_image in range(list_images.__len__()):
        list_images[index_image] = scale(list_images[index_image], (width, height))


class Battery:
    def __init__(self, screen):
        self.__screen = screen

        self.__width = 200
        self.__list_img_battery = [load(join(path_root_project, 'src', 'batteryStatus', f'battery{i}.png'))
                                   for i in range(7)]
        scale_images(self.__list_img_battery, self.__width)

        self.__index_image = 0
        self.add = 1

        self.complete = False
        self.void = False

    def add_charge(self):
        if self.__index_image != self.__list_img_battery.__len__() - 1:
            self.__index_image += 1

    def less_charge(self):
        if self.__index_image != 0:
            self.__index_image -= 1

    def __listen_state_battery(self):
        pass

    def run(self):
        self.__screen.blit(self.__list_img_battery[self.__index_image], (100, 100))



