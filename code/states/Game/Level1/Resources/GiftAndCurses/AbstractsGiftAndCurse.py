from code.states.Game.Level1.Resources.Character import AbstractGeneralCharacter
from code.states.Game.Level1.Resources.Platform import AbstractClassPlatform
from random import randint

from pygame.image import load


class AbstractMechanics:
    def __init__(self, screen_width, rect_img):
        self.__rect = rect_img
        self.__rect.x = screen_width - 200
        self.__screen_width = screen_width

        self.__collision = False

    def __move(self):
        if self.__rect.x - self.__rect.width < 0 and not self.__collision:
            self.__rect.x += AbstractClassPlatform.speed
        else:
            self.__rect.x = randint(self.__screen_width + 100, self.__screen_width + 400)
            self.__collision = False

    def __listen_for_collision(self):
        self.__collision = AbstractGeneralCharacter.rect_character.colliderect(self.__rect)

    def run(self):
        self.__move()
        self.__listen_for_collision()


class AbstractGui:
    def __init__(self, screen, path_img):
        self.__screen = screen
        self.__img = load(path_img)

        self.__img.get_rect().y = AbstractClassPlatform.y - self.__img.get_height()

    def get_rect(self):
        return self.__img.get_rect()

    def show(self):
        self.__screen.blit(self.__img, (self.__img.get_rect().x, self.__img.get_rect().y))


class AbstractGiftCurse:
    def __init__(self, screen, path_img):
        self.__gui = AbstractGui(screen, path_img)
        self.__mechanics = AbstractMechanics(screen.get_width(), self.__gui.get_rect())
