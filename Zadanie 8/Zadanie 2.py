import unittest
import platform
import os
"""--------------------------------------""" 
class Employee:
    def __init__(self, name, last, age, salary):
        self.first_name = name
        self.last_name = last
        self.age = age
        self.salary = salary
        
    def introduce_self(self):
        return f'My name is {self.first_name} {self.last_name} and I am {self.age} years old'
    
    def raise_salary(self, ratio):
        self.salary =(self.salary * ratio)
        return self.salary

    def check_age(self):
        if self.age < 18:
            return 'Underage employee'
        else:
            return 'Adult employee'
        
    def get_email(self):
        return f'{self.first_name}{self.last_name}@company.com'
"""--------------------------------------""" 
class TEST (unittest.TestCase):
    def test_introduce_self(self):
        Emp1 = Employee("Mr.A","Aa",30,400)
        Emp2 = Employee("Mr.B","Bb",20,300)
        Emp3 = Employee("Mr.C","Cc",25,500)
        Emp4 = Employee("Ben","__",15,100)
    
        self.assertEqual(Emp1.introduce_self(),'My name is Mr.A Aa and I am 30 years old')
        self.assertEqual(Emp2.introduce_self(),'My name is Mr.B Bb and I am 20 years old')
        self.assertEqual(Emp3.introduce_self(),'My name is Mr.C Cc and I am 25 years old')
        self.assertEqual(Emp4.introduce_self(),'My name is Ben __ and I am 15 years old')

    def test_raise_salary(self):
        Emp1 = Employee("Mr.A","Aa",30,400)
        Emp2 = Employee("Mr.B","Bb",20,300)
        Emp3 = Employee("Mr.C","Cc",25,500)
        Emp4 = Employee("Ben","__",15,100)

        self.assertEqual(Emp1.raise_salary(1.20),480)
        self.assertEqual(Emp2.raise_salary(1.20),360)
        self.assertEqual(Emp3.raise_salary(1.20),600)
        self.assertEqual(Emp4.raise_salary(1.20),120)
    
    def test_check_age(self):
        Emp1 = Employee("Mr.A","Aa",30,400)
        Emp2 = Employee("Mr.B","Bb",20,300)
        Emp3 = Employee("Mr.C","Cc",25,500)
        Emp4 = Employee("Ben","__",15,100)
        
        self.assertEqual(Emp1.check_age(),'Adult employee')
        self.assertEqual(Emp2.check_age(),'Adult employee')
        self.assertEqual(Emp3.check_age(),'Adult employee')
        self.assertEqual(Emp4.check_age(),'Underage employee')

    def test_get_email(self):
        Emp1 = Employee("Mr.A","Aa",30,400)
        Emp2 = Employee("Mr.B","Bb",20,300)
        Emp3 = Employee("Mr.C","Cc",25,500)
        Emp4 = Employee("Ben","__",15,100)
    
        self.assertEqual(Emp1.get_email(),'Mr.AAa@company.com')
        self.assertEqual(Emp2.get_email(),'Mr.BBb@company.com')
        self.assertEqual(Emp3.get_email(),'Mr.CCc@company.com')
        self.assertEqual(Emp4.get_email(),'Ben__@company.com')
"""--------------------------------------"""      
def MyClear():
    if os.name=="posix":
        os.system("clear")
    if platform.system()=="Windows":
        os.system("cls")  
"""--------------------------------------""" 
MyClear()
unittest.main()