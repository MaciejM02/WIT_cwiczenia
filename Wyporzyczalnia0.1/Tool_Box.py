import pandas as pd
import csv
from csv import writer
from collections import defaultdict
"""--------------------------------------"""
import Texts
"""--------------------------------------""" 

"""--------------------------------------"""   

"""--------------------------------------""" 
def Tool1():
    new_user = str(input("---Podaj nazwę nowego konta: "))
    a_csv_file = open("Data.csv", "r")
    dict_reader = csv.DictReader(a_csv_file)
    Users = list(dict_reader)
    #print(Users[1]["Login"])
    with open("Data.csv") as f:
        rows = sum(1 for line in f)
    i = 0
    while i != rows :
        try:
            if new_user == Users[i]["Login"]:
                Tool1_1()
                break
            else:
                i += 1
        except IndexError:
            Tool1_2(new_user)
            break
    if rows == i:
        Tool1_2(new_user)

def Tool1_1():
    print("Takie konto już istnieje, spróbuj ponownie\n")

def Tool1_2(new_user):
    new_user = new_user
    print("  !!Uwaga hasło musi zawierać co najmniej 4 znaki!!")
    new_passw = str(input("---Podaj hasło: "))
    if len(new_passw) >= 4:
        print("Hasło zaakceptowane\n")
        Tool1_2_1(new_user, new_passw)
    else:
        print("Hasło nie poprawne, spróbuj ponownie\n")

def Tool1_2_1(new_user, new_passw):
    new = [new_user, new_passw, 0, None, None]
    with open(r'Data.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(new)

"""--------------------------------------"""

def Tool2():
    user = str(input("---Podaj nazwę konta: "))
    a_csv_file = open("Data.csv", "r")
    dict_reader = csv.DictReader(a_csv_file)
    Users = list(dict_reader)
    #print(Users[1]["Login"])
    with open("Data.csv") as f:
        rows = sum(1 for line in f)
    i = 0
    while i != rows :
        try:
            if user == Users[i]["Login"]:
                #Tool2_1(i,user)
                passw = str(input("---Podaj hasło: "))
                a_csv_file = open("Data.csv", "r")
                dict_reader = csv.DictReader(a_csv_file)
                Users = list(dict_reader)
                if passw == Users[i]["Password"]:
                    return(user,passw)
                else:
                    print("Błędne hasło\n")
                break
            else:
                i += 1
        except IndexError:
            print("Taki użytkownik nie istnieje\n")
            break
    if rows == i:
        print("Taki użytkownik nie istnieje\n")

"""--------------------------------------"""
def copy_csv(filename):
    df = pd.read_csv(filename)
    df.to_csv('copy_of_' + filename)

def Tool3(Log):
    ON = 1
    x = 0
    while ON == 1:
        #try:
            for l in csv.reader(open('Apartments.csv',encoding="utf8").readlines()[0:1]):
                print(l)        
            page_down = x+2
            page_up = x+7
            for l in csv.reader(open('Apartments.csv',encoding="utf8").readlines()[page_down: page_up]):
                print(l)
            Texts.text_()
            Texts.text0()
            Texts.text3()
            Option1 = int(input("---Podaj numer operacji: "))
            if Option1 == 1:
                x+=5
            elif Option1 == 2:
                x-=5
            elif Option1 == 3:
                ON = 0
                Tool3_1(Log)
            elif Option1 == 4:
                ON = 0    
        #except ValueError:
        #    print("Operacja nie udana, nie możliwe jest dalsze wyświetlanie listy")
        #    if Option1 == 1:
        #        x-5
        #    elif Option1 == 2:
        #        x+5
def Tool3_1(Log):
    if Log == ('-', '-'):
        print("Musisz być zalogowany by wynająć mieszkanie")
        Texts.text_()
        Texts.text11()
        Option1 = int(input("---Podaj numer operacji: "))
        if Option1 == 1:
            Tool2()
        elif Option1 == 2:
            Tool3(Log)
    else:
        Tool3_2(Log)

def Tool3_2(Log):
    print("Jaką formę płatność wybierasz:")
    Texts.text_()
    Texts.text12()
    Option1 = int(input("---Podaj numer operacji: "))
    if Option1 == 1:
        Pay = 1
        Tool3_3(Log, Pay)
    elif Option1 == 2:
        Pay = 2
        Tool3_3(Log, Pay)

def Tool3_3(Log,Pay):
    print("! Prosimy o podawanie wartości z spacją !")
    print("Podaj Ulice i Numer mieszkania")
    SN = input("---")
    print("Podaj miasto i cene za noc")
    CP = input("---")
    Streat = SN.split(' ')[0]
    Number = SN.split(' ')[1]
    City = CP.split(' ')[0]
    Price = CP.split(' ')[1]
    #potwierdzenie
    i = 0
    a_csv_file = open("Apartments.csv", "r",encoding="utf8")
    dict_reader = csv.DictReader(a_csv_file)
    Apartments = list(dict_reader)
    with open("Apartments.csv",encoding="utf8") as f:
        rows = sum(1 for line in f)
    while i != rows:
        if Streat == Apartments[i]["Ulica"]:
            if Number == Apartments[i]["Numer"]:
                if City == Apartments[i]["Miasto"]:
                    if Price == Apartments[i]["Cena"]:
                        Line = i
                        break
        else:
            i += 1
    if rows == i:
        print("Taki użytkownik nie istnieje\n")
    Tool3_4(Log,Pay,Streat,Number,City,Price,Line)

def Tool3_4(Log,Pay,Streat,Number,City,Price,Line):
    if Pay == 1:
        print("Podaj numer karty")
        Card = input("---")
        if len(Card) != 12:
            print("Błąd wpisywania")
            print("1. Sprubuj ponownie")
            print("2. Wróć")
            Option1 = input("---")
            if Option1 == 1:
                Tool3_4(Log,Pay,Streat,Number,City,Price)
            elif Option1 == 2:
                Tool3_1(Log)
        else:
            print("Podaj Imie i Nazwisko")
            Name = str(input("---"))
            Tool3_5(Log,Pay,Streat,Number,City,Price,Line)
    elif Pay == 2:
        pass

def Tool3_5(Log,Pay,Streat,Number,City,Price,Line):
    if Pay == 1:
        Apartments_list = []
        with open('Apartments.csv', 'r',encoding="utf8") as f:
            apartments = csv.reader(f)
            Apartments_list.extend(apartments)
            a_csv_file = open("Apartments.csv", "r",encoding="utf8")
        dict_reader = csv.DictReader(a_csv_file)
        Apartments = list(dict_reader)
        line_to_override = {(Line+2):[Apartments[Line]["Ulica"],Apartments[Line]["Numer"],Apartments[Line]["Miasto"],Apartments[Line]["Powiat"],Apartments[Line]["Województwo"],Apartments[Line]["Wielkość"],Apartments[Line]["Cena"],False,Apartments[Line]["Właściciel"]] }
        with open('Apartments.csv', 'w',newline="",encoding="utf8") as f:
            writer = csv.writer(f)
            for line, row in enumerate(Apartments_list):
                data = line_to_override.get(line, row)
                writer.writerow(data)
        i = 0
        a_csv_file = open("Data.csv", "r",encoding="utf8")
        dict_reader = csv.DictReader(a_csv_file)
        Apartments = list(dict_reader)
        with open("Data.csv",encoding="utf8") as f:
            rows = sum(1 for line in f)
        ON = 1
        while ON == 1:
            if Log[0] == Apartments[i]["Login"]:
                if Log[1] == Apartments[i]["Password"]:                    
                    Data_list = []
                    with open('Data.csv', 'r',encoding="utf8") as f:
                        data1 = csv.reader(f)
                        Data_list.extend(data1)
                        a_csv_file = open("Data.csv", "r",encoding="utf8")
                    dict_reader = csv.DictReader(a_csv_file)
                    Data = list(dict_reader)
                    line_to_override = {(2*i+2):[Data[i]["Login"],Data[i]["Password"],Data[i]["Status"],Data[i]["Flors"],Streat+"_"+Number+"_"+City+"_"+Price] }
                    with open('Data.csv', 'w',newline="",encoding="utf8") as f:
                        writer = csv.writer(f)
                        for line, row in enumerate(Data_list):
                            data = line_to_override.get(line, row)
                            writer.writerow(data)
                            ON = 0
            else:
                i += 1
        print("Operacja udana\n")
    elif Pay == 2:
        Apartments_list = []
        with open('Apartments.csv', 'r',encoding="utf8") as f:
            apartments = csv.reader(f)
            Apartments_list.extend(apartments)
            a_csv_file = open("Apartments.csv", "r",encoding="utf8")
        dict_reader = csv.DictReader(a_csv_file)
        Apartments = list(dict_reader)
        line_to_override = {(Line+2):[Apartments[Line]["Ulica"],Apartments[Line]["Numer"],Apartments[Line]["Miasto"],Apartments[Line]["Powiat"],Apartments[Line]["Województwo"],Apartments[Line]["Wielkość"],Apartments[Line]["Cena"],False,Apartments[Line]["Właściciel"]] }
        with open('Apartments.csv', 'w',newline="",encoding="utf8") as f:
            writer = csv.writer(f)
            for line, row in enumerate(Apartments_list):
                data = line_to_override.get(line, row)
                writer.writerow(data)


"""--------------------------------------"""
def Tool4(Log):
    a_csv_file = open("Data.csv", "r")
    dict_reader = csv.DictReader(a_csv_file)
    Users = list(dict_reader)
    with open("Data.csv") as f:
        rows = sum(1 for line in f)
    user = Log[0]    
    i = 0
    while i != rows :
        if user == Users[i]["Login"]:
            passw = Log[1]
            a_csv_file = open("Data.csv", "r")
            dict_reader = csv.DictReader(a_csv_file)
            Users = list(dict_reader)
            if passw == Users[i]["Password"]:
                print()
                break
        else:
            i += 1
