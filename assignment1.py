# Liam Tolkkinen
# CS 7200
# Assignment 1 (Modified Gale-Shapley algorithm)
# Final Draft due: 02/17/2024

import sys
import re

class Person:
    def __init__(self, gender, number):
        self.gender = gender # gender = M or W
        self.number = number # number > 0

    def initialize_preferences(self, preferences):
        self.preferences = preferences




# Returns a number found in the filename
def getNumber(filename):
    digits = re.findall(r'\d+', filename) # Regex to find the digits in the name
    if not digits:
        return 0
    number = int(''.join(digits))
    return number


def main():
    # default values, forward declaration
    numberOfMen = 0
    numberOfWomen = 0
    # process file name:
    if len(sys.argv) != 2:
        print("make sure to include the file name of the input file!\n")
        sys.exit(1)
    inputFileName = sys.argv[1] # argv[1] contains the second argument (filename)
    fileNumber = getNumber(inputFileName)

    # the next line was used for testing purposes:
    # print("Filename: " + inputFileName + ", number: " + str(fileNumber))
    
    #this is used to filter out the '0' if needed
    if fileNumber > 0: #if greater than 0
        digit = str(fileNumber)
    else: #if equal to 0
        digit = ""

    # for making the output file
    outputFileName = "output" + digit + ".txt" 

    with open(inputFileName, 'r') as file:
        firstLine = file.readline()
        numbers = firstLine.split()
        if len(numbers) == 2: # should always be 2!
            numberOfMen = int(numbers[0])
            numberOfWomen = int(numbers[1])
        
        for i in range(numberOfMen):
            #initilize men

        for i in range(numberOfWomen):
            #initialize women

        #continue execution




    

if __name__ == "__main__":
    main() # execute main