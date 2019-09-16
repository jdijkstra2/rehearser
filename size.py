from converter import convert

import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("-f")
args = parser.parse_args()

def main():
    if args.f:
        if ".xlsx" in args.f:
            DATA = pd.read_excel("excel_files\\" + args.f).values 
            print(len(DATA))
        elif ".txt" in args.f:
            DATA = convert("txt_files\\" + args.f)
            print(len(DATA))
    return

main()
