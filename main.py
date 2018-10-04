from binar import *

create_coloda()

game_not_over = True
while game_not_over:
    a = input("Что вы хотите сделать?\n	1-получит карту? \n	2- положить карту на стол ")
    if a == "1":
        give_card(6)
    elif a == '2':
        put_on_table()
    else:
        print('Buy it game')
        game_not_over = False
