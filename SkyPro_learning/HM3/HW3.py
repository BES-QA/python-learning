questions = ['My name ___ Vova', 'I ___ a coder', 'I live ___ Moscow']
answers = ['is', 'am', 'in']

user_answers = []


def send_questions(questions, answers):
    num_question = 0

    for question in questions:
        num_question += 1

        user_answer = input(f'Вопрос №{num_question}: {question}\n')

        if user_answer.casefold() == answers[num_question - 1]:
            print('Ответ Верный!\n')
            user_answers.append(True)
        else:
            print(f'Неправильно. Правильный ответ: {answers[num_question - 1]}\n')
            user_answers.append(False)



if __name__ == '__main__':
    ready_or_not = input('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать\n')

    if not ready_or_not.casefold() == 'ready':
        print('Кажется вы не хотите играть. Очень жаль.')
    else:
        send_questions(questions, answers)

    print(f'Вот и все вы ответили на {user_answers.count(True)} вопросов из {len(questions)} верно, это {round(user_answers.count(True) / len(questions) * 100, 2)} процентов')