def convert_to_lowercase(input_file, output_file):
    """
    Читает файл input_file, переводит все слова в каждой строке в нижний регистр
    и записывает результат в output_file
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
        
        processed_lines = []
        for line in lines:
            lower_line = line.lower()
            processed_lines.append(lower_line)
        
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.writelines(processed_lines)
        
        print(f"Обработка завершена! Результат записан в файл '{output_file}'")
        print(f"Обработано строк: {len(processed_lines)}")
        
    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден!")
    except IOError as e:
        print(f"Ошибка ввода-вывода: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

if __name__ == "__main__":
    input_filename = "input.txt"
    output_filename = "output.txt"
    
    convert_to_lowercase(input_filename, output_filename)
    
    try:
        print("\n" + "="*50)
        print("СОДЕРЖИМОЕ ВХОДНОГО ФАЙЛА:")
        print("="*50)
        with open(input_filename, 'r', encoding='utf-8') as f:
            print(f.read())
    except:
        pass
    
    try:
        print("\n" + "="*50)
        print("СОДЕРЖИМОЕ ВЫХОДНОГО ФАЙЛА:")
        print("="*50)
        with open(output_filename, 'r', encoding='utf-8') as f:
            print(f.read())
    except:
        pass