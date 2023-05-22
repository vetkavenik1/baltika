from random import shuffle
spisog_omg = ['молоко', 'соль', 'картошка']

triks = input('введи ингредиент (харош - стоп):')
while triks != 'харош':
    if triks in spisog_omg:
        print('этот ингедиент уже есть!')

    else:
        spisog_omg.append(triks)

    triks = input('введи ингредиент (харош - стоп):')

spisok_blender = []
nums = int(input('сколько месим ингредиентов'))
for i in range(nums):
    shuffle(spisog_omg)
    spisok_blender.append(spisog_omg[0])
    spisog_omg.remove(spisog_omg[0])

print('приготовь что нибудь из:')
for i in range(nums):
    print(spisok_blender[i])