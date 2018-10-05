import pygame, math
from binar import *

create_coloda()  # ================================================ Делаем колоду
pygame.init()
game_work = True
# region color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# endregion
# region Экран
window = pygame.display.set_mode((1820, 900))
pygame.display.set_caption("Cards..... Jack")
# endregion
col_x = 15
col_y = 50
# Делаем карту, цвет и ее координаты
card = pygame.Surface((60, 80))
card.fill(WHITE)

ab = 400


def text_in_box(text='Jopa', size=10):
    myfont = pygame.font.SysFont('Comic Sans MS', size)
    textsurface = myfont.render(text, False, BLACK)
    return textsurface


gg = ['mama', 'papa', 'ya', 'ponty']

flag = True

while game_work:
    # region выход из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Кнопка выхода нажата\nBuy it game')
            game_work = False
    # endregion
    if flag:
        for i in coloda:
            b = i
            # i = pygame.Surface((65, 95)), pygame.Surface
            # i.fill(RED)
            i = pygame.Surface((60, 80))
            i.fill(WHITE)
            i.blit(text_in_box(b), (0, 0))
            window.blit(i, (col_x, col_y))
            if col_y <= ab:
                col_x += 24
                col_y += 50
                ab = 400
            else:
                col_x += 24
                col_y -= 50
                ab = 50
    flag = False
    # card.blit(text_in_box(), (0, 0))
    # window.blit(card, (col_x, col_y))

    pygame.display.flip()  # Обновить экран
