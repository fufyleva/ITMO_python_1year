import json
import functions

def main_all(items, size, cur_points):
    area, value = functions.get_area_value(items)
    result = []
    n = len(value)

    def find_all_solutions(i, used_area, taken_points, chosen):
        if i == n:
            if taken_points > 0:
                result.append([chosen, taken_points])
            return
        elif area[i] <= used_area:
            find_all_solutions(i + 1, used_area - area[i], taken_points + value[i] * 2,
                               chosen | {items[i].get('name'): area[i]})
        find_all_solutions(i + 1, used_area, taken_points, chosen)
    find_all_solutions(0, size[0] * size[1], cur_points - sum(value), {})
    result.sort(key=lambda x: -x[1])

    for i in range(len(result)):
        print(f'\n-------- вариант {i + 1} --------')
        functions.appearance(size, result[i][0], result[i][1])


all_items = json.load(open('all_items.json'))
main_all(all_items, (2, 4), 15)
