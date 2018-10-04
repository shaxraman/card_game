import pygame

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

# Делаем квадрат и его координаты
screen = pygame.Surface((40, 40))
screen.fill(RED)

myfont = pygame.font.SysFont('Comic Sans MS', 8)
textsurface = myfont.render('jopa', False, (0, 0, 0))


while game_work:
    # region выход из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Кнопка выхода нажата\nBuy it game')
            game_work = False
    # endregion

    # Надпись в квадрате
    screen.blit(textsurface, (0, 0))
    window.blit(screen, (40 - 10, 600 - 40 - 10))
    pygame.display.flip()
