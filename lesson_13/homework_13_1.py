import csv

# функция для вычитки уникальных уникальных строк
def read_unique_rows(file_path):
    unique_rows = set()
    header = None
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = list(csv.reader(csvfile))
        header = reader[0]  # Read header
        data_lines = reader[1:]
        for row in data_lines:
            # Convert list to tuple to make it hashable for the set
            unique_rows.add(tuple(row))
    print(f"Файл '{file_path}': прочитано {len(unique_rows)} уникальных строк.")
    print()
    return header, unique_rows


file_path_1 = 'random.csv'
file_path_2 = 'r-m-c.csv'

# Читаем уникальные строки из обоих файлов
header1, unique_rows1 = read_unique_rows(file_path_1)

header2, unique_rows2 = read_unique_rows(file_path_2)

# объединяем уникальные строки из двух сетов в один
united_rows = unique_rows1.union(unique_rows2)
print(f"Объединено {len(unique_rows1)} строк из файла '{file_path_1}' и {len(unique_rows2)} строк из файла '{file_path_2}'.")
print(f"Всего {len(united_rows)} уникальных строк будет записано в объединенный файл.")

output_file = 'result_zhuk.csv'

with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header1)
    for row in united_rows:
        writer.writerow(row)
    print()
    print(f"Данные успешно объединены и сохранены в файл: {output_file}")
