def easy_task_1():
    user_name = input('Введите имя: ')
    print(f'Ваше имя: {user_name}')


def easy_task_2():
    user_num = int(input('Введите число: '))
    print(f'Сумма = {user_num + 2}')


def easy_task_3():
    user_age = float(input('Введи ваш возраст: '))
    if user_age < 18:
        print('Извините, пользование данным ресурсом только с 18 лет')
    else:
        print('Доступ разрешен')


def normal_task_1():
    # num = float(input('Введите число в промежутке от 0 до 10: '))
    # while num > 10:
    #     num = float(input('Вы ввели не верное число, введите число от 0 до 10: '))
    # else:
    #     print(num ** 2)

    while True:
        num = float(input('Введите число в промежутке от 0 до 10: '))
        if 0 < num < 10:
            print(num ** 2)
            break
        else:
            print('Вы ввели не верное число')


def normal_task_2():
    a = input('Введите первое значение: ')
    b = input('Введите второе значение: ')

    a, b = b, a
    print(a, b)


def hard_task():
    fio = input('Введите ваше ФИО: ')
    age = int(input('Введите ваш возраст: '))
    weight = float(input('Введите ваш вес: '))

    if(age < 30) and (50 < weight < 120):
        print(f'{fio}, {age} год, вес {weight} - хорошее состояние')
    elif(age > 40) and (50 > weight or weight > 120):
        print(f'{fio}, {age} год, вес {weight} - следует обратиться к врачу!')
    elif(age > 30) and (50 > weight or weight > 120):
        print(f'{fio}, {age} год, вес {weight} - следует заняться собой')


if __name__ == '__main__':
    # easy_task_1()
    # easy_task_2()
    # easy_task_3()
    # normal_task_1()
    # normal_task_2()
    hard_task()
