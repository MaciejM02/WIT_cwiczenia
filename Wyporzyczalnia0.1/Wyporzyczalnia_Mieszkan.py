import unittest
import platform
import os
import pandas as pd
import csv
"""--------------------------------------"""
import Texts
import Tool_Box

"""--------------------------------------"""      
def MyClear():
    if os.name=="posix":
        os.system("clear")
    if platform.system()=="Windows":
        os.system("cls")  
"""--------------------------------------""" 

"""--------------------------------------"""
def Main():
    ON = 1
    Log = ('-', '-')
    while ON == 1:
        if Log != ('-', '-'):
            Texts.text0()
            Texts.text2()
            if 1==1:
            #try:
                Option1 = int(input("---Podaj numer operacji: "))
                if Option1 == 1:
                    #Tool_Box.copy_csv('Apartments.csv')
                    Tool_Box.Tool3(Log)
                elif Option1 == 2:
                    Tool_Box.Tool4(Log)
                elif Option1 == 3:
                    pass
                elif Option1 == 4:
                    pass
                elif Option1 == 5:
                    pass
                elif Option1 == 6:
                    Log = ('-', '-')
                elif Option1 == 7:
                    ON = 0
                else:
                    print("Podaj poprawny nume\n")
            #except ValueError:
                #print("Przyjmowane są jedynie liczby\n")
        else:
            Texts.text0()
            Texts.text1()
            try:
                Option1 = int(input("---Podaj numer operacji: "))
                if Option1 == 1:
                    #Tool_Box.copy_csv('Apartments.csv')
                    Log=Tool_Box.Tool3(Log)
                elif Option1 == 2:
                    Tool_Box.Tool1()
                elif Option1 == 3:
                    Log = Tool_Box.Tool2()
                elif Option1 == 4:
                    ON = 0
                else:
                    print("Podaj poprawny nume\n")
            except ValueError:
                print("Przyjmowane są jedynie liczby\n")
"""--------------------------------------"""
MyClear()
print("Witanka")
Main()


