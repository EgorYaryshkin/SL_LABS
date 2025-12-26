import requests
from bs4 import BeautifulSoup
import csv
import time
from typing import List, Dict

DISCIPLINES = {
    '60-metres': '60m',
    '100-metres': '100m',
    '200-metres': '200m',
    '400-metres': '400m'
}
GENDERS = ['men', 'women']
YEARS = range(2024, 2025)  

def construct_url(discipline: str, gender: str, year: int) -> str:
    """Формирует URL страницы с топ-листами."""
    base_url = "https://worldathletics.org/records/toplists/sprints"
    return f"{base_url}/{discipline}/all/{gender}/senior/{year}"

def scrape_top_result(url: str, discipline: str, gender: str, year: int) -> Dict:
    """Извлекает данные о лучшем результате (1-е место) с заданной страницы."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        print(f"Загрузка: {url}")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table')

        if not table:
            print(f"  Таблица с результатами не найдена.")
            return None

        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            if len(cells) >= 8:
                rank = cells[0].get_text(strip=True)
                if rank == '1':
                    mark = cells[1].get_text(strip=True)
                    competitor_cell = cells[3]   
                    competitor_name = competitor_cell.get_text(strip=True)
                    country_code = ""
                    country_span = competitor_cell.find('span')
                    if country_span:
                        country_code = country_span.get_text(strip=True)
                        competitor_name = competitor_name.replace(country_code, '').strip()

                    venue = cells[-2].get_text(strip=True)        
                    date = cells[-1].get_text(strip=True)         

                    result = {
                        'year': year,
                        'discipline': DISCIPLINES[discipline],
                        'gender': 'Men' if gender == 'men' else 'Women',
                        'athlete': competitor_name,
                        'country': country_code,
                        'result': mark,
                        'venue': venue,
                        'date': date
                    }
                    print(f"  Найден: {result['athlete']} - {result['result']}")
                    return result

        print(f"  Результат с 1-м местом не найден в таблице.")
        return None

    except requests.exceptions.RequestException as e:
        print(f"  Ошибка загрузки страницы: {e}")
        return None
    except Exception as e:
        print(f"  Неожиданная ошибка: {e}")
        return None

def scrape_all_data() -> List[Dict]:
    """Основная функция для сбора данных по всем заданным параметрам."""
    all_results = []
    total = len(DISCIPLINES) * len(GENDERS) * len(YEARS)
    current = 0
    print(f"Начинаем скрейпинг {total} страниц...\n")

    for discipline_key in DISCIPLINES.keys():
        for gender in GENDERS:
            for year in YEARS:
                current += 1
                print(f"[{current}/{total}] {DISCIPLINES[discipline_key]} - {gender} - {year}:", end=' ')

                url = construct_url(discipline_key, gender, year)
                result = scrape_top_result(url, discipline_key, gender, year)

                if result:
                    all_results.append(result)

                #time.sleep(1)

    return all_results

def save_to_csv(results: List[Dict], filename: str = 'top_results.csv'):
    """Сохраняет собранные данные в CSV файл."""
    if not results:
        print("\nНет данных для сохранения!")
        return

    fieldnames = ['year', 'discipline', 'gender', 'athlete', 'country', 'result', 'venue', 'date']
    with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"\nДанные успешно сохранены в файл: {filename}")
    print(f"Всего записей: {len(results)}")

if __name__ == "__main__":
    scraped_data = scrape_all_data()
    save_to_csv(scraped_data)