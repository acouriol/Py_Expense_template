from PyInquirer import prompt
user_questions = [
    {
        'type': 'input',
        'name': 'first_name',
        'message': 'What\'s your first name'
    }
]


def add_user():

    answers = prompt(user_questions)
    return answers
