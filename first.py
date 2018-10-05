import pygame, math
from binar import *

create_coloda()  # ================================================ Делаем колоду
# create_coloda()
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
col_y = 0
# Делаем карту, цвет и ее координаты
card = pygame.Surface((60, 80))
card.fill(WHITE)

ab = 400
j = pygame.Surface((75, 95))
j.fill(RED)


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
            pygame.time.wait(50)
            b = i
            i = pygame.Surface((60, 80))
            i.fill(WHITE)
            i.blit(text_in_box(b), (0, 0))
            j.blit(i, (5, 5))
            window.blit(j, (col_x, col_y))
            col_x += 30
            col_y = - (200 * math.cos(col_x / 300) - 200)
            pygame.display.flip()  # Обновить экран
    flag = False
    # card.blit(text_in_box(), (0, 0))
    # window.blit(card, (col_x, col_y))

    pygame.display.flip()  # Обновить экран
