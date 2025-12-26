import pickle

cities_temp = {
    "Москва": {"2017": 6.5, "2018": 7.2, "2019": 5.8, "2020": 7.9, "2021": 6.3, "2022": 7.1},
    "Сочи": {"2017": 14.8, "2018": 15.2, "2019": 14.1, "2020": 15.6, "2021": 14.9, "2022": 15.4},
    "Новосибирск": {"2017": 2.1, "2018": 2.8, "2019": 1.5, "2020": 3.2, "2021": 2.4, "2022": 2.9},
    "Санкт-Петербург": {"2017": 5.8, "2018": 6.1, "2019": 4.9, "2020": 6.5, "2021": 5.7, "2022": 6.3},
    "Екатеринбург": {"2017": 3.2, "2018": 3.8, "2019": 2.7, "2020": 4.1, "2021": 3.5, "2022": 3.9},
    "Владивосток": {"2017": 5.1, "2018": 5.3, "2019": 4.8, "2020": 5.6, "2021": 5.2, "2022": 5.5},
    "Краснодар": {"2017": 12.5, "2018": 12.9, "2019": 11.8, "2020": 13.2, "2021": 12.7, "2022": 13.1}
}

print("1. Список городов и средние температуры в них:")
print("-" * 50)
for city, temps in cities_temp.items():
    avg_temp = sum(temps.values()) / len(temps)
    print(f"{city}: средняя температура за 6 лет = {avg_temp:.2f}°C")
print()

print("2. Год с максимальной температурой для каждого города:")
print("-" * 50)
for city, temps in cities_temp.items():
    max_temp_year = max(temps.items(), key=lambda x: x[1])
    print(f"{city}: {max_temp_year[0]} год ({max_temp_year[1]}°C)")
print()

print("3. Города, где 2019 год был самым холодным:")
print("-" * 50)
coldest_2019_cities = []
for city, temps in cities_temp.items():
    coldest_year = min(temps.items(), key=lambda x: x[1])
    if coldest_year[0] == "2019":
        coldest_2019_cities.append(city)
        print(f"{city}: минимальная температура в 2019 году = {coldest_year[1]}°C")
print(f"Всего городов: {len(coldest_2019_cities)}")
print()

print("4. Города, где температура в 2017 году была выше, чем в 2018 более чем на 1 градус:")
print("-" * 50)
temp_diff_cities = []
for city, temps in cities_temp.items():
    if "2017" in temps and "2018" in temps:
        diff = temps["2017"] - temps["2018"]
        if diff > 1:
            temp_diff_cities.append(city)
            print(f"{city}: 2017 - {temps['2017']}°C, 2018 - {temps['2018']}°C, разница = {diff:.1f}°C")
print(f"Всего городов: {len(temp_diff_cities)}")
print()

print("5. Сохранение данных в файл data.pickle...")
try:
    with open('data.pickle', 'wb') as f:
        pickle.dump(cities_temp, f)
    print("Данные успешно сохранены в файл 'data.pickle'")
    
    with open('data.pickle', 'rb') as f:
        loaded_data = pickle.load(f)
    print("Данные успешно загружены из файла (проверка)")
    print(f"Загружено записей о городах: {len(loaded_data)}")
    
except Exception as e:
    print(f"Ошибка при работе с файлом: {e}")

print("\n" + "="*60)
print("ПОЛНЫЙ ОБЗОР ДАННЫХ:")
print("="*60)
for city, temps in cities_temp.items():
    print(f"\n{city}:")
    for year, temp in sorted(temps.items()):
        print(f"  {year}: {temp}°C")
    avg = sum(temps.values()) / len(temps)
    print(f"  Средняя за 6 лет: {avg:.2f}°C")