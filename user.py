import csv
from PyInquirer import prompt
user_questions = [
    {
        'type': 'input',
        'name': 'first_name',
        'message': 'What\'s your first name',
        'default': 'New user',
    },

]


def add_user():

    infos = prompt(user_questions)
    fd = open('users.csv', 'w')
    count = 0
    writer = csv.DictWriter(fd, 'users.csv')
    writer.writerow(infos)
    fd.close()
    return infos
