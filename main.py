from overhoor import overhoor
from converter import convert

from colorama import init, Fore, Back, Style
from random import randint
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f")
args = parser.parse_args()

def get_data_from_file(filename):
    """ Extracts a list of [question, answer] pairs from the file given"""
    
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
    final_repeat_list = overhoor(DATA)
    # final_repeat_list = overhoor(DATA[:15]) # rehearse first 15 only
    # final_repeat_list = overhoor(DATA[15:30]) # rehearse 15-30 only
    # final_repeat_list = overhoor(DATA[30:45]) # ... etc
    # final_repeat_list = overhoor(DATA[45:60])
    # final_repeat_list = overhoor(DATA[60:75])
    # final_repeat_list = overhoor(DATA[75:90])
    # final_repeat_list = overhoor(DATA[90:105])
    # final_repeat_list = overhoor(DATA[105:120])
    # final_repeat_list = overhoor(DATA[120:135])
    # final_repeat_list = overhoor(DATA[135:150])
    # final_repeat_list = overhoor(DATA[150:165]) 

    while(final_repeat_list):
        final_repeat_list = overhoor(final_repeat_list)

main()