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
    },
    {
        "type": "input",
        "name": "label",
        "message": "New Expense - Label: ",
    },
    {
        "type": "input",
        "name": "spender",
        "message": "New Expemense - Spender: ",
    },

]


def new_expense(*args):

    infos = prompt(expense_questions)

    fd = open('expense-report.csv', 'w')
    count = 0
    writer = csv.DictWriter(fd, 'expense-report.csv')
    writer.writerow(infos)
    fd.close()
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("Expense Added !")
    return True
