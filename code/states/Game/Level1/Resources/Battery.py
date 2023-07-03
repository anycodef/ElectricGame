from code.globals.constanst import path_root_project, join
from pygame import Rect
from pygame.image import load


class AbstractBattery:
    level_of_battery = 100


class ModifierPercentageCharge:
    @staticmethod
    def increase_level_battery():
        if AbstractBattery.level_of_battery < 100:
            AbstractBattery.level_of_battery += 5

    @staticmethod
    def decrease_level_battery():
        if AbstractBattery.level_of_battery > 0:
            AbstractBattery.level_of_battery -= 5


class BatteryGui:
    rect = Rect(20, 0, 0, 0)


class Gui(BatteryGui):
    def __init__(self, screen):
        self.__screen = screen

        self.__n_sprites = 7
        self.__sprite = [load(join(path_root_project, 'src', 'batteryStatus',
                                   f'battery{i}.png')) for i in range(self.__n_sprites)]

        self.__range_img = 100 / self.__n_sprites

        BatteryGui.rect.width = self.__sprite[0].get_width()
        BatteryGui.rect.height = self.__sprite[0].get_height()

    def show(self):
        self.__screen.blit(self.__sprite[int(AbstractBattery.level_of_battery / self.__range_img) - 1],
                           (BatteryGui.rect.x, BatteryGui.rect.y))


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
