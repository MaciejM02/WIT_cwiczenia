import os
import platform
import random
import sys   
import time
import math
def MyClear():
    if os.name=="posix":
        os.system("clear")
    if platform.system()=="Windows":
        os.system("cls")    
def calc_circle_area():
    try:
        r = int(input("Podaj promień: "))
    except ValueError:
        print("Błąd")
    area = math.pi*(r*r)
    print(f"Pole koła wynosi: {area}")

def check_parity():
    try:
        number = int(input("Podaj liczbę: "))
    except ValueError:
        print("Błąd")
    if number % 2 == 0:
        print("Liczba jest parzysta")
    else:
        print("Liczba jest nieparzysta")
def element_present():
    try:
        n = int(input("Podaj liczbę elementów listy: "))
        try:
            i = 0
            lista = []
            while i != n:
                lista.append(int((input("Podaj zawartość listy: "))))
                i+=1
        except ValueError:
            print("Błąd")
    except ValueError:
        print("Błąd")    
    element = int(input("Podaj liczbę do sprawdzenia: "))
    if lista.count(element) > 0:
        print("True")
    else:
        print("False")
def check_str_len():
    string = input("Podaj string: ")
    if len(string) < 9:
        raise ValueError
    else:
        print("O.K.")
def słowniczek():
    slownik = {}

    def print_menu():
        print('1. Dodaj wpis')
        print('2. Odzyskaj wpis')
        print('3. Zmodyfikuj wpis')
        print('4. Usu? wpis')
        print('0. Wyjd?')
        
    def create_item():
        klucz = input("Podaj klucz: ")
        wartość = input("Podaj wartość: ")
        slownik[klucz] = wartość
    def read_item():
        try:
            klucz = input("Podaj klucz: ")
            print(f"Wartość to {slownik[klucz]}")
        except KeyError:
            print("Brak wartości")
    def update_item():
        klucz = input("Podaj klucz: ")
        wartość = input("Podaj wartość: ")
        slownik[klucz] = wartość
    def delete_item():
        klucz = input("Podaj klucz: ")
        del slownik[klucz]
    while True:
        print_menu()

        option = input("Podaj opcj?: ")
        if option == '1':
            create_item()
        elif option == '2':
            read_item()
        elif option == '3':
            update_item()
        elif option == '4':
            delete_item()
        elif option == '0':
            break

class Animal:
    def __init__(self,name):
        self.name = name
    def get_name(self):
        pass
    def set_name(self):
        pass
class Mammal(Animal):
    def __init__(self,name,no_legs,has_fur):
        super().__init__(self,name)
        self.no_legs = no_legs
        self.has_fur = has_fur
    def get_no_legs(self):
        pass
    def set_no_legs(self):
        pass
    def get_has_fur(self):
        pass
    def set_has_fur(self):
        pass
class Canine(Mammal):
    def __init__(self,name,no_legs,has_fur):
        super().__init__(self,name,no_legs,has_fur)
    def howl(self):
        pass
    def bark(self):
        pass
class Dog(Canine):
    def __init__(self,name,no_legs,has_fur,kind,owner):
        super().__init__(self,name,no_legs,has_fur)
        self.kind = kind
        self.owner = owner
    def get_kind(self):
        pass
    def set_kind(self):
        pass
    def get_owner(self):
        pass
    def set_owner(self):
        pass

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
    print("5. Zadanie 5 ")
    print("0. Zakończ działanie")
    Zadanie_n = int(input("---Podaj numer operacji: "))
    if Zadanie_n == 1:
        calc_circle_area()
    elif Zadanie_n == 2:
        check_parity()
    elif Zadanie_n == 3:
        element_present()
    elif Zadanie_n == 4:
        check_str_len()
    elif Zadanie_n == 5:
        słowniczek()
    elif Zadanie_n == 0:
        Z = 1
    else:
        print("Podaj poprawny numer")



#Przepraszam że wszystko w jednym piku 

