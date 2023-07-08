from code.globals.constanst import path_root_project, join
from pygame.image import load

from code.states.Game.Level1.Resources.Portals.AbstractPortalVerticalHorizontal import *

from code.states.Game.Level1.Resources.Battery import AbstractBattery


class AbstractClassPlatform:
    y = 0
    position_blocks = []
    speed = -10

    directions = {-1: 'left',
                  1: 'right'}
    key_direction = -1
    direction = directions[key_direction]

    def __init__(self):
        self.width_block = 331

    @staticmethod
    def affect_vertical_portal():
        AbstractClassPlatform.speed *= -1
        AbstractClassPlatform.key_direction *= -1
        AbstractClassPlatform.direction = AbstractClassPlatform.directions[AbstractClassPlatform.key_direction]


def load_images_get_position(width_parent, height_parent):
    x = -300
    y = height_parent - 320
    AbstractClassPlatform.y = height_parent - 320

    img = load(join(path_root_project, 'src', 'platform', 'typePlatform1.png'))
    list_img = []
    list_pos = []

    while x <= width_parent:
        list_pos.append([x, y])
        img.get_rect().x = x
        list_img.append(img)
        x += 320

    return list_img, list_pos


class MechanicsPlatform(AbstractClassPlatform):
    def __init__(self, width_screen):
        AbstractClassPlatform.__init__(self)
        AbstractPortalVertical.list_method_of_the_object_affect.append(AbstractClassPlatform.affect_vertical_portal)

        self.__width_screen = width_screen

        self.__check_position = {
            'right': self.__check_position_right,
            'left': self.__check_position_left
        }

    def __check_position_left(self):
        first_block_position = AbstractClassPlatform.position_blocks[0]

        if first_block_position[0] + self.width_block < 0:
            AbstractClassPlatform.position_blocks.remove(first_block_position)
            first_block_position[0] = AbstractClassPlatform.position_blocks.copy().pop()[0] + self.width_block - 11
            AbstractClassPlatform.position_blocks.append(first_block_position)

    def __check_position_right(self):
        last_block_position = AbstractClassPlatform.position_blocks.copy().pop()

        if last_block_position[0] > self.__width_screen:
            AbstractClassPlatform.position_blocks.remove(last_block_position)
            last_block_position[0] = AbstractClassPlatform.position_blocks[0][0] - self.width_block + 11
            AbstractClassPlatform.position_blocks = [last_block_position] + AbstractClassPlatform.position_blocks

    def move(self):
        for index in range(AbstractClassPlatform.position_blocks.__len__()):
            AbstractClassPlatform.position_blocks[index][0] += AbstractClassPlatform.speed
        self.__check_position[AbstractClassPlatform.direction]()

    @staticmethod
    def GameOver():
        AbstractClassPlatform.speed = 0


class GuiPlatform(AbstractClassPlatform):
    def __init__(self, screen):
        AbstractClassPlatform.__init__(self)
        self.__screen = screen

        self.__list_img, AbstractClassPlatform.position_blocks = \
            load_images_get_position(screen.get_width(), screen.get_height())

    def show(self):
        for img_block, pos in list(zip(self.__list_img, AbstractClassPlatform.position_blocks)):
            self.__screen.blit(img_block, pos)


class Platform:
    def __init__(self, screen):
        self.__mechanics = MechanicsPlatform(screen.get_width())
        self.__gui = GuiPlatform(screen)

    def run(self):
        self.__mechanics.move()
        self.__gui.show()

        if AbstractBattery.level_of_battery == 0:
            self.__mechanics.GameOver()

    def __del__(self):
        AbstractClassPlatform.y = 0
        AbstractClassPlatform.position_blocks = []
        AbstractClassPlatform.speed = -10
        AbstractClassPlatform.directions = {-1: 'left',
                                           1: 'right'}
        AbstractClassPlatform.key_direction = -1
        AbstractClassPlatform.direction = AbstractClassPlatform.directions[AbstractClassPlatform.key_direction]
