from pygame.image import load
from code.globals.constanst import join, path_root_project
from pygame import KEYDOWN, KEYUP, K_SPACE
from code.globals.Effects.arcVoltaic import ArcVoltaic, Point, CoordSys
from pygame.mouse import get_pos, get_pressed
from random import choice

from code.states.Game.Level1.Resources.Battery import ModifierPercentageCharge


class AbstractArcVoltaicWeaponCollision:
    list_function_shoot = []


class AbstractMechanicsGui:
    x, y = None, None


class AbstractFacturesWeapon:
    X_RELATIVE = {
        'right': 17,
        'left': 6
    }
    Y_RELATIVE = 55

    X_SHOOT = {
        'right': 50,
        'left': 9
    }
    Y_SHOOT = 9

    x, y = 0, 0


class ArcVoltaicWeaponMechanics(AbstractArcVoltaicWeaponCollision, AbstractMechanicsGui):
    def __init__(self):
        pass

    @staticmethod
    def set_goal_mouse():
        if get_pressed()[0]:
            AbstractMechanicsGui.x, AbstractMechanicsGui.y = get_pos()
        else:
            AbstractMechanicsGui.x, AbstractMechanicsGui.y = None, None

    @staticmethod
    def set_random_goal():
        if AbstractArcVoltaicWeaponCollision.list_function_shoot:
            function_shoot_goal_return_position = choice(AbstractArcVoltaicWeaponCollision.list_function_shoot)
            AbstractMechanicsGui.x, AbstractMechanicsGui.y = function_shoot_goal_return_position()
            AbstractArcVoltaicWeaponCollision.list_function_shoot.remove(function_shoot_goal_return_position)
        else:
            AbstractMechanicsGui.x, AbstractMechanicsGui.y = None, None


class ArcVoltaicWeaponGui(AbstractMechanicsGui, AbstractFacturesWeapon):
    def __init__(self, screen):
        self.__arc_voltaic = ArcVoltaic(screen)
        self.__sysCord = CoordSys(screen.get_width(), screen.get_height())

    def show(self, current_direction):
        if AbstractMechanicsGui.x and AbstractMechanicsGui.y:
            self.__arc_voltaic.show(10, Point(*self.__sysCord.coord_pygame_to_coord_system(
                AbstractFacturesWeapon.x + AbstractFacturesWeapon.X_SHOOT[current_direction],
                AbstractFacturesWeapon.y + AbstractFacturesWeapon.Y_SHOOT)),
                                    Point(*self.__sysCord.coord_pygame_to_coord_system(
                                        AbstractMechanicsGui.x, AbstractMechanicsGui.y)), 20, 2)


class ArcVoltaicWeapon:
    def __init__(self, screen):
        self.__mechanics = ArcVoltaicWeaponMechanics()
        self.__gui = ArcVoltaicWeaponGui(screen)

    def set_goal_mouse(self):
        self.__mechanics.set_goal_mouse()

    def set_random_goal(self):
        self.__mechanics.set_random_goal()

    def run(self, current_direction):
        self.__gui.show(current_direction)


class Weapon:
    def __init__(self, screen):
        self.__screen = screen

        self.__img = {}

        # effect shooting
        self.__x_shoot = 0
        self.__x_shooting = 5

        self.__shooting = False
        self.__auto_shooting = False

        # load default images
        self.load_weapon()

        # arc voltaic shoot
        self.__arc = ArcVoltaicWeapon(screen)

    def load_weapon(self, name='weapon1'):
        self.__img.clear()
        for direction in ['right', 'left']:
            self.__img.__setitem__(direction, load(join(path_root_project, 'src', 'weapon', f'{name}-{direction}.png')))

    def manage_events(self, queue_event):
        if not self.__auto_shooting:
            if get_pressed()[0]:
                self.__arc.set_goal_mouse()
                self.__shooting = True
            else:
                self.__shooting = False

        for event in queue_event:
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.__shooting = not self.__shooting
                    self.__auto_shooting = True
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    self.__shooting = not self.__shooting
                    self.__auto_shooting = False

        if self.__auto_shooting:
            self.__arc.set_random_goal()

    def __shoot(self):
        if self.__shooting:
            if self.__x_shoot == self.__x_shooting:
                self.__x_shoot = -self.__x_shooting
            else:
                self.__x_shoot += self.__x_shooting
        else:
            self.__x_shoot = 0

    def __battery_less_charge(self):
        if self.__shooting and AbstractMechanicsGui.x and AbstractMechanicsGui.y:
            ModifierPercentageCharge.decrease_level_battery(-.2)

    def __show(self, current_direction):
        self.__screen.blit(self.__img[current_direction], (AbstractFacturesWeapon.x + self.__x_shoot,
                                                           AbstractFacturesWeapon.y))

    @staticmethod
    def update_position(x_character, y_character, current_direction):
        AbstractFacturesWeapon.x = x_character + AbstractFacturesWeapon.X_RELATIVE[current_direction]
        AbstractFacturesWeapon.y = y_character + AbstractFacturesWeapon.Y_RELATIVE

    def run(self, x_character, y_character, current_direction):
        self.update_position(x_character, y_character, current_direction)
        self.__shoot()
        self.__battery_less_charge()
        self.__show(current_direction)

        if self.__shooting:
            self.__arc.run(current_direction)

    def __del__(self):
        AbstractArcVoltaicWeaponCollision.list_function_shoot = []

        AbstractMechanicsGui.x = None
        AbstractMechanicsGui.y = None

        AbstractFacturesWeapon.x = 0
        AbstractFacturesWeapon.y = 0





