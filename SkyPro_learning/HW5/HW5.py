import random

en_words = ['code', 'bit', 'list', 'soul', 'next']
MORSE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.',
              'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..',
              'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---',
              'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-',
              'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..',

              '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....',
              '6': '-....', '7': '--...', '8': '---..',
              '9': '----.'
              }
user_answers = []


def get_word(dictionary):
    return random.choice(dictionary)


def morse_encode(sentence):
    morse_word = []
    for letter in sentence:
        morse_word.append(MORSE_DICT.get(letter.upper(), ''))

    return ' '.join(morse_word)


def print_questions(dictionary):
    for i in range(len(dictionary)):
        word = get_word(dictionary)
        morse_word = morse_encode(word)
        print(word)
        user_answer = input(f'Слово {i+1} - {morse_word}\n')

        if user_answer.casefold() == word:
            print(f'Верно {word}\n')
            user_answers.append(True)
        else:
            print(f'Неверно {word}\n')
            user_answers.append(False)


def print_statistics(answers):
    print(f'Всего задачек {len(answers)}')
    print(f'Отвечено верно {answers.count(True)}')
    print(f'Отвечено неверно {answers.count(False)}\n')


if __name__ == '__main__':
    input('Сегодня мы потренируемся расшифровывать морзянку.\n'
          'Нажмите Enter и начнем\n')

    print_questions(en_words)
    print_statistics(user_answers)

