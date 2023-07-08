from code.states.Game.Level1.Resources.Platform import AbstractClassPlatform
from code.states.Game.Level1.Resources.Character import AbstractGeneralCharacter

from code.states.Game.Level1.Resources.weapon import AbstractArcVoltaicWeaponCollision

from pygame.image import load
from random import randint


class Mechanics:
    def __init__(self, rect, width_screen):
        self.__rect = rect
        self.__width_screen = width_screen

        self.__all_shoot = 5
        self.__shoot_count = 0

        self.__re_position = False
        self.__collision = False  # with character

    def __listen_for_collision(self):
        if self.__rect.x < AbstractGeneralCharacter.x < self.__rect.x + self.__rect.width or \
                self.__rect.x < AbstractGeneralCharacter.x + AbstractGeneralCharacter.width < \
                self.__rect.x + self.__rect.width:
            self.__collision = True
            self.__re_position = True

    def __is_out_screen(self):
        if AbstractClassPlatform.direction == 'left':
            return self.__rect.x + self.__rect.width > 0
        else:
            return self.__rect.x < self.__width_screen

    def __position(self):
        if AbstractClassPlatform.direction == 'left':
            # self.__rect.x = randint(self.__width_screen + 10000, self.__width_screen + 100000)
            self.__rect.x = randint(self.__width_screen + 1000, self.__width_screen + 10000)
        else:
            # self.__rect.x = randint(-100, -10)
            self.__rect.x = randint(-10000, -1000)

    def __move(self):
        if self.__is_out_screen() and not self.__re_position:
            self.__rect.x += AbstractClassPlatform.speed

            if self.listen_fired not in AbstractArcVoltaicWeaponCollision.list_function_shoot:
                AbstractArcVoltaicWeaponCollision.list_function_shoot.append(self.listen_fired)

        else:
            self.__position()
            self.__re_position = False

    def listen_fired(self):  # add to the list_collision_weapon
        if self.__shoot_count == self.__all_shoot:
            self.__re_position = True
            self.__shoot_count = 0
        else:
            self.__shoot_count += 1

        return [self.__rect.x, self.__rect.y]

    def is_collision(self):
        return self.__collision

    def end_collision(self):
        self.__collision = False

    def get_rect(self):
        return self.__rect

    def run(self):
        self.__move()
        self.__listen_for_collision()


class Graphics:
    def __init__(self, screen, pathfile):
        self.__screen = screen
        self.__img = load(pathfile)
        self.__rect = self.__img.get_rect()
        self.__rect.y = AbstractClassPlatform.y - self.__img.get_height() + 10

    def get_rect(self):
        return self.__rect

    def update_rect(self, new_rect):
        self.__rect = new_rect

    def show(self):
        self.__screen.blit(self.__img, (self.__rect.x, self.__rect.y))


class Portal:
    def __init__(self, screen, pathfile):
        self.__graphics = Graphics(screen, pathfile)
        self.__mechanics = Mechanics(self.__graphics.get_rect(), screen.get_width())

    def is_collision(self):
        return self.__mechanics.is_collision()

    def end_collision(self):
        self.__mechanics.end_collision()

    def run(self):
        self.__mechanics.run()
        self.__graphics.update_rect(self.__mechanics.get_rect())
        self.__graphics.show()
