import os
import sys
import pandas as pd
import extract
import transform
import load
def main():
    url='https://drive.google.com/file/d/1xxVEprqDIAMIc9rAIo5LNjAjAzfH2sPq/view?usp=share_link'
    #python3 main.py --help, python3 main.py all, python3 main.py extract примеры вызова программы с аргументами командной строки
    #choice = input("What do you want to do? [extract/transform/load]: ").strip().lower()
    if len(sys.argv) > 1:#Если больше чем один аргумент командной строки(нулевой аргумент это название программы)
        first_argument = sys.argv[1]
        if first_argument == "--help":
            print("=========================================================================")
            print("It is a help command:")
            print("Put 'extract' as first argument to extract data from Google drive")
            print("Put 'all' as first argument to transform data from Google drive")
            print("=========================================================================")
            return 0
        if  first_argument == "extract":
            df = extract.extract(url)
        elif first_argument  == "all":
            # Assume CSV already exists locally
            df = extract.extract(url)
            df = transform.transform(df)
            load.load(df)
    else:
        print("Invalid choice. Please put --help as first argument.")

if __name__ == "__main__":
  main()
