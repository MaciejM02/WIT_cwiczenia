import os
import platform
import random
import sys   
import time
def MyClear():
    if os.name=="posix":
        os.system("clear")
    if platform.system()=="Windows":
        os.system("cls")      
def Zadanie_1 ():
    def digitize(number):
        number = str(number)
        i = 0
        lista = []
        while i != len(number):
            lista.append(int(number[i]))
            i += 1
        print(f"Wynik to: {lista}")
    MyClear()
    Z=0
    while Z == 0:
        time.sleep(1)
        print()
        print("Zadanie 1")
        print("   Wybierz operacje:")
        print("1. Digitize number")
        print("0. Zakończ działanie")
        try:
            Zadanie_n = int(input("---Podaj numer operacji: "))
            if Zadanie_n == 1:
                try:
                    number = input("Wprowadź liczbę do konwersji: ")
                    number = int(number)
                    digitize(number)
                except ValueError:
                    print("Przyjmowane są jedynie liczby")
            elif Zadanie_n == 0:
                Z = 1
                MyClear()
            else:
                print("Podaj poprawny numer")
        except ValueError:
            print("Przyjmowane są jedynie liczby")
def Zadanie_2 ():
    def roll_dice():
        print(f"Numer kości to: {random.randrange(1, 7)}")
    MyClear()
    Z=0
    while Z == 0:
        time.sleep(1)
        print()
        print("Zadanie 2")
        print("   Wybierz operacje:")
        print("1. Rzuć kością")
        print("0. Zakończ działanie")
        try:
            Zadanie_n = int(input("---Podaj numer operacji: "))
            if Zadanie_n == 1:
                roll_dice()
            elif Zadanie_n == 0:
                Z = 1
                MyClear()
            else:
                print("Podaj poprawny numer")
        except ValueError:
            print("Przyjmowane są jedynie liczby")
def Zadanie_3 ():
    def roll_dice(number):
        conter = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
        rzuty_kości = []
        i = 0
        while i != number:
            kość = random.randrange(1, 7)
            conter[kość] += 1
            i += 1
            rzuty_kości.append(kość)
        print(f"Rzuty kości: {rzuty_kości}")
        try:
            i=1   
            while i != 0:
               if conter[i] > 1: 
                   i=0
                   print("Wystęmpują duplikaty")
               else: i += 1
        except:
            print("Brak duplikatów")
    MyClear()
    Z=0
    while Z == 0:
        time.sleep(1)
        print()
        print("Zadanie 3")
        print("   Wybierz operacje:")
        print("1. Rzuć kością")
        print("0. Zakończ działanie")
        try:
            Zadanie_n = int(input("---Podaj numer operacji: "))
            if Zadanie_n == 1:
                try:
                    number = input("Wprowadź liczbę rzutów: ")
                    number = int(number)
                    roll_dice(number)
                except ValueError:
                    print("Przyjmowane są jedynie liczby")
            elif Zadanie_n == 0:
                Z = 1
                MyClear()
            else:
                print("Podaj poprawny numer")
        except ValueError:
            print("Przyjmowane są jedynie liczby")
def Zadanie_4 ():
    def roll_dice(number):
        rzuty_kości = []
        dublety = 0
        i = 0
        while i != number:
            kość1 = random.randrange(1, 7)
            kość2 = random.randrange(1, 7)
            i += 1
            rzuty_kości.append(kość1)
            rzuty_kości.append(kość2)
            if kość1 == kość2:
                dublety += 1
        print(f"Rzuty kości: {rzuty_kości}")
        try:
            procent = (dublety/number)*100
            print(f"Wystąpiło {dublety} dubletów, stanowią one {round(procent, 2)}% procent wszystkich rzutów")
        except:
            print("Brak duplikatów")
    MyClear()
    Z=0
    while Z == 0:
        time.sleep(1)
        print()
        print("Zadanie 4")
        print("   Wybierz operacje:")
        print("1. Rzuć kościmi")
        print("0. Zakończ działanie")
        try:
            Zadanie_n = int(input("---Podaj numer operacji: "))
            if Zadanie_n == 1:
                try:
                    number = input("Wprowadź liczbę rzutów: ")
                    number = int(number)
                    roll_dice(number)
                except ValueError:
                    print("Przyjmowane są jedynie liczby")
            elif Zadanie_n == 0:
                Z = 1
                MyClear()
            else:
                print("Podaj poprawny numer")
        except ValueError:
            print("Przyjmowane są jedynie liczby")
MyClear()
Z=0
while Z == 0:
    time.sleep(1)
    print()
    print("   Wybierz zadanie:")
    print("1. Zadanie 1")
    print("2. Zadanie 2")
    print("3. Zadanie 3")
    print("4. Zadanie 4")
    print("0. Zakończ działanie")
    try:
        Zadanie_n = int(input("---Podaj numer operacji: "))
        if Zadanie_n == 1:
            Zadanie_1 ()
        elif Zadanie_n == 2:
            Zadanie_2 ()
        elif Zadanie_n == 3:
            Zadanie_3 ()
        elif Zadanie_n == 4:
            Zadanie_4 ()
        elif Zadanie_n == 0:
            Z = 1
        else:
            print("Podaj poprawny numer")
    except ValueError:
        print("Przyjmowane są jedynie liczby")
