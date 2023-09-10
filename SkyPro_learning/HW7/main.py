import json
from config import QUESTIONS_PATH


def load_questions():
    """Загружает вопросы из файла"""
    with open(QUESTIONS_PATH, encoding='utf-8') as file:
        data = json.load(file)
    return data


def show_field(questions):
    """Выводит игровое поле"""
    # questions_category = [category for category in questions]
    for name, question in questions.items():

        print(name)
        for key, value in question.items():
            print(key)
    pass


def parse_input():
    """Делит ввод пользователя на категорию и число"""
    pass


def show_questions():
    """Печатает вопрос"""
    pass


def show_stats():
    """Выводит статистику"""
    pass


def save_result_to_file():
    """Записывает результат в файл JSON"""


if __name__ == '__main__':
    print(show_field(load_questions()))
    # for category, value in questions.items():
    #     # points = dict(value)
    #     for key in value.keys():
    #         print(category, key)
