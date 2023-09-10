import random


def get_word(path):
    """Получает все слова из файла"""
    with open(path, 'r', encoding='utf=8') as file:
        lines = file.read()
        words = lines.splitlines()
        return words


def shuffle_word(word):
    """Перемешивает буквы в слове"""
    new_word = list(word)
    random.shuffle(new_word)
    return ''.join(new_word)


def save_player_score(path, player_name, player_score):
    """Сохраняет имя и результат пользователя в файл"""
    with open(path, 'a', encoding='utf=8') as f:
        f.write(f'\n{player_name} {player_score}')


def get_statistics_from_file(path):
    with open(path, encoding='utf=8') as f:
        """Подсчитывает статистику, записывает в 
           файл и выводит лучший результат"""
        max_score = 0
        lines = f.readlines()

        for line in lines:
            score = int(line.split(' ')[-1])

            if max_score < score:
                max_score = score

    return {'max_score': max_score, 'games_played': len(lines)}
