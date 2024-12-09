#
def process_file(file_name, encoding):
    try:

        with open(file_name, "r", encoding=encoding) as file:
            content = file.read()


        content += " мир"


        with open(file_name, "w", encoding=encoding) as file:
            file.write(content)

        print(f"Файл '{file_name}' успешно обновлён.")
    except Exception as e:
        print(f"Ошибка при обработке файла '{file_name}': {e}")


files = [
    ("C:/Users/Пользователь/Desktop/rpo1-timofej/file1.txt", "utf-8"),
    ("C:/Users/Пользователь/Desktop/rpo1-timofej/file2.txt", "windows-1251")
]


for file_name, encoding in files:
    process_file(file_name, encoding)