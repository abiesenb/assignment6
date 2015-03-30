'''
This is programming for Assignment 6. This is the main program which will 
generate my answers for the assignment, which deals with programming in NumPy.
Each of the questions from the assignment has its own module, and from each module 
we import the function responsible for generating the required output.

Author: Adam Biesenbach
Date: March 26, 2015

'''

from question_one import AnswerQuestionOne
from question_two import AnswerQuestionTwo
from question_three import AnswerQuestionThree
from question_four import AnswerQuestionFour

if __name__ == '__main__':
    # Run the function for question 1. 
    
    (InitialArray, Question1PartAArray, Question1PartBArray, Question1PartCArray, Question1PartDArray) = AnswerQuestionOne()
       
    print "Question 1 'Initial' array: "
    print InitialArray       
    print ""
  
    # Create a number array containing the 2nd and 4th rows.   
    print "Question 1 Part A array: "
    print Question1PartAArray   
    print ""
    
    # Generate a new array containing the second column. 
    print "Question 1 Part B array: "
    print Question1PartBArray     
    print ""
    
    # Generate a new array that contains the elements in the 
    # rectangular section between [1,0] and [3,2].
    print "Question 1 Part C array: "
    print Question1PartCArray         
    print ""

    print "Question 1 Part D array: "
    print Question1PartDArray      
    print ""

    # Run the function for question 2.
    Question2Answer = AnswerQuestionTwo()
    print "Question 2 array: "   
    print Question2Answer
    print ""
    
    # Run the function for question 3.
    QuestionThreeOutput = AnswerQuestionThree()
    print "Question 3 array: "
    print QuestionThreeOutput
    print ""
    
    # Run the function for question 4.
    AnswerQuestionFour()