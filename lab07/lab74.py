import json

def read_json_file(filename):
    """Чтение JSON файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return None
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

def find_translators_by_language(data, language):
    """Поиск переводчиков по языку"""
    result = []
    if isinstance(data, dict) and "translators" in data:
        for translator in data["translators"]:
            if translator.get("language", "").lower() == language.lower():
                result.append(translator)
    return result

def calculate_avg_rate_by_specialization(data):
    """Вычисление средней ставки по специализациям"""
    rates = {}
    if isinstance(data, dict) and "translators" in data:
        for translator in data["translators"]:
            spec = translator.get("specialization")
            rate = translator.get("rate")
            if spec and rate is not None:
                try:
                    rate_val = float(rate)
                    if spec not in rates:
                        rates[spec] = []
                    rates[spec].append(rate_val)
                except:
                    continue
    
    avg_rates = {}
    for spec, rate_list in rates.items():
        if rate_list:
            avg_rates[spec] = sum(rate_list) / len(rate_list)
    
    return avg_rates

def calculate_avg_experience_by_language(data):
    """Вычисление среднего опыта работы по языкам"""
    experiences = {}
    if isinstance(data, dict) and "translators" in data:
        for translator in data["translators"]:
            lang = translator.get("language")
            exp = translator.get("experience_years")
            if lang and exp is not None:
                try:
                    exp_val = float(exp)
                    if lang not in experiences:
                        experiences[lang] = []
                    experiences[lang].append(exp_val)
                except:
                    continue
    
    avg_experiences = {}
    for lang, exp_list in experiences.items():
        if exp_list:
            avg_experiences[lang] = sum(exp_list) / len(exp_list)
    
    return avg_experiences

def save_filtered_data(data, output_filename="out.json"):
    """Сохранение отфильтрованных данных"""
    try:
        filtered = {"translators": []}
        if isinstance(data, dict) and "translators" in data:
            for translator in data["translators"]:
                exp = translator.get("experience_years")
                if exp is not None:
                    try:
                        if float(exp) > 5:
                            filtered["translators"].append(translator)
                    except:
                        continue
        
        with open(output_filename, 'w', encoding='utf-8') as file:
            json.dump(filtered, file, indent=2)
        return True
    except Exception as e:
        print(f"Ошибка сохранения: {e}")
        return False

def main():
    data = read_json_file("11.json")
    if not data:
        return
    
    print("1. Поиск переводчиков по языку")
    language = input("Введите язык: ").strip()
    translators = find_translators_by_language(data, language)
    print(f"Найдено: {len(translators)} переводчиков")
    
    print("\n2. Средняя ставка по специализациям")
    avg_rates = calculate_avg_rate_by_specialization(data)
    for spec, rate in avg_rates.items():
        print(f"{spec}: {rate:.1f}")
    
    print("\n3. Средний опыт работы по языкам")
    avg_exp = calculate_avg_experience_by_language(data)
    for lang, exp in avg_exp.items():
        print(f"{lang}: {exp:.1f} лет")
    
    print("\n4. Сохранение отфильтрованных данных")
    if save_filtered_data(data):
        print("Данные сохранены в out.json")

if __name__ == "__main__":
    main()