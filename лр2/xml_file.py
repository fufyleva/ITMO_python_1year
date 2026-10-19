from xml.etree import ElementTree
name_value = {}
tree = ElementTree.parse('currency.xml') # распарсиваю файл
root = tree.getroot() # достаю корневой элемент


for el in root:  # прохожусь по всем валютам в корневом элементе
    name = el.find('Name').text  # достаю имя по тегу
    value = el.find('Value').text  # достаю значение по тегу
    name_value[name] = value

for i in name_value:
    print(i, name_value[i])

