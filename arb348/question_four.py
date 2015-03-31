'''
This is the program for producing the results for question 4 from Assignment 6, 
which is intended to compute the Mandelbrot fractal and print it to an image file.

Author: Adam Biesenbach
Date: March 26, 2015
''' 

import numpy
import matplotlib.pyplot as plt 
import warnings 

def AnswerQuestionFour():
    """The code to produce the answer to question 4, which includes producing the
    output image file. """
     
    #Compute the Mandelbrot mask.
    MandelbrotMask = ComputeGrid()
    
    # Save the results to an image file.
    SaveResultstoImage(MandelbrotMask)
     
       
def ComputeGrid():  
    """The code to compute the grid used in the Mandelbrot calculation. """
    with warnings.catch_warnings():
        warnings.filterwarnings('error') 
        return HandleComputeGrid()
        

def HandleComputeGrid():
    """ Handle an exception in case the iteration overflows."""
    
    # NOTE: There is an overflow warning that might be generated if the N_Max variable is set too high. 
    try:
        (xRange, yRange, mask, N_max, some_threshold) = SetVariables()
        # Construct the grid. 
        for x in range(xRange.size):   
            for y in range(yRange.size):      
                c = xRange[x] + 1j*yRange[y]
                # Perform the Mandelbrot iteration.
                z = c
                for v in range(N_max):
                    z = z**2 + c
                    # Change mapping to False if threshold is reached.
                    if abs(z) >= some_threshold:
                        mask[x,y] = False
                        break
    except Warning: 
        print "Runtime Warning: in Question 4, an overflow occurred when you tried to run the Mandelbrot iteration."
    finally:
        return mask
    
def SetVariables():
    """ Initialize some variables that are needed in the program, including the 
    step sizes for the grid we create and some threshold numbers for computing
    the mask. """
    
    xStep = 0.01
    yStep = 0.01
    xStart = -2
    xEnd = 1
    yStart = -1.5
    yEnd = 1.5
    N_max = 50
    some_threshold = 50
    
    # Create each of the arrays for the two axes, that will eventually 
    # be used to create the grid.
    
    xRange = numpy.arange(xStart, xEnd, xStep)
    yRange = numpy.arange(yStart, yEnd, yStep)
    
    # Construct the initial mask, which is a Boolean of all true values.
    mask = numpy.ones((xRange.size, yRange.size), dtype = bool)
    return (xRange, yRange, mask, N_max, some_threshold)

def SaveResultstoImage(MandelbrotSet):
    """ A short function for saving the output for question 4."""
        
    plt.imshow(MandelbrotSet.T, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    return plt.savefig('mandelbrot.png')    