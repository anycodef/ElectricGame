from code.globals.constanst import path_root_project, join
from pygame.image import load


def load_images_get_position(width_parent, height_parent):
    x = -300
    y = height_parent - 320

    img = load(join(path_root_project, 'src', 'platform', 'typePlatform1.png'))
    list_img = []
    list_pos = []

    while x <= width_parent:
        list_pos.append([x, y])
        img.get_rect().x = x
        list_img.append(img)
        x += 320

    return list_img, list_pos


class AbstractClassPlatform:
    position_blocks = []

    def __init__(self):
        self.width_block = 331


class MechanicsPlatform(AbstractClassPlatform):
    def __init__(self):
        AbstractClassPlatform.__init__(self)
        self.__speed = -10

    def __check_position(self):
        first_block_position = AbstractClassPlatform.position_blocks[0]

        if first_block_position[0] + self.width_block < 0:
            AbstractClassPlatform.position_blocks.remove(first_block_position)
            first_block_position[0] = AbstractClassPlatform.position_blocks.copy().pop()[0] + self.width_block - 11
            AbstractClassPlatform.position_blocks.append(first_block_position)

    def move(self):
        for index in range(AbstractClassPlatform.position_blocks.__len__()):
            AbstractClassPlatform.position_blocks[index][0] += self.__speed
        self.__check_position()


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
        self.__mechanics = MechanicsPlatform()
        self.__gui = GuiPlatform(screen)

    def run(self):
        self.__mechanics.move()
        self.__gui.show()



