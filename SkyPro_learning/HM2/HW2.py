questions_answers = {'My name ___ Vova': 'is', 'I ___ a coder': 'am', 'I live ___ Moscow': 'in'}


user_name = input('Привет, предлагаю проверить свои знания английского!\n'
                  'Расскажи, как тебя зовут!\n')
print(f'Привет, {user_name}, начнем тренировку\n')

correct_answers = 0

for question, answer in questions_answers.items():
    user_answer = input(f'Вопрос: {question}\n')

    if user_answer.casefold() == answer:
        correct_answers += 1
        print('Ответ верный!\n'
              'Вы получили 10 баллов!\n')
    else:
        print('Непрвильно.\n'
              f'Правильный ответ: {answer}\n')


print(f'Вот и все {user_name}!\n'
      f'Вы ответили на {correct_answers} из {len(questions_answers)} верно.\n'
      f'Вы заработали {correct_answers * 10} баллов,\n'
      f'Это {int(correct_answers / len(questions_answers) * 100)} процентов!')
