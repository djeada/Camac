import itertools
import math
import pygame
import sys
import time

# Lista miast w formacie: (nazwa, x, y)
miasta = [("A", 50, 50), ("B", 200, 300), ("C", 350, 100), ("D", 450, 400)]


def oblicz_dystans(miasto1, miasto2):
    return math.sqrt((miasto1[1] - miasto2[1]) ** 2 + (miasto1[2] - miasto2[2]) ** 2)


def calkowity_dystans(trasa):
    dystans = 0
    for i in range(len(trasa) - 1):
        dystans += oblicz_dystans(trasa[i], trasa[i + 1])
    dystans += oblicz_dystans(trasa[-1], trasa[0])  # Powrot do pierwszego miasta
    return dystans


def rysuj_trase(trasa, screen):
    for i in range(len(trasa) - 1):
        pygame.draw.line(
            screen,
            (255, 0, 0),
            (trasa[i][1], trasa[i][2]),
            (trasa[i + 1][1], trasa[i + 1][2]),
            2,
        )
    pygame.draw.line(
        screen, (255, 0, 0), (trasa[-1][1], trasa[-1][2]), (trasa[0][1], trasa[0][2]), 2
    )


def rysuj_miasta(miasta, screen):
    font = pygame.font.Font(None, 36)
    for miasto in miasta:
        pygame.draw.circle(screen, (0, 0, 255), (miasto[1], miasto[2]), 10)
        text = font.render(miasto[0], 1, (10, 10, 10))
        screen.blit(text, (miasto[1] - 10, miasto[2] - 10))


def problem_komiwojazera_dynamicznie(miasta, screen):
    permutacje = itertools.permutations(miasta)
    najkrotsza_trasa = None
    minimalny_dystans = float("inf")

    for trasa in permutacje:
        screen.fill((255, 255, 255))
        rysuj_trase(trasa, screen)
        rysuj_miasta(miasta, screen)
        pygame.display.flip()
        time.sleep(0.5)  # Oczekiwanie pol sekundy przed rysowaniem kolejnej trasy

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        aktualny_dystans = calkowity_dystans(trasa)
        if aktualny_dystans < minimalny_dystans:
            minimalny_dystans = aktualny_dystans
            najkrotsza_trasa = trasa

    return najkrotsza_trasa, minimalny_dystans


def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Problem Komiwojazera")

    najkrotsza_trasa, minimalny_dystans = problem_komiwojazera_dynamicznie(
        miasta, screen
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((255, 255, 255))
        rysuj_trase(najkrotsza_trasa, screen)
        rysuj_miasta(miasta, screen)
        pygame.display.flip()


main()
