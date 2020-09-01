
import sys
import re


#Luis Renteria
#8/31/20
#CS 4375
#Pruitt/Freudenthal

#initializing the input files and dictionary
imputFile = sys.argv[1]
outputFile = sys.argv[2]
dictionary = {}


with open(inputFile,"r") as inFile:
    #iterating through the lines
    for line in inFile:
        fileLine = re.split('\W',line)

        for word in fileLine:
            
