def get_area_value(item: list):
    area = [i.get('size') for i in item]
    value = [i.get('points') for i in item]
    return area, value


def appearance(size: tuple, items, points):
    if points <=0:
        print(f'Очков выживания {points}, размера {size[0]}*{size[1]} недостаточно.\nЗомби убьют Тома')
    else:
        height, width = size
        res_list = ['[ ]' for i in range(height * width)]
        cur_num = 0
        for name in items.keys():
            for tymes in range(items[name]):
                res_list[cur_num] = f'[{name}]'
                cur_num += 1

        for h in range(height):
            for w in range(width):
                print(res_list[h * width + w], end='')
            print('')
        print('Итоговые очки выживания:', points)