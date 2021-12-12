import unittest
import platform
import os
"""--------------------------------------"""      
def MyClear():
    if os.name=="posix":
        os.system("clear")
    if platform.system()=="Windows":
        os.system("cls")  
"""--------------------------------------""" 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError('Can not divide by zero!')

    return x / y
"""--------------------------------------""" 
class TEST (unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(1, 5),6)
    def test_subtract(self):
        self.assertEqual(subtract(1, 5),-4)
    def test_multiply(self):
        self.assertEqual(multiply(2, 5),10)
    def test_divide(self):
        self.assertEqual(divide(1, 5),0.2)
    def test_divide(self):
        with self.assertRaises(ValueError):
            divide(1, 0)
"""--------------------------------------""" 
def is_numeric(arg):
    arg = isinstance(arg, (int, float))
    if arg == False:
        raise ValueError
def add_Plus(x, y):
    is_numeric(x)
    is_numeric(y)
    return x + y

def subtract_Plus(x, y):
    is_numeric(x)
    is_numeric(y)   
    return x - y

def multiply_Plus(x, y):
    is_numeric(x)
    is_numeric(y)           
    return x * y

def divide_Plus(x, y):
    is_numeric(x)
    is_numeric(y)
    if y == 0:
        raise ValueError('Can not divide by zero!')

    return x / y
"""--------------------------------------""" 
class TEST_Plus (unittest.TestCase):
    def test_add_Plus(self):
        self.assertEqual(add(1, 5),6)
        self.assertEqual(add(1.0, 5.0),6.0)
        with self.assertRaises(ValueError):
            divide_Plus(1, "_")    
            divide_Plus("_",1 ) 
            divide_Plus("_", "_") 
    def test_subtract_Plus(self):
        self.assertEqual(subtract(1, 5),-4)
        self.assertEqual(subtract(1.0, 5.0),-4.0)
        with self.assertRaises(ValueError):
            divide_Plus(1, "_")    
            divide_Plus("_",1 ) 
            divide_Plus("_", "_")
    def test_multiply_Plus(self):
        self.assertEqual(multiply(2, 5),10)
        self.assertEqual(multiply(2.0, 5.0),10.0)
        with self.assertRaises(ValueError):
            divide_Plus(1, "_")    
            divide_Plus("_",1 ) 
            divide_Plus("_", "_")
    def test_divide_Plus(self):
        self.assertEqual(divide_Plus(1, 5),0.2)
        self.assertEqual(divide_Plus(1.0, 5.0),0.2)
        with self.assertRaises(ValueError):
            #divide_Plus(1, 1) 
            divide_Plus(1, "_")
            divide_Plus("_", 0)
            divide_Plus("_", 1)
            divide_Plus("_", "_")
            divide_Plus(1, 0)
"""--------------------------------------""" 
MyClear()
unittest.main()
