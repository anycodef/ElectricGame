import time

import pygame
from sys import exit


def main():
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("ElectricGame")

    background_color = pygame.Color("white")

    stay_move_main_person = []
    clock = pygame.time.Clock()

    for i in range(4):
        stay_move_main_person.append(pygame.image.load(f"src\\sprite\\mainPerson\\stay{i + 1} 70x140.png"))

    exit_game = False
    while not exit_game:
        screen.fill(background_color)
        pygame.draw.rect(screen, "dark gray", (0, 500, 900, 100))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit_game = True
            if event.type == pygame.QUIT:
                exit_game = True

        for i in range(2):
            for image in stay_move_main_person:
                screen.blit(image, (70, 360))
                time.sleep(1)

   #     screen.blit(stay_move_main_person[0], (70, 360))
    #    screen.blit(stay_move_main_person[1], (70, 360))
     #   screen.blit(stay_move_main_person[2], (70, 360))
      #  screen.blit(stay_move_main_person[4], (70, 360))

        pygame.display.flip()
        clock.tick(20)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
    exit()
