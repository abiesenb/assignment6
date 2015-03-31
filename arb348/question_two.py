'''
This is the program for producing the results for question 2 from Assignment 6.

Author: Adam Biesenbach
Date: March 26, 2015
''' 

import numpy

def AnswerQuestionTwo():
    """ A function that produces the divides one given array by another and 
     prints the results. the 'arrange' creates evenly spaced elements. Reshape 
     changes the dimensions. """
     
    # Create initial array.
    a = numpy.arange(25).reshape(5, 5)
    aTransposed = numpy.transpose(a)
    
    # Divide each column element-wise by the following array:
    b = numpy.array([1., 5, 10, 15, 20])
    
    # To perform the column-wise division, I first transposed the array, 
    # then use the divide method. Afterward, I transpose the array again to its
    # original dimensions,
    
    Question2Answer = numpy.divide(aTransposed, b)
    Question2Answer = numpy.transpose(Question2Answer)

    return Question2Answer
