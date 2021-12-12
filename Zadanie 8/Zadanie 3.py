import unittest
import platform
import os
"""--------------------------------------""" 
def is_numeric(arg):
    return isinstance(arg, (int, float))
"""--------------------------------------""" 
class TEST1 (unittest.TestCase):
    def test_is_numeric(self):
        self.assertFalse(is_numeric("_______"))
        self.assertTrue(is_numeric(1234567890))
        self.assertTrue(is_numeric(1234567890.0))
"""--------------------------------------""" 
def is_negative(num):
    return num < 0
"""--------------------------------------""" 
class TEST2 (unittest.TestCase):
    def test_is_negative(self):
        self.assertTrue(is_negative(-1))
        self.assertFalse(is_negative(0))
        self.assertFalse(is_negative(1))
        with self.assertRaises(AssertionError):
            self.assertTrue(is_numeric("_______"))
"""--------------------------------------""" 
def calculate_savings(starting_amount, monthly_payment, monthly_deductions):
    if not is_numeric(starting_amount) or not is_numeric(monthly_payment) or not is_numeric(monthly_deductions):
        raise ValueError("All arguments must be numeric.")
    
    if is_negative(starting_amount) or is_negative(monthly_payment) or is_negative(monthly_deductions):
        raise ValueError("All arguments must be positive numbers.")
    
    return starting_amount + 12 * (monthly_payment - monthly_deductions)
"""--------------------------------------""" 
class TEST3 (unittest.TestCase):
    def test_calculate_savings(self):
        self.assertTrue(calculate_savings(1234567890,1234567890,1234567890))
        with self.assertRaises(ValueError):
            calculate_savings(1234567890,1234567890,"_______")
            calculate_savings(1234567890,"_______",1234567890)
            calculate_savings("_______",1234567890,1234567890)
            calculate_savings(1234567890,1234567890,-99999999)
            calculate_savings(1234567890,-99999999,1234567890)
            calculate_savings(-99999999,1234567890,1234567890)
        self.assertEquals(calculate_savings(1234567890,1234567890,1234567890),1234567890)
"""--------------------------------------"""      
def MyClear():
    if os.name=="posix":
        os.system("clear")
    if platform.system()=="Windows":
        os.system("cls")  
"""--------------------------------------""" 
MyClear()
unittest.main()
