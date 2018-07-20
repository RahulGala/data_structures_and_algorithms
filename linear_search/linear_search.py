#!/usr/bin/python2.7 -tt

#Notes:
#to run type: python linear_search.py in terminal
#you can change the number in array thevalues

import sys
            
def main():
    thevalues = [1, 2, 3 , 4, 5, 6, 7, 8, 9, 10]
    target = 6
    linearsearch(thevalues, target)

def linearsearch(thevalues, target):
    n = len(thevalues)
    for i in range (n):
        if thevalues[i] == target:
            print("match found")  

if __name__== '__main__':
    main()
