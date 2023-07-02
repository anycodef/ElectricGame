from pygame.image import load
from code.globals.constanst import join, path_root_project

from pygame import KEYDOWN, KEYUP, K_SPACE

from code.globals.Effects.arcVoltaic import ArcVoltaic, Point, CoordSys

from pygame.mouse import get_pos


class AbstractArcVoltaicWeaponCollision:
    list_rect_for_collision = []


class AbstractMechanicsGui:
    x, y = 0, 0


class AbstractFacturesWeapon:
    X_RELATIVE = {
        'right': 17
    }
    Y_RELATIVE = 55

    X_SHOOT, Y_SHOOT = 50, 9

    x, y = 0, 0


class ArcVoltaicWeaponMechanics(AbstractArcVoltaicWeaponCollision, AbstractMechanicsGui):
    def __init__(self):
        pass

    def run(self):
        pass


class ArcVoltaicWeaponGui(AbstractMechanicsGui, AbstractFacturesWeapon):
    def __init__(self, screen):
        self.__arc_voltaic = ArcVoltaic(screen)
        self.__sysCord = CoordSys(screen.get_width(), screen.get_height())

    def show(self):
        self.__arc_voltaic.show(10, Point(*self.__sysCord.coord_pygame_to_coord_system(
            AbstractFacturesWeapon.x + AbstractFacturesWeapon.X_SHOOT,
            AbstractFacturesWeapon.y + AbstractFacturesWeapon.Y_SHOOT)),
                                Point(*self.__sysCord.coord_pygame_to_coord_system(*get_pos())))


class ArcVoltaicWeapon:
    def __init__(self, screen):
        self.__mechanics = ArcVoltaicWeaponMechanics()
        self.__gui = ArcVoltaicWeaponGui(screen)

    def run(self):
        self.__gui.show()


def update_position(x_character, y_character, current_direction):
    AbstractFacturesWeapon.x = x_character + AbstractFacturesWeapon.X_RELATIVE[current_direction]
    AbstractFacturesWeapon.y = y_character + AbstractFacturesWeapon.Y_RELATIVE


class Weapon:
    def __init__(self, screen):
        self.__screen = screen

        self.__img = {}

        # effect shooting
        self.__x_shoot = 0
        self.__x_shooting = 5

        self.__shooting = False

        # load default images
        self.load_weapon()

        # arc voltaic shoot
        self.__arc = ArcVoltaicWeapon(screen)

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

    def __shoot(self):
        if self.__shooting:
            if self.__x_shoot == self.__x_shooting:
                self.__x_shoot = -self.__x_shooting
            else:
                self.__x_shoot += self.__x_shooting
        else:
            self.__x_shoot = 0

    def __show(self, current_direction):
        self.__screen.blit(self.__img[current_direction], (AbstractFacturesWeapon.x + self.__x_shoot,
                                                           AbstractFacturesWeapon.y))

    def run(self, x_character, y_character, current_direction):
        update_position(x_character, y_character, current_direction)
        self.__shoot()
        self.__show(current_direction)

        if self.__shooting:
            self.__arc.run()



