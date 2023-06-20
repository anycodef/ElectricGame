from pygame.display import set_mode, flip
from pygame.event import get
from pygame import QUIT, quit, init
from sys import exit

from pygame.time import Clock

from code.states.Game.Resources.Battery import Battery

init()
screen = set_mode([800, 800])

bat = Battery(screen)
clock = Clock()

exit_program = False
while not exit_program:

    screen.fill('white')
    bat.run()
    for event in get():
        if event.type == QUIT:
            exit_program = True

    flip()
    clock.tick(2)

quit()
exit()


