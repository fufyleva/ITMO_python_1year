from csv import reader


def open_file():
    try:
        with open('books-en.csv', 'r', encoding='utf-16', newline='') as in_file:
            data = list(reader(in_file, delimiter=';'))[1:]
            return data
    except FileNotFoundError: # если нет файла
        print("File isn't found")
        return []


def name_longer_30():
    data = open_file()
    if data:
        result = sum([1 for i in data if len(i[1]) > 30])
        print(result)
        return result
    print("File isn't found")
    return []

def find_book():
    author = input("Write the author's name: ").strip().upper() # перевожу в большие буквы и убираю пробелы и
                                                                # подобные знаки для более удобного поиска
    data = open_file()
    if data:
        authors_books = []
        for row in data:
            try:
                if (int(row[3]) in [1997, 1998, 1999, 2000]) and (author in row[2].upper()):
                    authors_books.append(row)
            except ValueError:
                if (int(row[-3]) in [1997, 1998, 1999, 2000]) and (author in row[-4].upper()):
                    authors_books.append(row)
        if authors_books:
            print(f'N name year')
            for i in range(len(authors_books)):
                print(f'{str(i + 1)} {authors_books[i][1]}   {authors_books[i][3]}')
        else:
            print("No book")
        return authors_books
    print("File isn't found")
    return []


def write_books():
    data = open_file()[:20]
    if data:
        with open('write_books.txt', 'w', newline='') as out_file:
            out_file.write(f'N  Author  Title    Year\n')
            for i in range(20):
                out_file.write(f'{str(i + 1)} {data[i][2]} {data[i][1]} – {data[i][3]}\n')
        return data
    print("File isn't found")
    return []

name_longer_30()
find_book()
write_books()

# доп
def publishers():
    data = open_file()
    if data:
        publishers_m = list(set([i[4] for i in data]))
        for i in range(len(publishers_m)):
            print(i + 1, publishers_m[i])
    print("File isn't found")
    return []


def the_most_popular():
    data = open_file()
    if data:
        data.sort(key=lambda x: float(x[-2]), reverse=True)
        for i in range(20):
            print(f'{i + 1}.', data[i][1])
        return data
    print("File isn't found")
    return []
# publishers()
# the_most_popular()