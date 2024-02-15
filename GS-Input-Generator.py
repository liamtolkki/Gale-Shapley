#This program is solely intended for making input files
#for assignment1.py
#it will output a random preference listing 
#for a random number of men and women
import random


class Person:
    def __init__(self, gender, number):
        preferences = [] #blank preferences array
        self.gender = gender
        self.number = number


def main():
    menArr = []
    womenArr = []    
    menCount = int(input("How many men? "))
    womenCount = int(input("How many women? "))
    fileNm = str(input("Name of file? (Ex: \"input3.txt\") "))

    #Initialize the arrays of men and women:
    for i in range(menCount):
        menArr.append(Person("m", i + 1)) #i + 1 because it cant start at 0
    for i in range(womenCount):
        womenArr.append(Person("w", i + 1))
    
    #so that we can have a copy
    menArrCpy = menArr[:]
    womenArrCpy = womenArr[:]
    #Initialize preferences: (Random)
    for man in menArr:
        #shuffle the array of women and make it the preference list
        random.shuffle(womenArr)
        man.preferences = womenArr[:]
    for woman in womenArr:
        #shuffle the array of women and make it the preference list
        random.shuffle(menArr)
        woman.preferences = menArr[:]
    path = "testing/" + fileNm
    with open(path, "w") as file:
        file.write(str(menCount) + " " + str(womenCount) + "\n") #write the men/women numbers
        for man in menArrCpy:
            file.write(man.gender + str(man.number) + " ") #print man, then preferences
            for woman in man.preferences:
                file.write(woman.gender + str(woman.number) + " ")
            file.write("\n") #new line
        for woman in womenArrCpy:
            file.write(woman.gender + str(woman.number) + " ")
            for man in woman.preferences:
                file.write(man.gender + str(man.number) + " ")
            file.write("\n")




    


main()