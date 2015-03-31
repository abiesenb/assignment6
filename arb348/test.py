'''
Created on Mar 29, 2015
@author: Adam Biesenbach

This file contains tests for the functions used to answer assignment #6. Test's for question 
1 work by creating the file we know we want from the question prompt and ensuring that the output from the question 1 
functions create it. For the other questions, we verify that the answers we create have the right length, dimensions, etc.
'''
import unittest
import numpy
import os.path
from question_one import AnswerQuestionOne
from question_two import AnswerQuestionTwo
from question_three import AnswerQuestionThree

class TestAssignment6Functions(unittest.TestCase):
    """This class provides the structure for the unit testing we perform for each
    function responsible for creating the answers to Assignment 6."""
    
    def testQuestionOne(self):   
        """ Test to ensure that Question 1's output is correct."""
        
        # First generate the values we should be getting, to test the values actually produced by our functions. 
        self.QuestionOneInitArray = numpy.array([[1, 6,11], [2, 7,12], [3, 8,13], [4, 9,14], [5, 10, 15]])
        self.QuestionOneAArray = numpy.array([[2, 7, 12], [4, 9, 14]])       
        self.QuestionOneBArray = numpy.array([6, 7, 8, 9, 10])
        self.QuestionOneCArray = numpy.array([[2, 7, 12], [3, 8, 13], [4, 9, 14]])
        self.QuestionOneDArray = numpy.array([6, 7, 8, 4, 9, 5, 10])
       
        # Check to make sure that the initial array used in Q1 is the same as the one we want. 
        self.assertTrue((AnswerQuestionOne()[0] == self.QuestionOneInitArray).all(), "Question one's initial array is not correct.")                 
        self.assertTrue((AnswerQuestionOne()[1] == self.QuestionOneAArray).all(), "Question one part A array is not correct.")                 
        self.assertTrue((AnswerQuestionOne()[2] == self.QuestionOneBArray).all(), "Question one part B array is not correct.")                 
        self.assertTrue((AnswerQuestionOne()[3] == self.QuestionOneCArray).all(), "Question one part C array is not correct.")                 
        self.assertTrue((AnswerQuestionOne()[4] == self.QuestionOneDArray).all(), "Question one part D array is not correct.")                 

    def testQuestionTwo(self):
        """ Test to ensure that Question 2's output is the correct dimensions."""
        self.assertEqual(AnswerQuestionTwo().shape, (5,5), "Question two's output is not one dimension.")                 
        
    def testQuestionThree(self):
        """ Test to ensure that Question 3's output is the correct length and dimensions."""
        self.assertEqual(AnswerQuestionThree().shape, (10,), "Question three's output is not one dimension.")        
        self.assertEqual(AnswerQuestionThree().size, 10, "Question three's output is not 10 long.")

    def testQuestionFour(self):
        """ Test to ensure that Question 4's output (mandelbrot.png) exists."""
        self.assertTrue(os.path.exists("./mandelbrot.png"), "Question 4's output (mandelbrot.png) does not exist.")
  
        
if __name__ == "__main__":
  
    unittest.main()