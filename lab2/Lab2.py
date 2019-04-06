


#Zadanie 2

'''
import random

def lotto():
    lista = []
    ile = 1
    while ile <= 6:
        wartosc = random.randint(1, 50)
        if wartosc not in lista:
            ile = ile+1
            lista.append(wartosc)
    return lista

print(lotto())
'''

#Zadanie 3

'''
a = int(input("Podaj liczbe a "))
b = int(input("Podaj liczbe b "))
znak = input("Podaj znak ")

def mnozenie(a,b):
    wynik = a*b
    return wynik

def dodawanie(a,b):
    wynik = a+b
    return wynik

def odejmowanie(a,b):
    wynik = a-b
    return wynik

def dzielenie(a,b):
    if b==0:
         return "Błąd - nie można dzielić przez 0"
    else:
        wynik = a/b
        return wynik

if znak == "*":
    print(mnozenie(a,b))
elif znak == "+":
     print(dodawanie(a,b))
elif znak == "-":
     print(odejmowanie(a,b))
elif znak == "/":
     print(dzielenie(a,b))
'''

#Zadanie 4
'''
import math

zapytanie = int(input("Wprowadź:"+"\n"+"1 - aby obliczyć pole i obwód koła"+"\n"+"0 - aby użyć domyślnego kalkulatora: "))

if zapytanie == 0:
    a = int(input("Podaj liczbe a "))
    b = int(input("Podaj liczbe b "))
    znak = input("Podaj znak ")
elif zapytanie == 1:
    r = int(input("Podaj promień "))
else:
    print("Podano błędną wartość")

def mnozenie(a,b):
    wynik = a*b
    return wynik

def dodawanie(a,b):
    wynik = a+b
    return wynik

def odejmowanie(a,b):
    wynik = a-b
    return wynik

def dzielenie(a,b):
    if b==0:
         return "Błąd - nie można dzielić przez 0"
    else:
        wynik = a/b
        return wynik

def polekola(r):
        wynik = math.pi*r*r
        return wynik

def obwodkola(r):
        wynik = 2*math.pi*r
        return wynik

if zapytanie == 0:
    if znak == "*":
        print(mnozenie(a,b))
    elif znak == "+":
         print(dodawanie(a,b))
    elif znak == "-":
         print(odejmowanie(a,b))
    elif znak == "/":
         print(dzielenie(a,b))

elif zapytanie == 1:
    print("Pole: "+str(polekola(r))+"\n"+"Obwód: "+str(obwodkola(r)))

'''

#Zadanie 5

'''

def sumalisty(lista):
    x = 0
    suma = 0
    while x < len(lista):
        suma = suma + lista[x]
        x = x + 1
    return suma

def funkcja(metoda):
    suma = 0
    try:
        file = open("plik_odczytu_liczb.txt", "r")
        for line in file:
            suma = suma + int(line)
    finally:
        file.close()
    wyniksumowaniawszytkiego = int(metoda) + int(suma)
    return wyniksumowaniawszytkiego

lista = [3, 2, 10, 5]
print(funkcja(sumalisty(lista)))

'''

#Zadanie 6

'''
import math

zapytanie = int(input("Wprowadź:"+"\n"+"1 - aby obliczyć pole i obwód koła"+"\n"+"0 - aby użyć domyślnego kalkulatora: "))

if zapytanie == 0:
    a = int(input("Podaj liczbe a "))
    b = int(input("Podaj liczbe b "))
    znak = input("Podaj znak ")
elif zapytanie == 1:
    r = int(input("Podaj promień "))
else:
    print("Podano błędną wartość")

def mnozenie(a,b):
    wynik = a*b
    return wynik

def dodawanie(a,b):
    wynik = a+b
    return wynik

def odejmowanie(a,b):
    wynik = a-b
    return wynik

def dzielenie(a,b):
    if b==0:
         return "Błąd - nie można dzielić przez 0"
    else:
        wynik = a/b
        return wynik

def polekola(r):
        wynik = math.pi*r*r
        return wynik

def obwodkola(r):
        wynik = 2*math.pi*r
        return wynik

def zapisz(r):
    try:
        file = open("Zapisany_Plik.txt", "w")
        file.write("Pole: "+str(math.pi)+"*"+str(r)+"*"+str(r)+"=")
        file.write(str(polekola(r))+"\n")
        file.write("Obwód: "+"2*"+str(math.pi)+"*"+str(r)+"=")
        file.write(str(obwodkola(r)))
        print("Zapisano do pliku!")
    finally:
        file.close()


if zapytanie == 0:
    if znak == "*":
        print(mnozenie(a,b))
    elif znak == "+":
         print(dodawanie(a,b))
    elif znak == "-":
         print(odejmowanie(a,b))
    elif znak == "/":
         print(dzielenie(a,b))
elif zapytanie == 1:
    zapisz(r)
    print("Pole: "+str(polekola(r))+"\n"+"Obwód: "+str(obwodkola(r)))
    

'''

#Zadanie 7
'''

import math

a = int(input("Podaj liczbe a "))
b = int(input("Podaj liczbe b "))
c = int(input("Podaj liczbe c "))


def wynikrownaniakwadratowego(a,b,c):
    delta = b*b-4*a*c
    if delta < 0:
        wynik = "Równanie nie ma rozwiązań rzeczywistych."+"\n"
        try:
            file = open("result.txt", "a")
            file.write(wynik)
            print("Zapisano do pliku!")
        finally:
            file.close()
        return wynik
    elif delta == 0:
         wynikx0 = -b/(2*a)
         wynik = "x0="+str(wynikx0)+"\n"
         try:
            file = open("result.txt", "a")
            file.write(wynik)
            print("Zapisano do pliku!")
         finally:
            file.close()
         return wynik
    else: # delta > 0
        wynikx1 = -b-math.sqrt(delta)/(2*a)
        wynikx2 = -b+math.sqrt(delta)/(2*a)
        wynik = "x1="+str(wynikx1)+"\n"+"x2="+str(wynikx2)+"\n"
        try:
            file = open("result.txt", "a")
            file.write(wynik)
            print("Zapisano do pliku!")
        finally:
            file.close()
        return wynik

print(wynikrownaniakwadratowego(a,b,c))
'''


