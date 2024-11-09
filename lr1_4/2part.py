# TODO импортировать необходимые молули


#INPUT_FILENAME = "input.csv"
#OUTPUT_FILENAME = "output.json"


#def task() -> None:
#    ...  # TODO считать содержимое csv файла

#    ...  # TODO Сериализовать в файл с отступ#ами равными 4


#if __name__ == '__main__':
    # Нужно для проверки
#    task()

 #   with open(OUTPUT_FILENAME) as output_f:
 #       for line in output_f:
 #          print(line, end="")
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Создаем пустой список для хранения записей
    json_data = []

    # Считываем содержимое CSV файла
    with open(INPUT_FILENAME, mode='r', newline='', encoding='utf-8') as csv_file:
        # Создаем объект csv.reader
        csv_reader = csv.reader(csv_file)

        # Извлекаем заголовки
        headers = next(csv_reader)

        # Проходим по всем строкам в CSV файле
        for row in csv_reader:
            # Создаем словарь для текущей строки
            row_dict = {}
            for i, header in enumerate(headers):
                row_dict[header] = row[i]
            # Добавляем словарь в список
            json_data.append(row_dict)

    # Сериализуем данные в JSON файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # Выполняем задачу
    task()

    # Для проверки, печатаем содержимое выходного JSON файла
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")