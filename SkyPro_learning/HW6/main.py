from utils.HW6 import get_word, save_player_score, get_statistics_from_file, shuffle_word
from config import WORDS_PATH, HISTORY_PATH

if __name__ == '__main__':
    user_name = input('Введите ваше имя\n')
    user_points = 0

    for word in get_word(WORDS_PATH):
        user_answer = input(f'Угадайте слово: {shuffle_word(word)}\n')

        if user_answer.casefold() == word:
            print(f'Верно! Вы получаете 10 очков.\n')
            user_points += 10
        else:
            print(f'Неверно! Верный ответ - {word}.\n')

    save_player_score(HISTORY_PATH, user_name, user_points)

    stats = get_statistics_from_file(HISTORY_PATH)

    print(f'Всего игр сыграно: {stats.get("games_played")}\n'
          f'Максимальный рекорд: {stats.get("max_score")}\n')
