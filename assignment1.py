# Liam Tolkkinen
# CS 7200
# Assignment 1 (Modified Gale-Shapley algorithm)
# Final Draft due: 02/17/2024

import sys
import re

# Returns a number found in the filename
def getNumber(filename):
    digits = re.findall(r'\d+', filename) # Regex to find the digits in the name
    if not digits:
        return 0
    number = int(''.join(digits))
    return number


def main():
    # process file name:
    if len(sys.argv) != 2:
        print("make sure to include the file name of the input file!\n")
        sys.exit(1)
    inputFileName = sys.argv[1]
    fileNumber = getNumber(inputFileName)
    print("Filename: " + inputFileName + ", number: " + str(fileNumber))
    

if __name__ == "__main__":
    main() # execute main