'''
This is the program for producing the results for question 4 from Assignment 6, 
which is intended to compute the Mandelbrot fractal and print it to an image file.

Author: Adam Biesenbach
Date: March 26, 2015
''' 

import numpy
import matplotlib.pyplot as plt 
from numpy import newaxis

def AnswerQuestionFour():
    """The code to produce the answer to question 4, which includes producing the
    output image file. """
     
    #Define the number of steps to use in creating the grid of values to be used in the Madelbrot iteration. 
    XStep = 100
    YStep = 100 
    
    # Compute a grid of C values in the range of [-2,1]x[-1.5, 1,5].  Fist, define the values used to create the space. 
    #NOTE: Here I picked the step as 100, but this was an arbitrary choice.
    FirstAxis = numpy.linspace(-2, 1, XStep)
    SecondAxis = numpy.linspace(-1.5, 1.5, YStep)
    
    # Use try to raise exceptions for the iteration component of the calculation. 
    MandelbrotIterations = HandleInteratorExceptions(FirstAxis, SecondAxis) 
     
    # Form the 2-d boolean mask indicating which points are in the set.
    some_threshold = 50.
    MandelbrotSet = (abs(MandelbrotIterations) < some_threshold)    
    
    SaveResultstoImage(MandelbrotSet)

def HandleInteratorExceptions(FirstAxis, SecondAxis):
    """ A function for handling errors that arise from the Mandelbrot iteration."""
    try:
        N_max = 50
        # Here we construct the grid. The 'newaxis' object can be used in all slicing operations to create an axis of length one.
        c = FirstAxis[:, newaxis] + 1j*SecondAxis[newaxis,:]
        
        # Perform the Mandelbrot iteration.
        numpy.seterr(invalid ='ignore', over='ignore')
        
        z = c
        for v in range(N_max):
            z = z**2 + c
        return z
  
    except ValueError:
        raise ValueError("Value error") 
          
def  SaveResultstoImage(MandelbrotSet):
    """ A short function for saving the output for question 4."""
    plt.imshow(MandelbrotSet.T, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    return plt.savefig('mandelbrot.png')
    