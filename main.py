import pygame
from sys import exit


def main():
    screen = pygame.display.set_mode((900, 700))
    pygame.display.set_caption("ElectricGame")

    background_color = pygame.Color("white")

    exit_game = False
    while not exit_game:
        screen.fill(background_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
    exit()


