# file_writer.py

# Функция для записи строки в файл с указанной кодировкой
def append_to_file(filename, text, encoding):
    with open(filename, 'a', encoding=encoding) as f:
        f.write(text)

# Основная программа
if __name__ == "__main__":
    append_to_file("utf-8.txt", "мир\n", "utf-8")
    append_to_file("windows-1251.txt", "мир\n", "windows-1251")
