import csv
from collections import defaultdict

def read_csv_file(filename):
    """Чтение CSV файла и возврат данных в виде списка словарей"""
    data = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=';')
            for row in csv_reader:
                data.append(row)
        return data
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден!")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None

def display_data(data):
    """Вывод данных в формате 'Ключ → Значение'"""
    if not data:
        return
    
    print("=" * 60)
    print("СОДЕРЖИМОЕ ФАЙЛА:")
    print("=" * 60)
    
    for i, row in enumerate(data, 1):
        print(f"\nПроект #{i}:")
        for key, value in row.items():
            print(f"  {key} → {value}")

def find_min_max_budget(data):
    """Нахождение проекта с самым маленьким и самым большим бюджетом"""
    if not data:
        return None, None
    
    min_budget = float('inf')
    max_budget = float('-inf')
    min_project = None
    max_project = None
    
    for row in data:
        try:
            budget = float(row.get('Budget', 0))
            
            if budget < min_budget:
                min_budget = budget
                min_project = row
            
            if budget > max_budget:
                max_budget = budget
                max_project = row
                
        except (ValueError, TypeError):
            continue
    
    return min_project, max_project

def calculate_total_team_size(data):
    """Подсчет общего количества сотрудников во всех проектах"""
    if not data:
        return 0
    
    total = 0
    for row in data:
        try:
            team_size = int(row.get('TeamSize', 0))
            total += team_size
        except (ValueError, TypeError):
            continue
    
    return total

def calculate_avg_completed_duration(data):
    """Вычисление средней продолжительности завершенных проектов"""
    if not data:
        return 0
    
    completed_durations = []
    for row in data:
        if row.get('Completed', '').strip().lower() == 'yes':
            try:
                duration = float(row.get('Duration', 0))
                completed_durations.append(duration)
            except (ValueError, TypeError):
                continue
    
    if not completed_durations:
        return 0
    
    return sum(completed_durations) / len(completed_durations)

def count_projects_by_status(data):
    """Подсчет количества проектов по статусам завершения"""
    if not data:
        return {}
    
    status_count = defaultdict(int)
    for row in data:
        status = row.get('Completed', 'Unknown').strip()
        status_count[status] += 1
    
    return dict(status_count)

def main():
    filename = "11.csv"
    data = read_csv_file(filename)
    
    if not data:
        print("Не удалось прочитать данные из файла.")
        return
    
    print("1. ЧТЕНИЕ И АНАЛИЗ СОДЕРЖИМОГО ФАЙЛА")
    print("=" * 60)
    display_data(data)
    
    print("\n" + "=" * 60)
    print("2. ПРОЕКТЫ С МИНИМАЛЬНЫМ И МАКСИМАЛЬНЫМ БЮДЖЕТОМ")
    print("=" * 60)
    
    min_project, max_project = find_min_max_budget(data)
    
    if min_project:
        print(f"\nПроект с минимальным бюджетом:")
        print(f"  ProjectID: {min_project.get('ProjectID', 'N/A')}")
        print(f"  ProjectName: {min_project.get('ProjectName', 'N/A')}")
        print(f"  Budget: {min_project.get('Budget', 'N/A')}")
    else:
        print("Не удалось определить проект с минимальным бюджетом")
    
    if max_project:
        print(f"\nПроект с максимальным бюджетом:")
        print(f"  ProjectID: {max_project.get('ProjectID', 'N/A')}")
        print(f"  ProjectName: {max_project.get('ProjectName', 'N/A')}")
        print(f"  Budget: {max_project.get('Budget', 'N/A')}")
    else:
        print("Не удалось определить проект с максимальным бюджетом")
    
    print("\n" + "=" * 60)
    print("3. ОБЩЕЕ КОЛИЧЕСТВО СОТРУДНИКОВ")
    print("=" * 60)
    
    total_team_size = calculate_total_team_size(data)
    print(f"Общее количество сотрудников во всех проектах: {total_team_size}")
    
    print("\n" + "=" * 60)
    print("4. СРЕДНЯЯ ПРОДОЛЖИТЕЛЬНОСТЬ ЗАВЕРШЕННЫХ ПРОЕКТОВ")
    print("=" * 60)
    
    avg_duration = calculate_avg_completed_duration(data)
    print(f"Средняя продолжительность завершенных проектов: {avg_duration:.2f}")
    
    print("\n" + "=" * 60)
    print("5. КОЛИЧЕСТВО ПРОЕКТОВ ПО СТАТУСАМ")
    print("=" * 60)
    
    status_counts = count_projects_by_status(data)
    print("Количество проектов по статусам завершения:")
    for status, count in status_counts.items():
        print(f"  Статус '{status}': {count} проект(ов)")

if __name__ == "__main__":
    import os
    main()