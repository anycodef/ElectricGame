from code.globals.constanst import path_root_project, join
from pygame import Rect
from pygame.image import load

from pygame.font import SysFont

from math import ceil


class AbstractBattery:
    level_of_battery = 100


class ModifierPercentageCharge:
    @staticmethod
    def increase_level_battery(step=5):
        AbstractBattery.level_of_battery += step

        if AbstractBattery.level_of_battery > 100:
            AbstractBattery.level_of_battery = 100

    @staticmethod
    def decrease_level_battery(step=-5):
        AbstractBattery.level_of_battery += step

        if AbstractBattery.level_of_battery < 0:
            AbstractBattery.level_of_battery = 0


class BatteryGui:
    rect = Rect(20, 0, 0, 0)


class LetterLevelBattery:
    def __init__(self, screen):
        self.__screen = screen

        self.__size = 20
        self.__color = 'white'
        self.__font = 'arial'

        self.__margin = 10

        self.__sysFont = SysFont(self.__font, self.__size)
        self.__text_level_battery = f'{ceil(AbstractBattery.level_of_battery)} %'
        self.__img = self.__sysFont.render(self.__text_level_battery, False, self.__color)

        self.__x_relative = (BatteryGui.rect.width - self.__img.get_width()) / 2
        self.__y_relative = BatteryGui.rect.height + self.__margin

    def __render_text(self):
        self.__text_level_battery = f'{ceil(AbstractBattery.level_of_battery)} %'
        self.__img = self.__sysFont.render(self.__text_level_battery, False, self.__color)

        self.__x_relative = (BatteryGui.rect.width - self.__img.get_width()) / 2
        self.__y_relative = BatteryGui.rect.height + self.__margin

    def __show(self):
        self.__screen.blit(self.__img, (BatteryGui.rect.x + self.__x_relative, BatteryGui.rect.y + self.__y_relative))

    def run(self):
        self.__render_text()
        self.__show()


class Gui(BatteryGui):
    def __init__(self, screen):
        self.__screen = screen

        self.__n_sprites = 8
        self.__sprite = [load(join(path_root_project, 'src', 'batteryStatus',
                                   f'battery{i}.png')) for i in range(self.__n_sprites)]

        self.__card_level = LetterLevelBattery(screen)

        self.__range_img = 100 / (self.__n_sprites - 1)

        BatteryGui.rect.width = self.__sprite[0].get_width()
        BatteryGui.rect.height = self.__sprite[0].get_height()

    def show(self):

        self.__screen.blit(self.__sprite[int(AbstractBattery.level_of_battery / self.__range_img)],
                           (BatteryGui.rect.x, BatteryGui.rect.y))

        self.__card_level.run()


class Mechanics(BatteryGui):
    def __init__(self, screen_height):
        self.__space_button_top = 100
        self.__floor_top = screen_height - self.__space_button_top - BatteryGui.rect.height

        BatteryGui.rect.y = self.__floor_top - (self.__floor_top -
                                                self.__space_button_top) * AbstractBattery.level_of_battery / 100

    def run(self):
        BatteryGui.rect.y = self.__floor_top - (self.__floor_top -
                                                self.__space_button_top) * AbstractBattery.level_of_battery / 100


class Battery:
    def __init__(self, screen):
        self.__gui = Gui(screen)
        self.__mechanics = Mechanics(screen.get_rect().height)

    def run(self):
        self.__gui.show()
        self.__mechanics.run()

    def __del__(self):
        AbstractBattery.level_of_battery = 100
        BatteryGui.rect = Rect(20, 0, 0, 0)
