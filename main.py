import time

import pygame
from sys import exit


def main():
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("ElectricGame")

    background_color = pygame.Color("white")

    stay_move_main_person = []
    clock = pygame.time.Clock()

    for i in range(12):
        stay_move_main_person.append(pygame.image.load(f"src\\sprite\\mainPerson2\\run{i + 1}-right.png"))

    exit_game = False
    index = 0
    while not exit_game:
        screen.fill(background_color)
        pygame.draw.rect(screen, "dark gray", (0, 500, 900, 100))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit_game = True
            if event.type == pygame.QUIT:
                exit_game = True

        if index >= 5: index = 0
        screen.blit(stay_move_main_person[index], (70, 500 - stay_move_main_person[index].get_height()))
        index += 1

   #     screen.blit(stay_move_main_person[0], (70, 360))
    #    screen.blit(stay_move_main_person[1], (70, 360))
     #   screen.blit(stay_move_main_person[2], (70, 360))
      #  screen.blit(stay_move_main_person[4], (70, 360))

        pygame.display.flip()
        clock.tick(15)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
    exit()
