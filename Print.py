print(213+231, "Сложение")
print(258-963, "Вычитание")
print(12*96,  "Умножение")
print(5/2, "Деление")
print(5//2, "Целочисленное деление")
print(10%3, "остаток от деления")
print(2**25, "Возведение в степь")


name="Володя"

print("Привет", name)


print(123123213, "Привет", "Бананчик", 37213721, sep="***", end="$$$")
print("Не хочу, чтобы этот текст был на новой строке")


print()












print("Привет Александр")
number1=112
number2=14
number3=112/2
result=(number1*number2+number1/2)
print("Результат равен", result)
print(number1,"*",number2,"+",number3,"=",result)
print("Пройдено шагов", result)

name = input("Пожалуйста введите свое имя ")
print("Привет," , name)


number1 = int(input("введите первое число "))
number2 = int(input("введите второе число "))
print("Сумма равна " , int(number1) + int(number2))


print(type(number1))

print(type(2.5))


import time
import random

from V import V

print("Началась работа программы")
time.sleep(5)
number = random.randint(1, 10)
print("Получившееся число", number)


"""
import random
facels = int(input("Введите число граней "))
print("Бросается кубик")
number = random.randint(1, facels)
print("Кажется выпало число" , number)
"""
"""
import time
import random

timee = int(input("Напиши время: "))
time.sleep(timee)
print("Время прошло")
"""
""""""


city = input("В какой город вы полетите? ")
money = int(input("сколько стоит одна ночь в отеле? "))
day = int(input("Сколько дней вы планируете провести? "))
fly = int(input("сколько стоит один билет на самолет? "))
result = money*day+fly*2

"домашнее задание"

import random

# Получаем от пользователя начало и конец диапазона
start = int(input("Введите начальное значение диапазона: "))
end = int(input("Введите конечное значение диапазона: "))

# Генерируем случайное число в заданном диапазоне
random_number = random.randint(start, end)

# Выводим результат
print(f"Случайное число между {start} и {end}: {random_number}")

"""
Пусть пользователь вводит слово! Задача компьютера - написать какая первая и последняя буквы у данного слова
"""

word = input("Введите любое слово ")
print(f"Первая буква - {word[0]}, последняя буква - {word[len(word)-1]}")


"""
П   Р   И   В   Е   Т
0   1   2   3   4   5

len("привет") -> 6

"""

text = "ПРИВЕТ"
print(text[::-1])

""""""
name = "АлеКсАндр"
name_lower = name.lower()
print(f"Привет\tмир\nНовая строка\n{name_lower}\n{name_lower[1:5]}")
""""""

word = input("введите любое слово ")
print(f"первая буква - {word[0]}, последняя буква - {word[len(word)-1]}")
""""""





print(text[::-2])










""""""

word = input("Введите ваше имя ")
result = len(word)

print(f"в вашем слове {result} букв")
""""""


name = input("Введите ваше имя ")

print(f"Привет, {name} ")





# Получаем от пользователя имя, фамилию и отчество
first_name = input("Введите имя: ")
last_name = input("Введите фамилию: ")
patronymic = input("Введите отчество: ")

# Извлекаем первые буквы из каждого слова и объединяем их
initials = first_name[0] + last_name[0] + patronymic[0]

# Выводим инициалы
print(f"Инициалы: {initials.upper()}")


a=5
b=6

print(a == b)




txt = input("Введите любой текст ")
result = len(txt)
result1 = result - result //2


print(txt[result1:] + txt[:result1])







cups = int(input("Укажите количество стаканов кофе: "))
floor = int(input("На каком этаже вы находитесь? "))

if (cups <= 3 and floor <= 100) or (4 <= cups <= 7 and floor <= 50) or (cups >= 8 and floor <= 2):
    print("Ваш заказ принят!")
else:
    print("К сожалению, мы не можем доставить ваш заказ.")


weight = int(input("Введите вес "))

if weight >= 101 and weight <= 120:
    print("У вас первый юношеский разряд")
elif weight >= 121 and weight <= 130:
    print("У вас второй юношеский разряд")
elif weight >= 131 and weight <= 135:
    print("Кандидат мастера спорта")
elif weight >= 136 and weight <= 140:
    print("Мастер спорта")
else:
    print("Для такого веса нет оценки")


    speed = int(input("Введите скорость "))

if speed >= 48 and speed <= 70:
    print("Проехала машина")
elif speed >= 80 and speed <= 110:
    print("проехал мотоцикл")
elif speed >= 120 and speed <= 330:
    print("Проехал поезд")
elif speed >= 340 and speed <= 990:
    print("Пролетел самолет")
else:
    print("Вид техники не известен")



    magic = input('Вы волшебник? да/нет')

if magic == 'да':
    age = int(input('Введите возраст:'))
    if age <= 17:
         print('Вы приняты!')
    else:
         print('Вы не приняты :(')
else:
    print('Вы не приняты :(')


"""""

Помните парк аттракционов? Вот там теперь новое правило. Всем, кто туда входит, надо сделать приседания. Девочкам, чтобы пройти внутрь, надо присесть больше 40 раз,
а мальчикам больше 20. Вот такой вот парк теперь. Но что поделать - надо написать программу, которая будет определять, пройдет ребенок или нет. Первое, 
что будет введено - это пол ребенка (мальчик или девочка),
а второе - сколько раз он присел.

"""""

transport = input("Введите вид транспорта")
if transport == "Мотоцикл" and "Автомобиль":
if transport == "мотоцикл" and (V>=0 and V<=60):

    
   




   print("Добро пожаловать")

while True:
    password = input('Введите пароль: ')
    if password == 'qwerty123':
        print('Вход выполнен')
        break
    else:
        print('Пароль неверный, попробуйте снова')

print("Здесь что-нибудь ещё")







promocode_used = 0

while promocode_used < 3:
    name = input("Введите своё имя ") 
    promocode = input("Введите промокод ")
    if name == "Вася" and promocode == "caramel":
        print("Вы получили скидку 20 процентов")
        promocode_used = promocode_used + 1

print("Промокоды кончились")





video = input("Введите название фильма")
while video != "stop": 
    video = input("Введите названия фильма еще раз")
    
print("Благодарю за информацию")









slide1 = {'name': 'Кантемир',        'length': 100, 'min_age': 12, 'status': 'closed'}
slide2 = {'name': 'Красный дракон',  'length': 53,  'min_age': 16, 'status': 'open'}
slide3 = {'name': 'Детская',         'length': 5,   'min_age': 7,  'status': 'open'}
slide4 = {'name': 'Закатное солнце', 'length': 20,  'min_age': 16, 'status': 'fix'}
slide5 = {'name': 'Жираф',           'length': 31,  'min_age': 16, 'status': 'open'}

slides = [slide1, slide2, slide3, slide4, slide5]


print(slides[1]["length"])





# словарь с словаре



slides = {
   'Кантемир': {
       'length': 100,
       'min_age': 12,
       'status': 'closed'
   },
   'Красный дракон': {
       'length': 53,
       'min_age': 16,
       'status': 'open'
   },
   'Детская': {
       'length': 5,
       'min_age': 7,
       'status': 'open'
   },
   'Закатное солнце': {
       'length': 20,
       'min_age': 16,
       'status': 'fix'
   },
   'Жираф': {
       'length': 31,
       'min_age': 16,
       'status': 'open'
   }
}

print(slides["Красный дракон"]["length"])





# v1
films = {
   'Магия': [
       ['Гарри Поттер и Философский Камень', 2001],
       ['Фантастические твари и где они обитают', 2016],
       ['Хроники Нарнии', 2005]
       ],
   'Фантастика': [
       ['Матрица', 1999],
       ['Господин Никто', 2000],
       ['Я - начало', 2014]
       ],
   'Космос': [
       ['Интерстеллар', 2014],
       ['Марсианин', 2015],
       ['Пассажиры', 2016]
   ],
   'Marvel': [
       ['Мстители: Война бесконечности', 2018],
       ['Дэдпул', 2016],
       ['Стражи галактики', 2014]
   ]
}

# v2
films = {
   'Магия': {
       'Гарри Поттер и Философский Камень': {"year": 2001},
       'Фантастические твари и где они обитают': {"year": 2016},
       'Хроники Нарнии': {"year": 2005}
   },
   'Фантастика': {
       'Матрица': {"year": 1999},
       'Господин Никто': {"year": 2000},
       'Я - начало': {"year": 2014}
   },
   'Космос': {
       'Интерстеллар': {"year": 2014},
       'Марсианин': {"year": 2015},
       'Пассажиры': {"year": 2016}
   },
   'Marvel': {
       'Мстители: Война бесконечности': {"year": 2001},
       'Дэдпул': {"year": 2016},
       'Стражи галактики': {"year": 2014}
   }
}

















films = {
   'Магия': [
       ['Гарри Поттер и Философский Камень', 2001],
       ['Фантастические твари и где они обитают', 2016],
       ['Хроники Нарнии', 2005]
       ],
   'Фантастика': [
       ['Матрица', 1999],
       ['Господин Никто', 2000],
       ['Я - начало', 2014]
       ],
   'Космос': [
       ['Интерстеллар', 2014],
       ['Марсианин', 2015],
       ['Пассажиры', 2016]
   ],
   'Marvel': [
       ['Мстители: Война бесконечности', 2018],
       ['Дэдпул', 2016],
       ['Стражи галактики', 2014]
   ]
}

for category in films:
    print(category)
    for film in films[category]:
        for er in films[category][film]:
            print(film)
            
            
    

