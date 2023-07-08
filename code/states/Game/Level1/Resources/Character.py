from pygame.image import load
from code.globals.constanst import path_root_project, join

from pygame import KEYDOWN, K_UP

# accessories
from code.states.Game.Level1.Resources.weapon import Weapon
from pygame.rect import Rect

from code.states.Game.Level1.Resources.Platform import AbstractClassPlatform


# class for load all frames of the main character
class LoaderImgCharacter:
    def __init__(self):
        # all action with its amount frames
        self.__action_name_num_frames = [{'action': 'dead', 'nFrames': 5},
                                         {'action': 'run', 'nFrames': 12},
                                         {'action': 'jump', 'nFrames': 6}]

        # directions. As this is a game in 2d then the possibilities is a right and left
        self.__direction = ['right', 'left']

        # the images will be load on the dictionary and will have a follow structure
        # {'action': {'left': [img_1, img_2, ..., img_n], 'right': [img_1, img_2, ..., img_n]}
        self.figure_image = {}

    # This method fill a dictionary, and it has him the structure showed above
    def load(self, root_path):
        self.figure_image.clear()

        for dict_action_nFrames in self.__action_name_num_frames:
            action = dict_action_nFrames['action']
            n_frames = dict_action_nFrames['nFrames']

            self.figure_image.__setitem__(action, {})
            for direction in self.__direction:
                self.figure_image[action].__setitem__(direction, [])
                for i in range(1, n_frames + 1):
                    self.figure_image[action][direction].append(
                        load(join(root_path, f"{action}{i}-{direction}.png")))

                    if not (AbstractGeneralCharacter.width and AbstractGeneralCharacter.height):
                        AbstractGeneralCharacter.width, AbstractGeneralCharacter.height = \
                            self.figure_image[action][direction][0].get_width(), \
                            self.figure_image[action][direction][0].get_height()


class AbstractGeneralCharacter:
    x, y = 0, 0
    width, height = 0, 0
    update = False
    direction = 'right'


# This class is a controller of the position of sprites. This class modify the current position of character
# Only this class have a method for return the current position and the run for execute all method needed
# for to update the position.

# The method of this class haven't a while structure and depend on the parent class while's.
class CharacterMechanisms(AbstractGeneralCharacter):
    def __init__(self):
        self.__speed = [0, 0]  # speed for moving
        self.__RUN_SPEED_X = 50  # This is a constant that indicate a component x of the speed vector

        # for jump
        self.__JUMP_SPEED_Y = 60
        self.__time = 0
        self.__add_jump = self.__JUMP_SPEED_Y / 3

        self.__actions = {
            'run': self.__set_stop,
            'dead': self.__set_stop,
            'jump': self.__set_jump,
        }

    def __update_position(self):
        AbstractGeneralCharacter.x += self.__speed[0]
        AbstractGeneralCharacter.y += self.__speed[1]

    def __set_jump(self):
        # v = v_i + gT
        self.__time += 1
        self.__speed[1] = self.__add_jump * self.__time - self.__JUMP_SPEED_Y

        if self.__time == 6:
            self.__speed[1] = 0
            self.__time = 0

    def __set_stop(self):
        self.__speed[0] = 0

    # This method is on the class parent while's.
    def run(self, state):
        if AbstractClassPlatform.direction == 'left':
            AbstractGeneralCharacter.direction = 'right'
        else:
            AbstractGeneralCharacter.direction = 'left'

        # manage states: The structure of state is as this: [[act1, act2, ..., actn], ..., [act1, act2, ..., actn]]
        if AbstractGeneralCharacter.update:
            self.__actions[state[0]]()  # execute the correct method for the given state
            self.__update_position()


class ManageSpriteCharacter(AbstractGeneralCharacter):
    def __init__(self, screen):

        self.__current_img = None
        self.__loader_img = LoaderImgCharacter()
        self.__loader_img.load(join(path_root_project, 'src', 'sprite', 'mainPerson'))
        self.__screen = screen

        # for exchange frames
        self.__index_img = 0
        self.__current_state = None

        self.__actions = {
            'run': self.__set_img_action_loop,
            'dead': self.__set_img_action_keep_last_frame,
            'jump': self.__set_img_action_keep_last_frame
        }

    def get_state(self):
        return self.__current_state

    def __set_img_action_loop(self, states):
        if self.__current_state != states[0]:
            self.__index_img = 0
            self.__current_state = states[0]

        self.__index_img += 1

        if self.__index_img == self.__loader_img.figure_image[states[0]][AbstractGeneralCharacter.direction].__len__():
            self.__index_img = 0

        self.__current_img = \
            self.__loader_img.figure_image[states[0]][AbstractGeneralCharacter.direction][self.__index_img]

    def __set_img_action_keep_last_frame(self, states):
        if self.__current_state != states[0]:
            self.__index_img = 0
            self.__current_state = states[0]

        if self.__index_img + 1 != \
                self.__loader_img.figure_image[states[0]][AbstractGeneralCharacter.direction].__len__():
            self.__index_img += 1
        else:
            if states.__len__() > 1:
                states.remove(states[0])
                self.__index_img = 0

        self.__current_img = \
            self.__loader_img.figure_image[states[0]][AbstractGeneralCharacter.direction][self.__index_img]

    def __show(self):
        AbstractGeneralCharacter.width = self.__current_img.get_width()
        AbstractGeneralCharacter.height = self.__current_img.get_height()
        AbstractGeneralCharacter.rect_img = self.__current_img.get_rect()

        self.__screen.blit(self.__current_img, (AbstractGeneralCharacter.x, AbstractGeneralCharacter.y))

    def run(self, states):

        if AbstractGeneralCharacter.y is 0:
            AbstractGeneralCharacter.y = AbstractClassPlatform.y - AbstractGeneralCharacter.height

        if AbstractGeneralCharacter.direction == 'left':
            AbstractGeneralCharacter.x = .75 * self.__screen.get_width()
        else:
            AbstractGeneralCharacter.x = .25 * self.__screen.get_width()

        if AbstractGeneralCharacter.update:
            self.__actions[states[0]](states)
        self.__show()


class Character:
    def __init__(self, screen, get_current_fps):

        # accessories
        self.accessories = [Weapon(screen)]

        self.states = ['run']

        self.__mechanisms = CharacterMechanisms()
        self.__manager_sprite = ManageSpriteCharacter(screen)

        # manage fps character
        self.__FPS = 15
        self.__get_current_fps = get_current_fps
        self.__counter_space_time = self.__get_current_fps() + self.__FPS

    def exe(self):

        if self.__counter_space_time > self.__get_current_fps() / self.__FPS:
            AbstractGeneralCharacter.update = True
            self.__counter_space_time = 0
        else:
            AbstractGeneralCharacter.update = False
            self.__counter_space_time += 1

        self.__mechanisms.run(self.states)
        self.__manager_sprite.run(self.states)

        for _ in self.accessories:
            _.run(AbstractGeneralCharacter.x, AbstractGeneralCharacter.y, AbstractGeneralCharacter.direction)


class CharacterUser(Character):
    def __init__(self, screen, get_current_fps):
        Character.__init__(self, screen, get_current_fps)

    def __manage_event(self, queue_event):
        for _ in self.accessories:
            _.manage_events(queue_event)

        for event in queue_event:
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    if 'jump' not in self.states:
                        self.states = ['jump'] + self.states

    def execution(self, queue_event):
        self.__manage_event(queue_event)
        self.exe()
