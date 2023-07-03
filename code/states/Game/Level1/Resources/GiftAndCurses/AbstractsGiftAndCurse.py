from code.states.Game.Level1.Resources.Character import AbstractGeneralCharacter
from code.states.Game.Level1.Resources.Platform import AbstractClassPlatform
from random import randint

from pygame.image import load


class AbstractMechanics:
    def __init__(self, screen_width, rect_img):
        self.__rect = rect_img
        self.__rect.x = screen_width + 200
        self.__screen_width = screen_width

        self.__collision = False
        self.re_position = False

    def is_collision(self):
        return self.__collision

    def end_collision(self):
        self.__collision = False

    def __move(self):
        if self.__rect.x + self.__rect.width > 0 and not self.re_position:
            self.__rect.x += AbstractClassPlatform.speed
        else:
            self.__rect.x = randint(self.__screen_width + 100, self.__screen_width + 8000)
            self.re_position = False

    def __listen_for_collision(self):
        if self.__rect.x < AbstractGeneralCharacter.x < self.__rect.x + self.__rect.width or self.__rect.x <\
                AbstractGeneralCharacter.x + AbstractGeneralCharacter.width < self.__rect.x + self.__rect.width:
            if self.__rect.y < AbstractGeneralCharacter.y + AbstractGeneralCharacter.height - 30:
                self.__collision = True
                self.re_position = True

    def get_rect(self):
        return self.__rect

    def run(self):
        self.__listen_for_collision()
        self.__move()


class AbstractGui:
    def __init__(self, screen, path_img):
        self.__screen = screen
        self.__img = load(path_img)
        self.__rect = self.__img.get_rect()
        self.__rect.y = AbstractClassPlatform.y - self.__img.get_height()

    def get_rect(self):
        return self.__rect

    def update_rect(self, new_rect):
        self.__rect = new_rect

    def show(self):
        self.__screen.blit(self.__img, (self.__rect.x, self.__rect.y))


class AbstractGiftCurse:
    def __init__(self, screen, path_img):
        self.__gui = AbstractGui(screen, path_img)
        self.__mechanics = AbstractMechanics(screen.get_width(), self.__gui.get_rect())

    def is_collision(self):
        return self.__mechanics.is_collision()

    def end_collision(self):
        self.__mechanics.end_collision()

    def get_rect(self):
        return self.__mechanics.get_rect()

    def set_reposition(self, value):
        self.__mechanics.re_position = value

    def run(self):
        self.__gui.update_rect(self.__mechanics.get_rect())
        self.__gui.show()
        self.__mechanics.run()


