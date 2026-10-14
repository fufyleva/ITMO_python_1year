import os
from time import sleep

blue = '\u001b[44m'
red = '\u001b[41m'
white = '\u001b[47m'
reset = '\u001b[0m'


# 1
def flag():
    pixel = '   '
    height = 7 # высота флага
    for i in range(height):
        print(blue + pixel * 3 + white + pixel * 3 + red + pixel * 3 + reset)


# 2
def pattern(n=2):  # n количество узоров
    pixel = '   '
    flag = True # делаем "  #  " или "#  #" строку (чередование белых квадратов
    for i in range(3):
        if flag:
            print((white + pixel + reset + pixel) * n * 3)
            flag = False
        else:
            print((pixel + white + pixel + reset) * n * 3)
            flag = True

# 3

def animation():
    os.system('clear')
    pixel = '   '
    num_color = 0
    for k in range(3):
        size = 13 - 6 * k # длина стороны квадрата
        top = 3 + 3 * k # начало отсчета для квадрата по ОУ (левый верхний угол)
        left = 9 + 9 * k # начало отсчета для квадрата по ОХ (левый верхний угол)
        colors = [44, 41, 42]

        for row in range(size):
            print(f'\033[{top + row};{left}H', end='') # идем в начало отсчета, но с каждоной новой строкой (итерацией)
            # смещаемся вниз на единицу, чтобы нарисовать строку пикселей
            for col in range(size):
                print(f'\u001b[{colors[num_color]}m' + pixel + reset, end='') # рисуем строку пикселей
        num_color += 1  # смена цвета
        sleep(0.5)
        os.system('clear')


# 4
def sequence():
    greater_0 = []  # числа больше 0
    less_0 = []  # числа меньше 0
    with open('sequence.txt', 'r') as f: # считываем числа
        for i in f:
            if float(i) > 0:
                greater_0.append(float(i))
            elif float(i) < 0:
                less_0.append(float(i))
    sumi_of_nums = len(greater_0) + len(less_0)  # сумма чисел
    print(f'{blue}{' ' * int(len(greater_0) / 5)}{reset} {len(greater_0) / sumi_of_nums * 100}% numbers more than 0')
    # строка с теми, что больше 0
    print(f'{red}{' ' * int(len(less_0) / 5)}{reset} {len(less_0) / sumi_of_nums * 100}% numbers less than 0 ')
    # строка с теми что меньше 0


# 5
# примечание: для корректного отображения графика, надо раскрыть терминал, чтобы он был большим
# т.е не должно быть необходимости прокручивать. Если терминал будет узким окном, то график обрежется
def parabola():
    os.system('clear')
    # рисем ось ординат
    print('y ^')
    for i in range(25, 1, -1):
        if i < 10:
            print(f'{i} |')
        else:
            print(f'{i}|')
    print(f'1 |___{'___' * 4} > x')
    # рисуем ось абсцисс
    print('0 ', end='')
    for i in range(1, 6):
        print(f' {i} ', end='')
    print(f'\033[1A\033[14D{blue}  {reset}', end='')
    # заполняем значениями
    cur_value_of_function = 1  # текущее значение функции. переменная чтобы было проще рисовать колонку
    for i in range(2, 6):
        while i ** 2 > cur_value_of_function:
            print(f'\033[1A{blue}  {reset}\033[2D', end='')  # рисуем колонку от cur_value_of_function до квадрата числа
            cur_value_of_function += 1
        print(f'\033[2C', end='') # смещаемся вправо для новой колонки
    print(f'\033[27B') # смешаемся вниз, чтобы строка с тем, что программа выполнена не перекрыла график





# запуск
flag()
sleep(1)
os.system('clear')
pattern()
sleep(1)
os.system('clear')
animation()
sleep(1)
sequence()
sleep(1)
parabola()
