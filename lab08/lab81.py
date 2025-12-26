import requests
import json
import os

def get_asian_countries():
    """Получить данные об азиатских странах с численностью населения более 30 миллионов"""
    url = "https://restcountries.com/v3.1/region/asia"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        
        all_countries = response.json()
        
        filtered_countries = []
        for country in all_countries:
            population = country.get('population', 0)
            if population > 30000000:
                country_data = {
                    'name': country.get('name', {}).get('common', 'Unknown'),
                    'capital': country.get('capital', ['Unknown'])[0] if country.get('capital') else 'Unknown',
                    'area': country.get('area', 0),
                    'population': population,
                    'cca2': country.get('cca2', '').lower()  
                }
                filtered_countries.append(country_data)
        
        return filtered_countries
        
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении данных: {e}")
        return []

def calculate_population_density(countries):
    """Вычислить плотность населения для каждой страны"""
    for country in countries:
        area = country['area']
        population = country['population']
        
        if area > 0:
            density = population / area
            country['density'] = round(density, 2)
        else:
            country['density'] = 0
    
    return countries

def save_to_json(data, filename='results.json'):
    """Сохранить данные в JSON файл"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Данные сохранены в файл {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении в файл: {e}")

def print_top_5_by_density(countries):
    """Вывести топ-5 стран по плотности населения"""
    sorted_countries = sorted(countries, key=lambda x: x['density'], reverse=True)
    top_5 = sorted_countries[:5]
    
    print("\n" + "="*60)
    print("ТОП-5 АЗИАТСКИХ СТРАН ПО ПЛОТНОСТИ НАСЕЛЕНИЯ")
    print("(с населением более 30 млн человек)")
    print("="*60)
    
    for i, country in enumerate(top_5, 1):
        print(f"{i}. {country['name']}")
        print(f"   Столица: {country['capital']}")
        print(f"   Плотность населения: {country['density']:.2f} чел/км²")
        print(f"   Население: {country['population']:,} чел")
        print(f"   Площадь: {country['area']:,} км²")
        print("-"*60)
    
    return top_5

def download_flags(top_countries):
    """Скачать PNG флаги для топ-5 стран"""
    flags_dir = "country_flags"
    if not os.path.exists(flags_dir):
        os.makedirs(flags_dir)
        print(f"\nСоздана папка для флагов: {flags_dir}")
    
    print("\n" + "="*60)
    print("СОХРАНЕНИЕ ФЛАГОВ В ФОРМАТЕ PNG")
    print("="*60)
    
    for country in top_countries:
        country_code = country.get('cca2', '').lower()
        country_name = country['name']
        
        if country_code:
            flag_url = f"https://flagcdn.com/w640/{country_code}.png"
            filename = f"{flags_dir}/{country_name.replace(' ', '_')}_flag.png"
            
            try:
                response = requests.get(flag_url)
                response.raise_for_status()
                
                with open(filename, 'wb') as f:
                    f.write(response.content)
                
                print(f"✓ Флаг {country_name} сохранен как: {filename}")
                
            except requests.exceptions.RequestException as e:
                print(f"✗ Ошибка при загрузке флага {country_name}: {e}")
        else:
            print(f"✗ Не найден код страны для {country_name}")

def main():
    """Основная функция приложения"""
    print("="*60)
    print("ПОЛУЧЕНИЕ ДАННЫХ ОБ АЗИАТСКИХ СТРАНАХ")
    print("="*60)
    
    print("\n1. Получение данных с RestCountries API...")
    countries = get_asian_countries()
    
    if not countries:
        print("Не удалось получить данные стран.")
        return
    
    print(f"Найдено {len(countries)} азиатских стран с населением > 30 млн")
    
    print("\n2. Вычисление плотности населения...")
    countries = calculate_population_density(countries)
    
    print("\n3. Сохранение данных в файл results.json...")
    save_to_json(countries)
    print("\n4. Поиск топ-5 стран по плотности населения...")
    top_countries = print_top_5_by_density(countries)
    print("\n5. Загрузка флагов...")
    download_flags(top_countries)
    
    print("\n" + "="*60)
    print("ВСЕ ОПЕРАЦИИ УСПЕШНО ВЫПОЛНЕНЫ!")
    print("="*60)
    print("\nСозданные файлы:")
    print("1. results.json - полные данные о странах")
    print("2. country_flags/ - папка с PNG флагами стран")
    print("="*60)

if __name__ == "__main__":
    main()