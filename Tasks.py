## 1. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

# line1 = 'привет мир, привет друзья'
# line2 = 'привет'
# list = line1.split(" ")
# count = 0
# for i in list:
#     if i == line2:
#         count += 1
# print(count)

## Другой способ

# str1 = 'привет мир, привет коллеги, привет друзья'
# str2 = 'привет'
# print(str1.count(str2))



## Создать генерацию рандомного числа

# import datetime
# print(datetime.datetime.now().microsecond % 100)



## Определить, присутствует ли в заданном списке строк, некоторое число

# line1 = ['my', 'name', 'is', 'Dima', 'hi', 'everyone', '!', '1']

# def find_digit(line2):
#     for i in range(len(line2)):
#         if line2[i].isdigit():
#             print(i)
# find_digit(line1)


## таже задача только поиск конкретного числа

# line1 = ['5', '8', '32', '55', '7', '8']
# num = 8
# def find_digit(line2, num):
#     for i in range(len(line2)):
#         if line2[i].isdigit():
#             if int(line2[i]) == num:
#                 print(i)
# find_digit(line1, num)

## таже задача только поиск конкретного числа из списка букв и цифр

# line1 = ['5', 'sftgjh8', 'stdfh32', '2sht55', '7', '8']
# num = 5
# def find_digit(line2, num):
#     for i in range(len(line2)):
#         for j in line2[i]:
#             if j.isdigit():
#                 if int(j) == num:
#                     print(i)
#                     break # Закрывает текущий список
# find_digit(line1, num)


## Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# line1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# key_word = 'qwe'
# def find_coincidence(line2, key):
#     count = 0
#     for i in range(len(line2)):
#         if line2[i] == key:
#             count += 1
#             if count == 2:
#                 print(i)
#                 break
#     if count < 2:
#         print('-1')
# find_coincidence(line1, key_word)


## Другой ответ, когда только одно вхождение чтобы получить -1

# text_1 =["qwe", "asd", "zxc", "ertqwe"]
# key_word = "qwe"
# def find_coincidence(new_text, key):
#     count = 0
#     for i in range(len(new_text)):
#         if new_text[i] == key:
#             count += 1
#             if count == 2:
#                 print(i)
#                 break
#     if count < 2:
#         print("-1")
            
# find_coincidence(text_1, key_word)



