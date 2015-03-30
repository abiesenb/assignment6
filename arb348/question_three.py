'''
This is the program for producing the results for question 3 from Assignment 6.

Author: Adam Biesenbach
Date: March 26, 2015
''' 

import numpy

def AnswerQuestionThree():
    """ Write a module to generate a 10X3 array of random numbers in the range [0,1]."
    It includes use of the argsort, transpose, choose and other numpy functionality."""
    
    InitialArray = numpy.random.rand(10,3)
    
    # For each row, pick the number closest to 0.5. 'argsort' returns an array that would sort the array 
    # fed as input. So here, we take the distance between the InitialArray values
    # and 0.5, and find the index values of the minimum elements (i.e the first column, or [:,0]. 
    # Then, use the choose attribute to construct an array from that index array.
              
    Question3PartAArray = numpy.argsort(abs(InitialArray - 0.5))[:,0].choose(InitialArray.transpose())
        
    # We can use what we have in part (A) to answer the same question.         
    Question3PartBArray = numpy.argsort(abs(InitialArray - 0.5))[:,0]
    
    # Use fancy indexing to extract the numbers into an array.
    # For all the values from 0 to the number of elements in Question2PartBArray (in this case 10 elements),
    # select 
    Question3PartCArray = numpy.asarray([InitialArray[j, Question3PartBArray[j]] for j in range(0, Question3PartBArray.size)])
    
    return Question3PartCArray