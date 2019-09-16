from overhoor import overhoor
from converter import convert

from colorama import init, Fore, Back, Style
from random import randint
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f") # Filename
parser.add_argument("-s") # Start index
parser.add_argument("-e") # End index
args = parser.parse_args()

def get_data_from_file(filename):
    """ Extracts a [[question, answer]] structure from the file given in filename"""
    
    if ".xlsx" in filename:
        DATA = pd.read_excel("excel_files\\" + filename).values 
    elif ".txt" in filename:
        DATA = convert("txt_files\\" + filename)
    return DATA


def main():
    # if to be rehearsed file is given as an argument
    if args.f:
        DATA = get_data_from_file(args.f)
    # otherwise prompt user for filename
    else:
        print("what file do you want to rehearse?")
        response = input()
        DATA = get_data_from_file(response)

    # start rehearsal

    # if start and end point given
    if args.s and args.e:
        DATA = DATA[int(args.s):int(args.e)]
    # if only start point given
    elif args.s:
        DATA = DATA[int(args.s):]
    # if only end point given
    elif args.e:
        DATA = DATA[:int(args.e)]

    final_repeat_list = overhoor(DATA)

    n_wrong = len(final_repeat_list)

    while(final_repeat_list):
        final_repeat_list = overhoor(final_repeat_list)

    n_total = len(DATA)
    print(str(n_total-n_wrong) + "/" + str(n_total)+ " correct on first try.")
    print("Grade: " + str(round((((n_total-n_wrong)/n_total)*10), 1)) + "/10")

main()