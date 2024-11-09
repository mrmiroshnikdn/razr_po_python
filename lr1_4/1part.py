# TODO решите задачу
#def task() -> float:
#    ...


#print(task())
import json

def calculate_weighted_score(json_file_path):
    # Инициализируем переменную для хранения суммы произведений
    total_weighted_score = 0.0

    # Открываем и читаем JSON файл
    with open(json_file_path, 'r') as file:
        data = json.load(file)  # Загружаем данные из JSON файла

        # Перебираем каждый словарь в данных
        for entry in data:
            # Проверяем, что ключи 'score' и 'weight' присутствуют
            if 'score' in entry and 'weight' in entry:
                # Вычисляем произведение 'score' и 'weight'
                product = entry['score'] * entry['weight']
                # Добавляем произведение к общей сумме
                total_weighted_score += product

    # Округляем результат до трех знаков после запятой
    return round(total_weighted_score, 3)

# Пример вызова функции
result = calculate_weighted_score('input.json')
print(result)
