import pygame
from binar import *

# create_coloda()  # ================================================ Делаем колоду
pygame.init()
game_work = True
# region color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# endregion
# region Экран
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cards..... Jack")
# endregion
col_x = 10
col_y = 0
# Делаем карту, цвет и ее координаты
card = pygame.Surface((60, 80))
card.fill(WHITE)


def text_in_box(text='Jopa', size=10):
    myfont = pygame.font.SysFont('Comic Sans MS', size)
    textsurface = myfont.render(text, False, BLACK)
    return textsurface


gg = ['mama', 'papa', 'ya', 'ponty']

while game_work:
    # region выход из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Кнопка выхода нажата\nBuy it game')
            game_work = False
    # endregion
    card.blit(text_in_box(), (0, 0))
    window.blit(card, (col_x, col_y))

    pygame.display.flip()  # Обновить экран
