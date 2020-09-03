
import sys
import re


#Luis Renteria
#8/31/20
#CS 4375
#Pruitt/Freudenthal

#initializing the input files and dictionary
inputFile = sys.argv[1]
outputFile = sys.argv[2]
dictionary = dict()


with open(inputFile,"r") as inFile:
    #iterating through the lines
    for line in inFile:

        #Making all words lowercase to avoid counting more words than necessary
        line = line.lower()
        #Removing all whitespaces so that they are not counted
        line = line.strip()
        
        fileLine = re.split('\W',line)
        #iterating through every word in the line
        for word in fileLine:

            #if the word is already in the dictionary, increment by one.
            if word in dictionary:
                dictionary[word] +=1
                #If not in dictionary, add to dictionary
            else:
                dictionary[word] = 1


with open(outputFile, "w") as outFile:
    
    #Sorting the dictionary for descending order
    for i in sorted(dictionary.keys()):
        outFile.write(i+" "+str(dictionary[i])+"\n")

    outFile.close()
