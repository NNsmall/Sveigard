import requests
# сохранение файла html по ссылке
# link = input('Введите адрес сайта для записи в файл:\n')
link = 'https://xn--b1agjltkq.xn--p1ai'
reponce = requests.get(link).text
File = open('save.html', "w", encoding="utf-8")
File.write(reponce)
File.close()
print(reponce)