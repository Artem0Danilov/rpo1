with open("utf-8.txt", "a", encoding="utf-8") as utf_file:
    utf_file.write("мир\n")

with open("windows-1251.txt", "a", encoding="windows-1251") as win_file:
    win_file.write("мир\n")

print("Строка 'мир' добавлена в оба файла.")