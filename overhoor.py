from colorama import init, Fore, Back, Style
from random import randint
import pandas as pd

init() # belongs to colorama

RED  = '\033[31m' # RED
GREEN  = '\033[32m' # GREEN

def overhoor(DATA):
    """ Rehearses a list of [[question, answer]] pairs. It repeats a question if it is answered wrong, and in the end all 
    questions that have been answered wrong are repeated once more (just like in WRTS)"""

    asked_questions = []                # list of indices (Integers) of answered questions
    intermediate_repeat_list = []       # list of indices (Integers) of -incorrectly- answered questions to be repeated during the rehearsal
    final_repeat_list = []              # list of indices (Integers) of -incorrectly- answered questions to be repeated in the end

    n_correct = 0
    n_wrong = 0

    for _ in range(len(DATA)):
        # pick next question
        index, asked_questions = pick_question(asked_questions, DATA)

        # get user response
        meaning, response = ask_question(index, DATA)

        # check if answer is correct
        isCorrect = check_correct(meaning, response)
        if (isCorrect):
            n_correct += 1
        else:
            n_wrong += 1
            final_repeat_list.append(DATA[index])
            if intermediate_repeat_list:
                intermediate_repeat_list.append(index)
            else:
                # the falses are dummy's, we want to repeat a question answered incorrectly after 2 other words have passed by
                intermediate_repeat_list.extend([False, False, index])

        # show how many words are left and how well you are doing
        print_progress(len(DATA), len(asked_questions), n_correct, n_wrong)
    
        # if there is a question to be repeated, repeat it
        if intermediate_repeat_list:
            intermediate_repeat_list = repeat_question_if_necessary(intermediate_repeat_list, DATA)

    return final_repeat_list


def pick_question(asked_questions, DATA):
    """ Picks a random question that hasn't been answered yet """

    index = randint(0, len(DATA)-1)
    while (index in asked_questions):
        index = randint(0, len(DATA)-1)
    asked_questions.append(index)
    return index, asked_questions


def ask_question(pairIndex, DATA):
    """ Ask the question to the user and get an answer """

    kanji = DATA[pairIndex][0]
    meaning = DATA[pairIndex][1]
    print(kanji)
    return meaning, input()


def check_correct(correctAnswer, response):
    """ Check if the response matches the meaning"""
    
    if response == correctAnswer:
        cprint("CORRECT", "GREEN", "black")
        return True
    else:
        cprint(correctAnswer, "RED", "black")
        return False


def repeat_question_if_necessary(repeat_list, DATA):
    head = repeat_list.pop(0)
    if head:
        meaning, response = ask_question(head, DATA)
        isCorrect = check_correct(meaning, response)
        # if again wrong -> put in repeatList again
        if not isCorrect:
            if repeat_list:
                repeat_list.append(head)
            else:
                repeat_list.extend([False, False, head])
    return repeat_list


def cprint(msg, foreground, background):
    """ Taken from: https://stackoverflow.com/questions/37340049/how-do-i-print-coloRED-output-to-the-terminal-in-python """
    fground = foreground.upper()
    bground = background.upper()
    style = getattr(Fore, fground) + getattr(Back, bground)
    print(style + msg + Style.RESET_ALL)


def print_progress(n_total, n_asked, n_correct, n_wrong):
    print( str(n_total - n_asked) + " to go, " + str(n_correct) + " correct, " + str(n_wrong) + " wrong")



    




