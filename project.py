import csv
import sys
import argparse
from statistics import mean
from pathlib import Path


# Функция для парсинга аргументов командной строки
def parse_arguments():
    # Создаем парсер для командной строки
    parser = argparse.ArgumentParser(
        description="Консольное приложение для анализа температурных данных из CSV файла."
    )
    # Добавляем аргумент для файла
    parser.add_argument("-f", "--file", type=str, help="Путь к входному CSV файлу для обработки.")
    # Добавляем аргумент для месяца (необязательный)
    parser.add_argument("-m", "--month", type=int, choices=range(1, 13), help="Номер месяца для вывода статистики.")
    return parser.parse_args()


# Функция для валидации данных в каждой строке
def validate_row(row, line_number):
    try:
        # Проверяем, что в строке ровно 6 колонок
        if len(row) != 6:
            raise ValueError(f"Некорректное количество колонок (ожидалось 6, получено {len(row)})")

        # Разбираем данные по колонкам
        year, month, day, hour, minute, temp = row

        # Проверяем формат каждого поля
        if not (year.isdigit() and len(year) == 4):
            raise ValueError("Некорректный формат года.")
        if not (month.isdigit() and 1 <= int(month) <= 12):
            raise ValueError("Некорректный формат месяца.")
        if not (day.isdigit() and 1 <= int(day) <= 31):
            raise ValueError("Некорректный формат дня.")
        if not (hour.isdigit() and 0 <= int(hour) <= 23):
            raise ValueError("Некорректный формат часа.")
        if not (minute.isdigit() and 0 <= int(minute) <= 59):
            raise ValueError("Некорректный формат минуты.")
        if not (temp.lstrip("-").isdigit() and -99 <= int(temp) <= 99):
            raise ValueError("Некорректная температура.")
    except ValueError as e:
        # В случае ошибки выводим подробности о строке с ошибкой
        raise ValueError(f"Ошибка в строке {line_number}: {e}")


# Функция для чтения и обработки данных из CSV файла
def read_csv_file(file_path):
    data = {}  # Словарь для хранения данных (по месяцам)
    errors = []  # Список для хранения ошибок

    try:
        # Открываем CSV файл для чтения
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=';')  # Чтение с разделителем ";"
            for line_number, row in enumerate(reader, start=1):
                # Удаляем пробелы из каждого элемента строки
                row = [value.strip() for value in row]
                try:
                    # Валидируем данные в строке
                    validate_row(row, line_number)
                    year, month, day, hour, minute, temp = row
                    month = int(month)  # Преобразуем месяц в целое число
                    temp = int(temp)  # Преобразуем температуру в целое число

                    # Добавляем температуру в список для месяца
                    if month not in data:
                        data[month] = []
                    data[month].append(temp)
                except ValueError as e:
                    # В случае ошибки добавляем сообщение об ошибке в список
                    errors.append(str(e))
    except FileNotFoundError:
        # Обрабатываем случай, если файл не найден
        print(f"Файл {file_path} не найден.")
        sys.exit(1)

    return data, errors


# Функция для вычисления статистики (средняя, минимум, максимум) по данным
def calculate_statistics(data):
    statistics = {}
    for month, temps in data.items():
        # Вычисляем статистику для каждого месяца
        statistics[month] = {
            "average": mean(temps),  # Средняя температура
            "min": min(temps),  # Минимальная температура
            "max": max(temps),  # Максимальная температура
        }
    return statistics


# Функция для вывода статистики
def print_statistics(statistics, month=None):
    if month:
        # Если задан месяц, выводим только статистику по этому месяцу
        if month in statistics:
            stats = statistics[month]
            print(f"Статистика за месяц {month}:")
            print(f"  Средняя температура: {stats['average']:.2f}")
            print(f"  Минимальная температура: {stats['min']}")
            print(f"  Максимальная температура: {stats['max']}")
        else:
            # Если данных за месяц нет, выводим сообщение
            print(f"Данные за месяц {month} отсутствуют.")
    else:
        # Если месяц не задан, выводим статистику за год
        print("Статистика за год:")
        for month, stats in sorted(statistics.items()):
            print(f"Месяц {month}:")
            print(f"  Средняя температура: {stats['average']:.2f}")
            print(f"  Минимальная температура: {stats['min']}")
            print(f"  Максимальная температура: {stats['max']}")


# Главная функция, которая управляет всей программой
def main():
    args = parse_arguments()  # Получаем аргументы из командной строки

    if not args.file:
        # Если не указан файл, выводим ошибку и завершаем программу
        print("Укажите входной файл с помощью ключа -f. Используйте -h для справки.")
        sys.exit(1)

    file_path = Path(args.file)  # Получаем путь к файлу
    if not file_path.exists():
        # Если файл не существует, выводим ошибку и завершаем программу
        print(f"Файл {file_path} не найден.")
        sys.exit(1)

    data, errors = read_csv_file(file_path)  # Читаем и обрабатываем данные из файла

    if errors:
        # Если были ошибки при обработке файла, выводим их
        print("Ошибки при обработке файла:")
        for error in errors:
            print(error)

    if data:
        # Если данные есть, вычисляем статистику и выводим ее
        statistics = calculate_statistics(data)
        if args.month:
            print_statistics(statistics, month=args.month)
        else:
            print_statistics(statistics)
    else:
        # Если данных нет, выводим сообщение
        print("Нет корректных данных для отображения статистики.")


# Точка входа в программу
if __name__ == "__main__":
    main()
