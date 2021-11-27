import time

Z=0
while Z == 0:

    def Zadanie_1 ():

        print()
        print("Zadanie 1")
        time.sleep(0.5)

        def convert_string_to_number (data1):
            print(int(data1))
            print(type(int(data1)))

        A=0
        while A == 0:
            time.sleep(1)
            print()
            print("   Możliwe operacje:")
            print("1. Przekonwertuj 111")
            print("2. Przekonwertuj 456")
            print("3. Wprowadź liczbę do konwersji")
            print("4. Powrót")
            Option1 = input("---Podaj numer operacji: ")
            if Option1 == "1":
                convert_string_to_number ("111")
            elif Option1 == "2":
                convert_string_to_number ("456")
            elif Option1 == "3":
                data2 = input("---Podaj liczbę do konwersji: ")
                convert_string_to_number (data2)
            elif Option1 == "4":
                A+=1
            else:
                print("Podaj poprawny numer")

    def Zadanie_2 ():

        print()
        print("Zadanie 2")
        time.sleep(0.5)

        def find_min (lista1):
            if len(lista1) > 0:
                lista1.sort()
                print(lista1[0])
            else:
                print("Brak")

        lista2 = [34, 21, 90, 14]
        A=0
        while A == 0:
            time.sleep(1)
            print()
            print("   Możliwe operacje:")
            print("1. Pokaż listę")
            print("2. Zmień listę")
            print("3. Podaj najmniejszą wartość listy")
            print("4. Powrót")
            Option1 = input("---Podaj numer operacji: ")
            if Option1 == "1":
                print(f"lista = {lista2}")
            elif Option1 == "2":
                B=0
                while B == 0:
                    time.sleep(1)
                    print()
                    print("   Możliwe operacje:")
                    print("1. Dodaj element")
                    print("2. Wyczyść listę")
                    print("3. Przerwij modyfikacje")
                    Option2 = input("---Podaj numer operacji: ")
                    if Option2 == "1":
                        print(" !!! Uwaga przyjmowane są jedynie liczby !!! ")
                        element =  (input("---Wprowadź element: "))
                        element = int(element)
                        lista2.append(element)
                        print(f"Dodano do listy {element}")
                    elif Option2 == "2":
                        lista2.clear()
                        print("Lista wyczyszczona")
                    elif Option2 == "3":
                        B+=1
                    else:
                        print("Podaj poprawny numer")
            elif Option1 == "3":
                print(f"Najmniejszy numer to: ",end="")
                find_min (lista2)
            elif Option1 == "4":
                A+=1
            else:
                print("Podaj poprawny numer")

    def Zadanie_3 ():

        print()
        print("Zadanie 3")
        time.sleep(0.5)

        def print_list (lista3):
            A=0
            while A != len(lista3):
                print(lista3[A])
                A+=1

        lista4 = [1, 2, 3, 4, 5]
        A=0
        while A == 0:
            time.sleep(1)
            print()
            print("   Możliwe operacje:")
            print("1. Pokaż listę")
            print("2. Zmień listę")
            print("3. Wymień elementy listy")
            print("4. Powrót")
            Option1 = input("---Podaj numer operacji: ")
            if Option1 == "1":
                print(f"lista = {lista4}")
            elif Option1 == "2":
                B=0
                while B == 0:
                    time.sleep(1)
                    print()
                    print("   Możliwe operacje:")
                    print("1. Dodaj element")
                    print("2. Wyczyść listę")
                    print("3. Przerwij modyfikacje")
                    Option2 = input("---Podaj numer operacji: ")
                    if Option2 == "1":
                        print(" !!! Uwaga przyjmowane są jedynie liczby !!! ")
                        element =  (input("---Wprowadź element: "))
                        element = int(element)
                        lista4.append(element)
                        print(f"Dodano do listy {element}")
                    elif Option2 == "2":
                        lista4.clear()
                        print("Lista wyczyszczona")
                    elif Option2 == "3":
                        B+=1
                    else:
                        print("Podaj poprawny numer")
            elif Option1 == "3":
                print("Elementy listy to kolejno: ")
                print_list (lista4)
            elif Option1 == "4":
                A+=1
            else:
                print("Podaj poprawny numer")

    def Zadanie_4 ():

        print()
        print("Zadanie 4")
        time.sleep(0.5)

        def print_dict (słow1):
            pass

        słow2 = {"a": 1,"b": 2,"c": 3}
        A=0
        while A == 0:
            time.sleep(1)
            print()
            print("   Możliwe operacje:")
            print("1. Pokaż słownik")
            print("2. Zmień słownik")
            print("3. Wymień elementy słownika")
            print("4. Powrót")
            Option1 = input("---Podaj numer operacji: ")
            if Option1 == "1":
                print(f"słownik = {słow2}")
            elif Option1 == "2":
                B=0
                while B == 0:
                    time.sleep(1)
                    print()
                    print("   Możliwe operacje:")
                    print("1. Dodaj lub zmień element")
                    print("2. Usuń element")
                    print("3. Wyczyść słownik")
                    print("4. Przerwij modyfikacje")
                    Option2 = input("---Podaj numer operacji: ")
                    if Option2 == "1":
                        element1 = (input("---Wprowadź klucz: "))
                        element2 = (input("---Wprowadź element: "))
                        element3 = input("Czy element ma być zapisany w formie liczby? (Y/N) ")
                        if element3.lower() in ["y"]:
                            element2 = int(element2)
                        słow2[element1] = element2
                        print(f"Dodano do słownika {element1}: {element2}")
                    elif Option2 == "2":
                        element1 = (input("---Wprowadź klucz do usunięcia: "))
                        print(f"Usunięto {słow2[element1]}")
                        del słow2[element1]
                    elif Option2 == "3":
                        słow2.clear()
                        print("Słownik wyczyszczony")
                    elif Option2 == "4":
                        B+=1
                    else:
                        print("Podaj poprawny numer")
            elif Option1 == "3":
                print("Elementy słownika to kolejno:")
                print_dict (słow2)
            elif Option1 == "4":
                A+=1
            else:
                print("Podaj poprawny numer")

    def Zadanie_5 ():

        print()
        print("Zadanie 5")
        time.sleep(0.5)

        def get_length (data1):
            print(f"Długość słowa '{data1}' to ", end=(""))
            print(len(data1))

        A=0
        while A == 0:
            time.sleep(1)
            print()
            print("   Możliwe operacje:")
            print("1. Podaj długość 'litery'")
            print("2. Podaj długość 'cokolwiek'")
            print("3. Wprowadź słowo do zliczenia")
            print("4. Powrót")
            Option1 = input("---Podaj numer operacji: ")
            if Option1 == "1":
                get_length ("litery")
            elif Option1 == "2":
                get_length ("cokolwiek")
            elif Option1 == "3":
                data2 = input("---Podaj słowo do przeliczenia: ")
                get_length (data2)
            elif Option1 == "4":
                A+=1
            else:
                print("Podaj poprawny numer")

    def Zadanie_6 ():

        print()
        print("Zadanie 6")
        time.sleep(0.5)

        def remove_outer_characters (string1): 
            if len(string1) >=3:
                print(string1[1:len(string1)-1])

        string2 = "string"
        A=0
        while A == 0:
            time.sleep(1)
            print()
            print("   Możliwe operacje:")
            print("1. Pokaż stringa")
            print("2. Zmień stringa")
            print("3. Usuń litery")
            print("4. Powrót")
            Option1 = input("---Podaj numer operacji: ")
            if Option1 == "1":
                print(f"string = {string2}")
            elif Option1 == "2":
                string2 = input("Wprowadź stringa: ") 
                print(f"String zmieniona na {string2}")
            elif Option1 == "3":
                if len(string2) >= 3:
                    print("Wynik operacji to ", end=(""))
                    remove_outer_characters (string2)
                else:
                    print("Błąd, wyraz jest za krótki")
            elif Option1 == "4":
                A+=1
            else:
                print("Podaj poprawny numer")

    def Zadanie_7  ():

        print()
        print("Zadanie 7")
        time.sleep(0.5)

        def count_chars (słow3):
            słownik = {}
            A = 0
            while A != len(słow3):
                słownik[słow3[A]] = 1
                A+=1
            print(f"słownik = {słownik}")
            A = 0

        słow4 = "Przyklad"
        A=0
        while A == 0:
            time.sleep(1)
            print()
            print("   Możliwe operacje:")
            print("1. Pokaż stringa")
            print("2. Zmień stringa")
            print("3. Zmień stringa na słownik")
            print("4. Powrót")
            Option1 = input("---Podaj numer operacji: ")
            if Option1 == "1":
                print(f"string = {słow4}")
            elif Option1 == "2":
                słow4 = input("Wprowadź stringa: ") 
                print(f"String zmieniona na {słow4}")
            elif Option1 == "3":
                if len(słow4) >= 1:
                    count_chars (słow4)
                else:
                    print("Błąd, wyraz jest za krótki")
            elif Option1 == "4":
                A+=1
            else:
                print("Podaj poprawny numer")

    time.sleep(1)
    print()
    print("   Wybierz zadanie:")
    print("1. Zadanie 1")
    print("2. Zadanie 2")
    print("3. Zadanie 3")
    print("4. Zadanie 4")
    print("5. Zadanie 5")
    print("6. Zadanie 6")
    print("7. Zadanie 7")
    print("8. Zakończ działanie")
    Zadanie_n = int(input("---Podaj numer operacji: "))

    if Zadanie_n == 1:
        Zadanie_1 ()
    elif Zadanie_n == 2:
        Zadanie_2 ()
    elif Zadanie_n == 3:
        Zadanie_3 ()
    elif Zadanie_n == 4:
        Zadanie_4 ()
    elif Zadanie_n == 5:
        Zadanie_5 ()
    elif Zadanie_n == 6:
        Zadanie_6 ()
    elif Zadanie_n == 7:
        Zadanie_7 ()
    elif Zadanie_n == 8:
        Z = 1
    else:
        print("Podaj poprawny numer")