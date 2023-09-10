easy = {'book': 'книга', 'child': 'ребенок', 'country': 'страна', 'friend': 'друг', 'name': 'имя'}
medium = {'group': 'группа', 'home': 'дом', 'lot': 'много', 'married': 'женатый', 'old': 'старый'}
hard = {'place': 'место', 'right': 'правильно', 'state': 'государство', 'age': 'возраст', 'young': 'молодой'}

levels = {
    0: 'Нулевой',
    1: 'Так себе',
    2: 'Можно лучше',
    3: 'Норм',
    4: 'Хорошо',
    5: 'Отлично',
}
answers = {}


def selected_difficulty_level():
    level = input('Выберите уровень сложности:\n'
                  'Легкий, средний, сложный\n')
    print('Выбран уровень сложности, мы предложим 5 слов, подберите перевод\n')

    if level.casefold() in ('легкий', 'лёгкий'):
        return easy
    elif level.casefold() == 'средний':
        return medium
    elif level.casefold() == 'сложный':
        return hard


def print_question(level):
    for key, value in level.items():
        input('Нажмите Enter')

        user_answer = input(f'{key}, {len(value)} букв, начинается на {value[0]}...\n')

        if user_answer.casefold() == value:
            print(f'Верно, {key} это {value}\n')
            answers[key] = True
        else:
            print(f'Неверно, {key} это {value}\n')
            answers[key] = False


def print_result(dictionary):
    correct_answers = []
    incorrect_answers = []

    for word, answer in dictionary.items():
        if answer:
            correct_answers.append(word)
        elif not answer:
            incorrect_answers.append(word)

    print('\nПравильно отвечены слова\n' + '\n'.join(correct_answers))
    print('\nНеравильно отвечены слова\n' + '\n'.join(incorrect_answers))
    print(f'\nВаш ранг:\n'
          f'{levels[len(correct_answers)]}')


if __name__ == '__main__':
    print(print_question(selected_difficulty_level()))
    print_result(answers)


