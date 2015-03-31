'''
This is the program for producing the results for question 1 from Assignment 6.

Author: Adam Biesenbach
Date: March 26, 2015
''' 

import numpy

def AnswerQuestionOne():
    """Perform the calculations necessary to answer question 1 from Assignment 6."""
    
    # Create the functions first array. 
    InitialArray = CreateInitialArray()
    
    # Create a number array containing the 2nd and 4th rows.   
    Question1PartAArray =  InitialArray[[1, 3], :]

    # Generate a new array containing the second column. 
    Question1PartBArray =  InitialArray[:, 1]

    # Generate a new array that contains the elements in the 
    # rectangular section between [1,0] and [3,2].
    Question1PartCArray =  InitialArray[1:4, 0:3]

    # Generate a new array where the elements are between 3 and 11.
    Question1PartDArray  = InitialArray[(InitialArray>3) & (InitialArray<11)]
  
    return (InitialArray, Question1PartAArray, Question1PartBArray, Question1PartCArray, Question1PartDArray)

def CreateInitialArray():
    """creates the specific array requested in question 1."""
    return numpy.arange(1,16,1).reshape((3,5)).transpose()

