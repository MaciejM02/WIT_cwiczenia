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
is_authenticated = False
movies = {}
users = {}
def register_user():
    login=input("Wprowadź login: ")
    try:
        users[login]
        print("Taki użytkownik już istnieje")
    except KeyError:
        haslo=input("Wprowadź hasło: ")
        if len(haslo)<5:
            print("Hasło jest zakrótkie")
        else:
            users[login]=haslo
            print("Konto zostało utworzone")
def add_movie():
    if is_authenticated == False:
        print("Musisz być zalogowany by móc skorzystać z tej opcji")
    elif is_authenticated == True:
        title=input("Podaj nazwę filmu: ")
        try:
            movies[title]
            print("Taki film istnieje już w biblotece")
        except KeyError:
            try:
                amount=input("Podaj liczbę wolnych sztuk filmu: ")
                amount = int(amount)
                if amount >= 0:
                    movies[title]=amount
                    print("Film został dodany do bibloteki")
                else:
                    print("Błąd, podano ujemnąliczbę filmów")
            except ValueError:
                print("Błąd, źle wprowadzona informacja")
def modify_movie():
    if is_authenticated == False:
        print("Musisz być zalogowany by móc skorzystać z tej opcji")
    elif is_authenticated == True:
        title=input("Podaj nazwę filmu: ")
        try:
            movies[title]
            try:
                amount=input("Podaj liczbę wolnych sztuk filmu: ")
                amount = int(amount)
                if amount >= 0:
                    movies[title]=amount
                    print("Informacje o filmie zostały zmodyfikowane")
                else:
                    print("Błąd, podano ujemnąliczbę filmów")
            except ValueError:
                print("Błąd, źle wprowadzona informacja")
            except ValueError:
                print("Błąd, źle wprowadzona informacja")
        except KeyError:
            print("Taki film nie istnieje w biblotece")

def get_movies():
    print("Aktualnie w naszej biblotece znajdują się poniższe filmy:")
    for x in movies:
        print(x)

def check_movie_availability():
    print("Podaj nazwę filmu, kotórego chcesz sprawdzić zawartość")
    title = input(": ")
    try:
        movies[title]
        print(f"Aktkualnie mamy dostęmpne {movies[title]} sztuk filmu {title}")
    except KeyError:
        print("Taki film nie istnieje w biblotece")
def rent_movie():
    if is_authenticated == False:
        print("Musisz być zalogowany by móc skorzystać z tej opcji")
    elif is_authenticated == True:
        title=input("Podaj nazwę filmu: ")
        try:
            movies[title]
            if movies[title]<1:
                print("Przepraszsamy, ale nieposiadamy wolnych sztuk filmu")
            else:
                print(f"Aktkualnie mamy dostęmpne {movies[title]} sztuk filmu {title}")
                print("Czy chcesz wyporzyczyć film?")
                decyzja = input("Wpisz tak lub nie ")
                if decyzja.lower() == "tak":
                    movies[title]-=1
                    print(f"Wypożyczyno film o tytule {title}")
                elif decyzja.lower() == "nie":
                    print("Operacja została anulowana")
                else:
                    print("Pobano niewłaściwą decyzję, operacja została anulowana")
        except KeyError:
            print("Taki film nie istnieje w biblotece")


def login_user():
    login=input("Wprowadź login: ")
    try:
        users[login]
        haslo=input("Wprowadź hasło: ")
        if users[login]==haslo:
            print("Logowanie zakończone")
            return True
        else:
            print("Hasło nie poprawne")
    except KeyError:
        print("Taki użytkownik nie istnieje")
def log_out():
    return False


MyClear()
Z=0
while Z == 0:
    time.sleep(1)
    print()
    print("   Wybierz zadanie:")
    print("1. Utwórz użytkownika")
    print("2. Dodaj film")
    print("3. Zmodyfikuj ilość dostępnego filmu")
    print("4. Zobacz całą ofertę")
    print("5. Sprawdź dostępność filmu")
    print("6. Wypożycz film")
    if is_authenticated==False:
        print("7. Zaloguj się")
    elif is_authenticated==True:
        print("7. Wyloguj się")
    print("0. Zakończ działanie")
    try:
        Zadanie_n = int(input("---Podaj numer operacji: "))
        if Zadanie_n == 1:
            register_user()
        elif Zadanie_n == 2:
            add_movie()
        elif Zadanie_n == 3:
            modify_movie()
        elif Zadanie_n == 4:
            get_movies()
        elif Zadanie_n == 5:
            check_movie_availability()
        elif Zadanie_n == 6:
            rent_movie()
        elif Zadanie_n == 7:
            if is_authenticated==False:
                is_authenticated=login_user()
            elif is_authenticated==True:
                print("Wylogowano")
                is_authenticated=log_out()
        elif Zadanie_n == 0:
            Z = 1
        else:
            print("Podaj poprawny numer")
    except ValueError:
        print("Przyjmowane są jedynie liczby")