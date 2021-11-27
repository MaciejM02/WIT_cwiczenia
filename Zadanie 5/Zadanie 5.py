Z=0
Argumenty = []
Urzytkownicy = {}
while Z==0:
    def Zadanie_1 ():
        Urzytkownicy1 = {}
        def Opcja_1 ():
            Login=input("Podaj login: ")
            Hasło=input("Podaj hasło: ")
            try:
                if len(Login) <= 5: raise ValueError ("Login powinien zawierać min. 6 zanaków")      
                try:
                    if len(Hasło) <= 6: raise ValueError ("Hasło powinno zawierać min. 7 zanaków")
                    print("Rejestracja zakończona sukcesem")
                    Urzytkownicy1[Login] = Hasło
                except  ValueError:
                    print("Hasło jest zakrótkie")
            except ValueError:
                print("Login jest zakrótki")
        def Opcja_2 ():
            print(Urzytkownicy1)
        X=0
        while X==0:
            print("Zadanie 1. Rejestracja")
            print()
            print("   Wybierz opcje:")
            print("1. Zarejestruj")
            print("2. Sprawdź listę użytkowników")
            print("0. Powrót")
            Opcja = int(input("---Podaj numer operacji: "))
            if Opcja == 1:
                Opcja_1 ()
            elif Opcja == 2:
                Opcja_2 ()
            elif Opcja == 0:
                X=1
            else:
                print("Podaj poprawny numer")
        

    def Zadanie_2 ():
        def Opcja_1 ():
            XY=0
            while XY == 0:
                XYZ=0
                while XYZ == 0:
                    Ar1=input("Podaj argument: ")
                    if type(Ar1) != int or float:
                        try:
                            Ar1 = int(Ar1)
                            XYZ=1
                        except ValueError:
                            try:
                                Ar1 = float(Ar1)
                                XYZ=1
                            except ValueError:
                                print("Argument musi być int lub foat")
                Argumenty.append(Ar1)
                F=input("Przerwać wprowadzanie? (Y): ")
                if F.lower() in ["y"]:
                    XY=1
            if type(Ar1) == int or float:
                try:
                    if Argumenty == []: raise ValueError   
                    Argumenty.sort()
                    i=0
                    Suma=0
                    while i != len(Argumenty):
                        Suma+=Argumenty[i]
                        i+=1
                    Wynik = (f"Wynik to ({Suma},{Argumenty[-1]},{Argumenty[0]})")
                    print(Wynik)
                    print()
                except ValueError:
                    print("Lista jest pusta")
        def Opcja_2 ():
            i=0
            Suma=0
            while i != len(Argumenty):
                Suma+=Argumenty[i]
                i+=1
            print(f"Suma to {Suma}")
            print()
        def Opcja_3 ():
            print(f"Max. to {Argumenty[-1]}")
            print()
        def Opcja_4 ():
            print(f"Mini. to {Argumenty[0]}")
            print()
        X=0
        Y=0

        while Y==0:
            try:
                if type(Argumenty[0]) == int or float:X=1
            except:
                pass
            print("Zadanie 2. Działania na liście")
            print()
            print("   Wybierz opcje:")
            print("1. Wprowadź Argumenty")
            if X==1:
                print("2. Podaja ponownie sumę")
                print("3. Podaja ponownie maksimum")
                print("4. Podaja ponownie minimum")
            print("0. Powrót")
            Opcja = int(input("---Podaj numer operacji: "))
            if Opcja == 1:
                Opcja_1 ()
            elif Opcja == 2 and X==1:
                Opcja_2 ()
            elif Opcja == 3 and X==1:
                Opcja_3 ()
            elif Opcja == 4 and X==1:
                Opcja_4 ()            
            elif Opcja == 0:
                Y=1
            else:
                print("Podaj poprawny numer")
        

    def Zadanie_3 ():
        def Opcja_1 ():
            print()
            print("Login musi zawierać 6 znaków")
            Login=input("Podaj login: ")
            try:
                if Urzytkownicy[f'{Login}'] != None:
                    print()
                    print("Taki urzytkownik już istnieje")
            except KeyError:
                try:  
                    if len(Login) <= 5: raise ValueError ("Login powinien zawierać min. 6 zanaków")      
                    print()
                    print("Hasło musi zawierać 7 znaków")
                    Hasło=input("Podaj hasło: ")
                    try:
                        if len(Hasło) <= 6: raise ValueError ("Hasło powinno zawierać min. 7 zanaków")
                        print()
                        print("Rejestracja zakończona sukcesem")
                        Urzytkownicy[Login] = Hasło
                    except  ValueError:
                            print()
                            print("Hasło jest zakrótkie")
                except ValueError:
                    print()
                    print("Login jest zakrótki")


        def Opcja_2 ():
            print("Aktywni urzytkownicy:")
            print()
            for key, value in Urzytkownicy.items() :
                print (f"Nazwa: {key}")
                print (f" Hasło: {value}")
                print()
        
        def Opcja_3 ():
            print()
            print("Podaj nazwę urzytkownika")
            Login=input("Podaj login: ")
            try:
                if Urzytkownicy[f'{Login}'] != None:
                    print()
                    Hasło=input("Podaj hasło: ")
                    if Urzytkownicy[Login] == Hasło:
                        print()
                        print("Hasło musi zawierać 7 znaków")
                        NHasło=input("Podaj nowe hasło: ")
                        try:
                            if len(NHasło) <= 6: raise ValueError ("Hasło powinno zawierać min. 7 zanaków")
                            print()
                            N2Hasło=input("Powtórz hasło: ")
                            if NHasło == N2Hasło:
                                print()
                                print("Zmiana hasła zakończona sukcesem")
                                Urzytkownicy[Login] = NHasło
                            else:
                                print("Hasła się niepokrywają")
                        except  ValueError:
                            print()
                            print("Hasło jest zakrótkie")
                    else:
                        print()
                        print("Błędne hasło")
            except KeyError:
                    print()
                    print("Taki urzytkownik nie istnieje")
        def Opcja_4 ():
            print()
            print("Podaj nazwę urzytkownika")
            Login=input("Podaj login: ")
            try:
                if Urzytkownicy[f'{Login}'] != None:
                    print()
                    Hasło=input("Podaj hasło: ")
                    if Urzytkownicy[Login] == Hasło:
                        print()
                        print("Uwaga zamierzasz usunąć konto, jeśli chcesz kontynułować wpisz: USUŃ_[Nazwa konta]")
                        if (f"USUŃ_{Login}") == input("Podaj potwierdzienie: "):
                            print("Konto usunięte")
                            del Urzytkownicy[Login]
                        else:
                            print("Operacja przerwana")
                    else:
                        print()
                        print("Błędne hasło")
            except KeyError:
                    print()
                    print("Taki urzytkownik nie istnieje")
        X=0
        while X==0:
            print()
            print("Zadanie 3. Skrypt")
            print()
            print("   Wybierz opcje:")
            print("1. Dodaj użytkownika")
            print("2. Wyświetl użytkowników")
            print("3. Zmień hasło użytkownika")
            print("4. Usuń użytkownika")
            print("0. Powrót")
            Opcja = int(input("---Podaj numer operacji: "))
            if Opcja == 1:
                Opcja_1 ()
            elif Opcja == 2:
                Opcja_2 ()
            elif Opcja == 3:
                Opcja_3 ()
            elif Opcja == 4:
                Opcja_4 ()
            elif Opcja == 0:
                X=1
            else:
                print("Podaj poprawny numer")
        



    print()
    print("   Wybierz zadanie:")
    print("1. Zadanie 1")
    print("2. Zadanie 2")
    print("3. Zadanie 3")
    print("0. Zakończ działanie")
    Zadanie_n = int(input("---Podaj numer operacji: "))

    if Zadanie_n == 1:
        Zadanie_1 ()
    elif Zadanie_n == 2:
        Zadanie_2 ()
    elif Zadanie_n == 3:
        Zadanie_3 ()
    elif Zadanie_n == 0:
        Z = 1
    else:
        print("Podaj poprawny numer")