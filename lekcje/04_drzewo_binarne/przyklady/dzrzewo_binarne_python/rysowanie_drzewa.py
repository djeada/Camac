import pygame
import sys
from drzewo_binarne import DrzewoBinarne

# Kolory
KOLORY = {"bialy": (255, 255, 255), "czarny": (0, 0, 0), "czerwony": (255, 0, 0)}

# Inicjalizacja drzewa binarnego
drzewo = DrzewoBinarne()
wartosci = [10, 5, 15, 2, 7]
[drzewo.dodaj(wartosc) for wartosc in wartosci]

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna
ROZMIAR = (800, 600)
ekran = pygame.display.set_mode(ROZMIAR)
pygame.display.set_caption("Wizualizacja Drzewa Binarnego")
font = pygame.font.Font(None, 36)

# Funkcja do rysowania drzewa
def rysuj_drzewo(ekran, wezel, x, y, dx, odleglosc=60, promien=20):
    if wezel:
        pygame.draw.circle(ekran, KOLORY["czarny"], (x, y), promien)
        tekst = font.render(str(wezel.klucz), True, KOLORY["czerwony"])
        ekran.blit(tekst, (x - tekst.get_width() // 2, y - tekst.get_height() // 2))

        if wezel.lewe:
            pygame.draw.line(ekran, KOLORY["czarny"], (x, y), (x - dx, y + odleglosc))
            rysuj_drzewo(ekran, wezel.lewe, x - dx, y + odleglosc, dx // 2)
        if wezel.prawe:
            pygame.draw.line(ekran, KOLORY["czarny"], (x, y), (x + dx, y + odleglosc))
            rysuj_drzewo(ekran, wezel.prawe, x + dx, y + odleglosc, dx // 2)


def main():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        ekran.fill(KOLORY["bialy"])
        rysuj_drzewo(ekran, drzewo.korzen, ROZMIAR[0] // 2, 40, ROZMIAR[0] // 4)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
