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

    fd = open('users.csv', 'w')
    count = 0
    infos = prompt(user_questions)

    for val in infos:
        if count == 0:
            
            header = val.keys()
            fd.writerow(header)
            count += 1
 
        fd.writerow(val.values())

    fd.close()
    return infos
