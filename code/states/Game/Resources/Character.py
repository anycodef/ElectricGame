from pygame.image import load
from code.globals.constanst import path_root_project, join

from pygame import KEYUP, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT


# class for load all frames of the main character
class LoaderImgCharacter:
    def __init__(self):
        # all action with its amount frames
        self.__action_name_num_frames = [{'action': 'dead', 'nFrames': 5},
                                         {'action': 'run', 'nFrames': 12},
                                         {'action': 'jump', 'nFrames': 6},
                                         {'action': 'stop', 'nFrames': 1},
                                         {'action': 'toBendDown', 'nFrames': 5},
                                         {'action': 'toBendUp', 'nFrames': 5}]

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


# This class is a controller of the position of sprites. This class modify the current position of character
# Only this class have a method for return the current position and the run for execute all method needed
# for to update the position.

# The method of this class haven't a while structure and depend on the parent class while's.
class CharacterMechanisms:
    def __init__(self):
        self.__x, self.__y = [10, 100]  # This is a position of the sprites
        self.__speed = [0, 0]  # speed for moving
        self.__RUN_SPEED_X = 50  # This is a constant that indicate a component x of the speed vector

        self.__actions = {
            'run': self.__set_run,
            'dead': self.__set_stop,
            'jump': self.__set_jump,
            'stop': self.__set_stop,
            'toBendDown': self.__set_toBendDown,
            'toBendUp': self.__set_toBendUp
        }

    def get_pos(self):
        return self.__x, self.__y

    def __update_position(self):
        self.__x += self.__speed[0]
        self.__y += self.__speed[1]

    def __set_run(self):
        self.__speed[0] = self.__RUN_SPEED_X

    def __set_jump(self):
        pass

    def __set_stop(self):
        self.__speed[0] = 0

    def __set_toBendDown(self):
        pass

    def __set_toBendUp(self):
        pass

    def __update_direction(self, direction):
        if direction == 'left':
            if self.__RUN_SPEED_X > 0:
                self.__RUN_SPEED_X *= -1
        else:
            if self.__RUN_SPEED_X < 0:
                self.__RUN_SPEED_X *= -1

    # This method is on the class parent while's.
    def run(self, current_state, current_direction):
        self.__update_direction(current_direction)
        self.__actions[current_state]()  # execute the correct method for the given state
        self.__update_position()


class ManageSpriteCharacter:
    def __init__(self, screen):
        self.__screen = screen

        self.__current_img = None
        self.__loader_img = LoaderImgCharacter()
        self.__loader_img.load(join(path_root_project, 'src', 'sprite', 'mainPerson'))

        # for exchange frames
        self.__index_img = 0
        self.__current_state = None

        self.__actions = {
            'run': self.__set_img_action_loop,
            'dead': self.__set_img_action_keep_last_frame,
            'jump': self.__set_img_action_keep_last_frame,
            'stop': self.__set_img_action_loop,
            'toBendDown': self.__set_img_action_keep_last_frame,
            'toBendUp': self.__set_img_action_keep_last_frame
        }

    def get_state(self):
        return self.__current_state

    def __set_img_action_loop(self, states, current_direction):
        if self.__current_state != states[0]:
            self.__index_img = 0
            self.__current_state = states[0]

        self.__index_img += 1

        if self.__index_img == self.__loader_img.figure_image[states[0]][current_direction].__len__():
            self.__index_img = 0

        self.__current_img = self.__loader_img.figure_image[states[0]][current_direction][self.__index_img]

    def __set_img_action_keep_last_frame(self, states, current_direction):
        if self.__current_state != states[0]:
            self.__index_img = 0
            self.__current_state = states[0]

        if self.__index_img + 1 != self.__loader_img.figure_image[states[0]][current_direction].__len__():
            self.__index_img += 1
        else:
            if states.__len__() > 1:
                states.remove(states[0])
                self.__index_img = 0

        self.__current_img = self.__loader_img.figure_image[states[0]][current_direction][self.__index_img]

    def __show(self, current_pos):
        self.__screen.blit(self.__current_img, current_pos)

    def run(self, states, current_direction, current_pos):
        self.__actions[states[0]](states, current_direction)
        self.__show(current_pos)


class Character:
    def __init__(self, screen):
        self.__current_pos = None

        self.states = ['stop']
        self.current_direction = 'right'

        self.__mechanisms = CharacterMechanisms()
        self.__manager_sprite = ManageSpriteCharacter(screen)

    def exe(self):
        self.__mechanisms.run(self.states[0], self.current_direction)
        self.__current_pos = self.__mechanisms.get_pos()

        self.__manager_sprite.run(self.states, self.current_direction, self.__current_pos)


class CharacterUser(Character):
    def __init__(self, screen):
        Character.__init__(self, screen)
        self.__speed_x = 10

    def __manage_event(self, queue_event):
        for event in queue_event:
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    self.states = ['jump'] + self.states

                if event.key == K_DOWN:
                    print(self.states)
                    self.states.remove('stop')
                    self.states.append('toBendUp')

                if event.key == K_LEFT:
                    self.states.remove('stop')
                    self.states.append('run')
                    self.current_direction = 'left'

                if event.key == K_RIGHT:
                    self.states.remove('stop')
                    self.states.append('run')
                    self.current_direction = 'right'

            if event.type == KEYUP:
                if event.key == K_DOWN:
                    self.states.append('toBendUp')
                    self.states.append('stop')

                if event.key in [K_LEFT, K_RIGHT]:
                    self.states.append('stop')
                    self.states.remove('run')

    def execution(self, queue_event):
        self.__manage_event(queue_event)
        self.exe()


class CharacterAuto(Character):
    def __init__(self, screen):
        Character.__init__(self, screen)


