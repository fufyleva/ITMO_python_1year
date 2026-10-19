from csv import reader


def open_file():
    try:
        with open('books-en.csv', 'r', encoding='utf-16', newline='') as in_file:
            data = list(reader(in_file, delimiter=';'))[1:]
            return data
    except FileNotFoundError: # если нет файла
        print("File isn't found")


def name_longer_30():
    data = open_file()
    result = sum([1 for i in data if len(i[1]) > 30])
    print(result)
    return result


def find_book():
    author = input("Write the author's name: ").strip().upper() # перевожу в большие буквы и убираю пробелы и
                                                                # подобные знаки для более удобного поиска
    data = open_file()
    authors_books = []
    for row in data:
        if (float(row[-1].replace(',', '.')) < 150) and (row[2].upper() == author):
            authors_books.append(row)
    if authors_books:
        maxi_name = len(max([i[1] for i in authors_books], key=len)) # максимальная длина имени автора,
                                                                    # чтобы был более красивый вывод
        print(f'{'N':<3} {'Book Title':<{maxi_name + 3}}   {'Year':<4}')
        for i in range(len(authors_books)):
            print(f'{str(i + 1) + '.' :<3} {authors_books[i][1]:<{maxi_name + 3}}   {authors_books[i][3]:<4}')
    else:
        print("No book")
    return authors_books


def write_books():
    data = open_file()[:20]
    with open('write_books.txt', 'w', newline='') as out_file:
        maxi_lens = [len(max(list([data[i][j] for i in range(len(data))]), key=len)) for j in [1, 2]] # максимальная
        # длина имени и названия книги, чтоб красиво записывалось
        out_file.write(f'{'N':<3} {'Author':<{maxi_lens[1] + 2}} {'Title':<{maxi_lens[0] + 2}} – {'Year'}\n')
        for i in range(20):
            out_file.write(f'{str(i + 1) + '.' :<3} {data[i][2]:<{maxi_lens[1] + 2}} {data[i][1]:<{maxi_lens[0] + 2}} – {data[i][3]}\n')

# name_longer_30()
# find_book()
# write_books()

# доп
def publishers():
    data = open_file()
    publishers_m = list(set([i[4] for i in data]))
    for i in range(len(publishers_m)):
        print(i + 1, publishers_m[i])


def the_most_popular():
    data = sorted(open_file(), key=lambda x: (float(x[-2]), float(x[-1].replace(',', '.'))), reverse=True)
    # не было второго критерия по сортировке (основной это количество скачиваний), поставила с максимальной ценой
    for i in range(20):
        print(f'{i + 1}.', data[i])

publishers()
the_most_popular()