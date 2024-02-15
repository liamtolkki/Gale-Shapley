# Liam Tolkkinen
# CS 7200
# Assignment 1 (Modified Gale-Shapley algorithm)
# Submission 1 submitted: 02/02/2024
# Submission 2 sumitted: 02/10/2024
# Final Draft due: 02/17/2024

import sys
import re

class Person:
    def __init__(self, gender, number):
        self.gender = gender # gender = m or w
        self.number = number # number > 0
        self.partner = None # during initiation, they wont have a partner

    def initialize_preferences(self, preferences):
        self.preferences = preferences
    

    #this is just for testing purposes...
    def toString(self):
        string = ""
        string += self.gender + str(self.number) + ": "
        for person in self.preferences:
            string += person.gender + str(person.number) + " "
        return string

#searches the list of person's preferences
#and returns a weighted number representing person's preference for the other person
def getPriority(person, other):
    return len(person.preferences) - 1 - person.preferences.index(other)


def findPerson(menArr, womenArr, gender, number):
    
    if gender == 'm':
                #search the menArray:
        whatPerson = menArr[number - 1]
    else: #gender == 'w'
        whatPerson = womenArr[number - 1]
    return whatPerson
#returns true or false: true if the woman accepts the proposal,
#false if she rejects it

def propose(man, woman):
    #man proposes to woman
    if woman.partner == None:
        #accept
        woman.partner = man
        man.partner = woman
        return True #paired!    
    if getPriority(woman, man) > getPriority(woman, woman.partner):
        #accept and break up with current partner:
        oldMan = woman.partner
        oldMan.partner = None
        man.partner = woman
        woman.partner = man
        #make him find new partner before proceeding
        for woman_ in oldMan.preferences:
            result = propose(oldMan, woman_)
            if result == True:
                break #dont keep proposing if found a partner

            #this is recursive, but necessary to maintain optimal space complexity
            #it is possible that this man will not find a partner
        return True #because man paired with woman

    else: #woman prefers her current partner (Reject):
        return False




                            


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
            menArr.append(Person('m', i + 1)) #i+1 because the numbering for the people starts at 1
        for i in range(numberOfWomen):
            #initialize women
            womenArr.append(Person('w', i + 1))
        #continue execution
        #initialize preferences:
        line = file.readline() #this will hold the first line of actual preference data
        while line:
            #keep reading lines until done with file
            lineComponents = line.split()
            tempPeopleArr = []
            for i in range(len(lineComponents)):

                digits = re.findall(r'\d+', lineComponents[i])
                currGender = lineComponents[i][0].lower()
                number = int("".join(digits))
                whatPerson = findPerson(menArr, womenArr, currGender, number)
                tempPeopleArr.append(whatPerson)
            #now, take tempPeopleArr[0] (TPA[0]) and add preferences as:
            # tempPeopleArr[0].preferences = TPA[1], TPA[2], ..., TPA[n]
            targetPerson = tempPeopleArr[0]
            preferences = tempPeopleArr[1:] #subset of the previous array
            targetPerson.initialize_preferences(preferences)

            line = file.readline() #read next line and repeat...

    #Uncomment this to test data structuring:

    #for man in menArr:
    #    print(man.toString())
    #for woman in womenArr:
    #    print(woman.toString())
    

    #implement Gale-Shapely Algorithm:
    
    #have m* make proposal to m*.preferences[0] (w*)
    #have w* evaluate the proposal, if w* isn't matched yet, accept
    #if w* is matched:
        #Evaluate:
        #if w* prefers her current partner (m') over m*, reject
            #->m* proposes to next on list after rejection and so on
        #if w* prefers m* over m', leave current partner and accept m*
            #->m' must propose to his next choice on his list
    
    for man in menArr:
        #man proposes through his preferences:
        for woman in man.preferences:
            result = propose(man, woman)
            if result == True:
                break #stop proposing if found best available partner
    
    #output to file:
    outPath = "testing/" + outputFileName
    with open(outPath, 'w') as file:
        #file.write(str(numberOfMen) + " " + str(numberOfWomen) + "\n") #-- Do not need this!
        for man in menArr:
            partnerStr = ""
            if man.partner == None:
                partnerStr = "--"
            else:
                partnerStr = man.partner.gender + str(man.partner.number)
            file.write(man.gender + str(man.number) + " " + partnerStr + "\n")
        for woman in womenArr:
            if woman.partner == None:
                #only write this line to file if woman doesn't have a partner
                file.write("-- " + woman.gender + str(woman.number) + "\n") 
            else:
                continue


        

if __name__ == "__main__":
    main() # execute main