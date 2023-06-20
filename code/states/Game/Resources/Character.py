from pygame.image import load
from code.globals.constanst import path_root_project, join

from pygame import KEYUP, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT


class LoaderImgCharacter:
    def __init__(self):
        self.__action_name_num_frames = [('dead', 5), ('run', 12), ('jump', 6), ('stop', 1), ('toBendDown', 5)]
        self.__direction = ['right', 'left']

        self.figure_image = {}

    def load(self, root_path):
        self.figure_image.clear()

        for action, nFrame in self.__action_name_num_frames:
            self.figure_image.__setitem__(action, {})
            for direction in self.__direction:
                self.figure_image[action].__setitem__(direction, [])
                for i in range(1, nFrame + 1):
                    self.figure_image[action][direction].append(
                        load(join(root_path, f"{action}{i}-{direction}.png")))


class CharacterMechanisms:
    def __init__(self):
        self.__x, self.__y = [10, 100]
        self.__speed = [0, 0]

    def get_pos(self):
        return self.__x, self.__y

    def update_position(self):
        self.__x += self.__speed[0]
        self.__y += self.__speed[1]

    def set_run(self, speed_x):
        self.__speed[0] = speed_x

    def set_jump(self):
        pass


class ManageSpriteCharacter:
    def __init__(self, screen):
        self.__screen = screen

        self.__current_img = None
        self.__loader_img = LoaderImgCharacter()
        self.__loader_img.load(join(path_root_project, 'src', 'sprite', 'mainPerson'))

    def __set_img(self, current_state, current_direction):
        if self.__current_img in self.__loader_img.figure_image[current_state][current_direction]:
            index = self.__loader_img.figure_image[current_state][current_direction]. \
                index(self.__current_img)

            if index + 1 == self.__loader_img.figure_image[current_state][current_direction].__len__():
                index = 0
            else:
                index += 1

            self.__current_img = self.__loader_img.figure_image[current_state][current_direction][index]
        else:
            self.__current_img = self.__loader_img.figure_image[current_state][current_direction][0]

    def __show(self, current_pos):
        self.__screen.blit(self.__current_img, current_pos)

    def run(self, current_state, current_direction, current_pos):
        self.__set_img(current_state, current_direction)
        self.__show(current_pos)


class Character:
    def __init__(self, screen):
        self.__current_pos = None

        self.current_state = 'stop'
        self.current_direction = 'right'

        self.__mechanisms = CharacterMechanisms()
        self.__manager_sprite = ManageSpriteCharacter(screen)

    def run(self, speed_x):
        self.__mechanisms.set_run(speed_x)
        self.current_state = 'run'

    def exe(self):
        self.__mechanisms.update_position()
        self.__current_pos = self.__mechanisms.get_pos()
        self.__manager_sprite.run(self.current_state, self.current_direction, self.__current_pos)


class CharacterUser(Character):
    def __init__(self, screen):
        Character.__init__(self, screen)
        self.__speed_x = 10

    def __manage_event(self, queue_event):
        for event in queue_event:
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    pass
                if event.key == K_DOWN:
                    pass
                if event.key == K_LEFT:
                    self.current_state = 'run'
                    self.current_direction = 'left'
                    self.run(-self.__speed_x)

                if event.key == K_RIGHT:
                    self.current_state = 'run'
                    self.current_direction = 'right'
                    self.run(self.__speed_x)

            if event.type == KEYUP:
                if event.key == K_UP:
                    pass
                if event.key == K_DOWN:
                    pass
                if event.key in [K_LEFT, K_RIGHT]:
                    self.run(0)
                    self.current_state = 'stop'

    def execution(self, queue_event):
        self.__manage_event(queue_event)
        self.exe()


class CharacterAuto(Character):
    def __init__(self, screen):
        Character.__init__(self, screen)


