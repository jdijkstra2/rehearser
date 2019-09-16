from colorama import init, Fore, Back, Style
from random import randint
import pandas as pd

init() # needed for colorama package

RED  = '\033[31m' # RED
GREEN  = '\033[32m' # GREEN

def overhoor(DATA):
    """ Rehearses a list of [[question, answer]] pairs. It repeats a question if it is answered wrong, and in the end all 
    questions that have been answered wrong are repeated once more (just like in WRTS: https://wrts.nl/signin)"""
    
    n_correct = 0
    n_wrong = 0

    asked_questions_list = []
    
    final_repeat_list = []

    for _ in range(len(DATA)):
        question_number, asked_questions_list = pick_random_new_question(asked_questions_list, DATA)

        user_answer = ask_question(question_number, DATA)

        meaning = get_meaning(question_number, DATA)

        is_correct = check_correct(meaning, user_answer)

        n_correct, n_wrong, final_repeat_list = do_administration(is_correct, question_number, n_correct, n_wrong, final_repeat_list, DATA)

        show_progress(len(DATA), len(asked_questions_list), n_correct, n_wrong)     

    return final_repeat_list


def pick_random_new_question(asked_questions_list, DATA):
    """ Picks a random question that hasn't been answered yet """

    question_number = randint(0, len(DATA)-1)

    while (question_number in asked_questions_list):
        question_number = randint(0, len(DATA)-1)
    asked_questions_list.append(question_number)
    
    return question_number, asked_questions_list


def ask_question(question_number, DATA):
    """ Ask the question to the user and get an answer """
    kanji = DATA[question_number][0]
    print(kanji)
    return input()


def get_meaning(question_number, DATA):
    """ Looks up the meaning of question_number of DATA"""
    return DATA[question_number][1]


def check_correct(correctAnswer, response):
    """ Check if the response matches the meaning"""
    if response == correctAnswer:
        color_print("CORRECT", "GREEN", "black")
        return True
    else:
        color_print(correctAnswer, "RED", "black")
        return False


def do_administration(is_correct, question_number, n_correct, n_wrong, final_repeat_list, DATA):
    if (is_correct):
        n_correct += 1
    else:
        n_wrong += 1
        final_repeat_list.append([DATA[question_number][0], DATA[question_number][1]])
    return n_correct, n_wrong, final_repeat_list


def add_to_repeat_list(questions_to_repeat, question_number):
    if questions_to_repeat:
        questions_to_repeat.append(question_number)
    else:
        # the falses are dummy's, we want to repeat a question answered incorrectly after 2 other words have passed by
        questions_to_repeat.extend([False, False, question_number])
    return questions_to_repeat


def repeat_question(repeat_list, DATA):
    head = repeat_list.pop(0)
    if head:        
        response = ask_question(head, DATA)
        meaning = get_meaning(head, DATA)
        correct = check_correct(meaning, response)
        if not correct:
            if repeat_list:
                repeat_list.append(head)
            else:
                repeat_list.extend([False, False, head])
    return repeat_list


def color_print(msg, foreground, background):
    """ Taken from: https://stackoverflow.com/questions/37340049/how-do-i-print-colored-output-to-the-terminal-in-python 
    Allows for printing to command line in color """
    fground = foreground.upper()
    bground = background.upper()
    style = getattr(Fore, fground) + getattr(Back, bground)
    print(style + msg + Style.RESET_ALL)


def show_progress(n_total, n_asked, n_correct, n_wrong):
    print( str(n_total - n_asked + n_wrong) + " to go, " + str(n_correct) + " correct, " + str(n_wrong) + " wrong")

#TODO: Fix problem where error occurs if last question is answered wrong 



    




