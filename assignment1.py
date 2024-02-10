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


def findPerson(menArr, womenArr, gender, number):
    
    if gender == 'M':
                #search the menArray:
        whatPerson = menArr[number - 1]
    else: #gender == 'W'
        whatPerson = womenArr[number - 1]
    return whatPerson
                            


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
    #declare 2 arrays: 1 for men, 1 for women
    menArr = []
    womenArr = []
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

        #once we know how many men and women, we can create their objects:
        for i in range(numberOfMen):
            #initilize men
            menArr.append(Person('M', i + 1)) #i+1 because the numbering for the people starts at 1
        for i in range(numberOfWomen):
            #initialize women
            womenArr.append(Person('F', i + 1))
        #continue execution
        #initialize preferences:
        line = file.readline() #this will hold the first line of actual preference data
        while line:
            #keep reading lines until done with file
            lineComponents = line.split()
            tempPeopleArr = []
            for i in range(len(lineComponents)):

                digits = re.findall(r'\d+', lineComponents[i])
                currGender = lineComponents[i][0].upper()
                number = int("".join(digits))
                whatPerson = findPerson(menArr, womenArr, currGender, number)
                tempPeopleArr.append(whatPerson)
            #now, take tempPeopleArr[0] (TPA[0]) and add preferences as:
            # tempPeopleArr[0].preferences = TPA[1], TPA[2], ..., TPA[n]
            targetPerson = tempPeopleArr[0]
            preferences = tempPeopleArr[1:] #subset of the previous array
            targetPerson.initialize_preferences(preferences)

            line = file.readline() #read next line and repeat...

        




    

if __name__ == "__main__":
    main() # execute main