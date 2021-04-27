from random import *

words = []
with open('py_file.txt', 'r', encoding='utf8') as file:
    for i in file:
        words.append(i.replace('\n', ''))
word = choice(words).lower()  # рандом случайного значения из списка слов

print('***Добро пожаловать в игру "угадайка слов", у вас есть 10 попыток чтобы отгадать слово***')
print(word)
pole = "*" * len(word)  # создали поле в которое будут помещаться буквы введенные пользователем


def retur(n):
    print("Слово -", pole)


def check(l):  # функция проверка на соответствие символов выводит только текст если символ не соответствует

    if l in '1234567890':
        print('Цифры не используются!')
        retur(pole)
        return True
    elif 64 < ord(l) < 123:
        print('Использовать только русские буквы!')
        retur(pole)
        return True
    elif l in '!@#$%^&*()_+=-?:;№"\|^/\<>.,':
        print('Знаки не использовать!')
        retur(pole)
        return True


def win():
    if count == 0 and pole != word:
        print("***************")
        print('\033[31mВы проиграли...')
        print(f'А слово было\033[31m"{word}"')
        return False
    elif pole == word:
        print("\033[34m**победа**")
        return False


def func(a, wor):
    global pole
    pole = list(pole)
    for i in range(len(wor)):
        if wor[i] == a:
            pole[i] = a
    pole = ''.join(pole)
    return pole


if  10 <=len(word) <=15:  # выставляю начальное значение коунта в зависимости от длинны слова
    count = 11
elif len(word)<10:
    count = 14
elif len(word)>15:
    count=17

retur(pole)
print(f'Колличество букв в слове -{len(word)}')
print(f'Колличество возможных ошибок -{count}')
while True:

    print('---------------')
    k = input('Введите одну букву').lower()
    if len(k) != 1:
        count -= 1
        print('Введите только один символ!')
        print(f'Колличество оставшихся попыток--{count}')
    elif len(k) == 1 and check(k) == True:
        count -= 1
        print(f'Колличество оставшихся попыток--{count}')
    elif k not in word:
        count -= 1
        print('К сожалению такой буквы в слове нет')
        print(f'Колличество оставшихся попыток--{count}')
        retur(pole)
    elif (k in word) and (k not in pole):
        func(k, word)
        retur(pole)
    elif (k in word) and (k in pole):
        count -= 1
        print('Эту букву вы уже отгадали!')
        print(f'Колличество оставшихся попыток--{count}')
        retur(pole)
    if win() == False:
        break
