import random

chilas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'valert', 'dama', 'korol`', 'tuz']
mast = ['chervi', 'piki', 'bubi', 'kresti']

coloda = []
hand = []
table = []


# делает колоду
def create_coloda():
    for i in chilas:
        for b in mast:
            coloda.append(str(i) + ' ' + b)


# показать колоду	
def show_coloda():
    for i in coloda:
        print(i)
    print(len(coloda), '\n\n')


# показать руки
def show_hand():
    print("У вас на руках:")
    for i, b in zip(range(1, len(hand) + 1), hand):
        print(i, '\t', b)


# for i in hand:
#     for b in range(len(hand))
#         print(b,'\t', i)


# получить карту
def give_card(kol_vo=1):
    kol_vo = input("сколько карт вам нужно? \nНажмите Enter для 1 карты")
    if kol_vo == "":
        kol_vo = 1
    else:
        kol_vo=int(kol_vo)
    for i in range(kol_vo):
        a = random.choice(coloda)
        hand.append(a)
        print("Вы получили", a)
        coloda.remove(a)
    show_hand()


# положить карту на стол
def put_on_table():
    while True:
        try:
            value = input("Какие карты вы хотите положить на стол?")
        # except ValueError:
        #     print('Напишите числа через пробел')
        #     continue
        except TypeError:
            print("Пишите числа")
            continue
        try:
            for i in value.split(" "):
                table.append(hand[int(i) - 1])
                hand.remove(hand[int(i) - 1])
            break
            # table.append(hand[value - 1])
            # hand.remove(hand[value - 1])
            #     break
        except IndexError:
            print("\t\nУ вас нет такого номера карты, попробуйте еще раз")
        except TypeError:
            print("Пишите числа")
    print('На столе:', table)
