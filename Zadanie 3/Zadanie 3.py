import time
print("Zadanie 1")
time.sleep(1)

#lista = []
#a = int(input("Podaj liczbę znaków: "))
#while a != 0:
#    lista.append(int(input("Dodaj znak: ")))
#    a -= 1

lista = [1,2,3,4,5]

odwrocona_lista = lista[:]
n = len(odwrocona_lista)

while n >= 1:
    odwrocona_lista.insert(n, odwrocona_lista[0])
    del odwrocona_lista[0]
    n-=1
print(f"lista = {lista}")
print(f"odwrocona_lista = {odwrocona_lista}")

print()
print("Zadanie 2")
time.sleep(1)

Lista1 = lista[:]
Lista1.sort()
m0=Lista1[len(Lista1)-1]
m1=Lista1[len(Lista1)-2]
print(f"lista_max = {m1},{m0}")

print()
print("Zadanie 3")
time.sleep(1)

lista1 = []
lista2 = []
x=0
#while x <= 13:
#    if x>=3:
#        lista1.insert(x, x)
#    if x<=10:
#        lista2.insert(x, x)
#    x+=1
while x<=10:
    lista2.insert(x, x)
    x+=1
y=0
for y in range(3,14):
    lista1.insert(y, y)
print(f"lista1 = {lista1}")
print(f"lista2 = {lista2}")

print()
print("Zadanie 4")
time.sleep(1)

#dane_logowania = {"Użytkownik": "Admin1", "Hasło": "Start1234"}
#z = 0
#while z == 0:
#    Nazwa = str(input("Podaj nazwę użytkownika: "))
#    Kod_dostempu = str(input("Podaj hasło: "))
#    if Nazwa == dane_logowania["Użytkownik"] and Kod_dostempu == dane_logowania["Hasło"]:
#        z+=1
#        print("Logowanie poprawne")
#    else:
#        print("Błąd logowania, spróbuj ponownie")

dane_logowania = {"Admin": "1234"}
z = 0
while z == 0:
    Nazwa = str(input("Podaj nazwę użytkownika: "))
    Kod_dostempu = str(input("Podaj hasło: "))
    if dane_logowania.get(Nazwa) == Kod_dostempu:
        print("Logowanie poprawne")
        z+=1
    else:
        print("Błąd logowania, spróbuj ponownie")
print()
print("Zadanie 5")
time.sleep(1)

lista1 = [1,2,3,4,5]
lista2 = [1,2,3,4,5]
lista3 = [1,2,2,3,3,4,5]
lista1_set = set(lista1)
lista2_set = set(lista2)
lista3_set = set(lista3)
if lista1_set == lista2_set:
    print("lista1 i lista2 mają wspólne elementy")
else:
    print("lista1 i lista2 mają różne elementy")
if lista2_set == lista3_set:
    print("lista2 i lista3 mają wspólne elementy")
else:
    print("lista2 i lista3 mają różne elementy")
if lista3_set == lista1_set:
    print("lista3 i lista1 mają wspólne elementy")
else:
    print("lista3 i lista1 mają różne elementy")
if lista1_set == lista2_set and lista2_set == lista3_set and lista3_set == lista1_set:
    print("Wszystkie listy zawierają te same elementy")
print()
if len(lista1) == len(lista1_set):
    print("lista1 nie zawiera duplikatów")
else:
    print("lista1 zawiera duplikaty")
if len(lista2) == len(lista2_set):
    print("lista2 nie zawiera duplikatów")
else:
    print("lista2 zawiera duplikaty")
if len(lista3) == len(lista3_set):
    print("lista3 nie zawiera duplikatów")
else:
    print("lista3 zawiera duplikaty")
