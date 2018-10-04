from binar import *

create_coloda()

while True:
    a = input("Что вы хотите сделать?\n	1-получит карту? \n	2- положить карту на стол ")
    if a == "1":
        give_card(6)
    elif a == '2':
        put_on_table()
    else:
        print('buy')
        break
