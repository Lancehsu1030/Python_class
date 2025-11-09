#使用相對位置讀取names.txt檔案內容
with open('assets/names.txt', encoding="utf-8") as file:
    content = file.read()

names = content.split(',')
names