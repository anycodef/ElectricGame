from pygame.image import load
from code.globals.constanst import join, path_root_project

from pygame import KEYDOWN, KEYUP, K_SPACE


class Weapon:
    def __init__(self, screen):
        self.__screen = screen

        self.__img = {}
        self.__X_RELATIVE = {
            'left': 2,
            'right': 17
        }
        self.__Y_RELATIVE = 46

        # effect shooting
        self.__x, self.__y = 0, 0
        self.__x_shoot = 0
        self.__x_shooting = 5

        self.__shooting = False

        # load default images
        self.load_weapon()

    def load_weapon(self, name='weapon1'):
        self.__img.clear()
        for direction in ['right', 'left']:
            self.__img.__setitem__(direction, load(join(path_root_project, 'src', 'weapon', f'{name}-{direction}.png')))

    def manage_events(self, queue_event):
        for event in queue_event:
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.__shooting = not self.__shooting
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    self.__shooting = not self.__shooting

    def __update_position(self, x_character, y_character, current_direction):
        self.__x = x_character + self.__X_RELATIVE[current_direction]
        self.__y = y_character + self.__Y_RELATIVE

    def __shoot(self):
        if self.__shooting:
            if self.__x_shoot == self.__x_shooting:
                self.__x_shoot = -self.__x_shooting
            else:
                self.__x_shoot += self.__x_shooting
        else:
            self.__x_shoot = 0

    def __show(self, current_direction):
        self.__screen.blit(self.__img[current_direction], (self.__x + self.__x_shoot, self.__y))

    def run(self, x_character, y_character, current_direction, state):
        if 'toBendDown' not in state:
            self.__update_position(x_character, y_character, current_direction)
            self.__shoot()
            self.__show(current_direction)



