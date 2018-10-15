# def func(a,b):
#     return a-b
# print(func(1,3))
# func = lambda a,b: a**b
#
# print(func(64, 64))
# chilsa = [i for i in range(1, 11)]+list(['valet', 'dama', 'korol', 'tuz'])
# mast = list('♥♠♣♦')
#  = [str(i)+' '+b for i in chilsa for b in mast]
# for i in :
#     print(i)

# def abb(*adbb):
#     for i in adbb:
#         if type(i) == int:
#             return str(i) + 'K=======K'
#         else:
#             return i + 'Jopa'
#
# a= abb(1, '1sdfsd','sadfsfc', 1341, 'dfc')
# print(a)
def dd():
    global coloda
    chilsa = [i for i in range(1, 11)] + list(['valet', 'dama', 'korol', 'tuz'])
    mast = list('♥♠♣♦')
    s = [str(i)+' '+b for i in chilsa for b in mast]
    coloda = dict()
    for i in s:
        #print(i, '-----', i[0:len(i)-2], i[0::-1].isdigit())  # проверка
        if i[0::-1].isdigit():
            coloda[i] = int(i[0:len(i)-2])
        elif i[0] == 't':
            coloda[i] = 11
        else:
            coloda[i] = 10
    return coloda
dd()
print(coloda)
for i in coloda.items():
    for b in i:
        print(b, end=" ")
    print(end='\n')