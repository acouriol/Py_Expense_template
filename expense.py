from cmd import PROMPT
import csv
import pprint
from PyInquirer import prompt
from examples import custom_style_2

expense_questions = [
    {
        "type": "input",
        "name": "amount",
        "message": "New Expense - Amount: ",
        "validate":  lambda val: type(val) == int or type(val) == float
    },
    {
        "type": "input",
        "name": "label",
        "message": "New Expense - Label: ",
    },
    {
        "type": "input",
        "name": "spender",
        "message": "New Expense - Spender: ",
        "choices": csv.reader('users.csv'),
    },
    {
        "type": "input",
        "name": "involved",
        "message": "New Expense - People involved: ",
        "choices": csv.reader('users.csv'),
    }

]


def new_expense(*args):

    infos = prompt(expense_questions)

    fd = open('expense_report.csv', 'w')
    count = 0
    writer = csv.DictWriter(fd, 'expense_report.csv')
    writer.writerow(infos)
    fd.close()
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("Expense Added !")
    return True
