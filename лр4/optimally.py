import json
import functions

def get_table_points(max_area: int, data: list):
    area, value = functions.get_area_value(data)
    cont_items = len(value)
    # создаем таблицу, где все 0, размером max_area + 1 на cont_items + 1, что бы корректно работала сортировка
    table = [[0 for i in range(max_area + 1)] for j in range(cont_items + 1)]
    for i in range(cont_items + 1): # перебиваем индекс предмета
        for a in range(max_area + 1): # перебираем текущую возможную площадь
            if a == 0 or i == 0:
                table[i][a] = 0
            elif area[i - 1] <= a: # можем взять
                # берем максимум из верхнего варианта / текущий + остаток площади
                table[i][a] = max(table[i - 1][a], table[i - 1][a - area[i - 1]] + value[i - 1])
            else:  # не можем взять, копируем лучший результат
                table[i][a] = table[i-1][a]
    return table


def get_one_solution(max_area: int, data: list, cur_points: int):
    area, value = functions.get_area_value(data)
    table = get_table_points(max_area, data)
    n = len(value)
    points = table[n][max_area]  # какую максимальную сумму собрали
    res_points = points * 2 + cur_points - sum(value)  # вычитаем из макс суммы цену предметов,
                                                        # которые не взяли
    if res_points <= 0:  # проверка на умрет ли Том
        return {}, res_points
    taken_indexes = []  # какие предметы берем

    for i in range(n, 0, -1):
        if points == 0:  # собрали все предметы
            break
        # если ничего не поменялось в таблице, значит этот предмет не бырали, идем тальше
        elif table[i][max_area] == table[i - 1][max_area]:
            continue
        else:  # значение поменялось
            taken_indexes.append(i - 1)
            points -= value[i - 1]
            max_area -= area[i - 1]

    taken_items = {data[i].get('name'): data[i].get('size') for i in taken_indexes}
    return taken_items, res_points


def main_one_solution(size: tuple, start_points: int, data: list):
    items, points = get_one_solution(size[0] * size[1], data, start_points)
    functions.appearance(size, items, points)

all_items = json.load(open('all_items.json'))
main_one_solution((1, 7), 15,  all_items)  # доп задание с 7
main_one_solution((2, 4), 15, all_items)