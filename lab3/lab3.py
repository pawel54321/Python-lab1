# Zadanie 2
'''
from array import *
ilosc = int(input("Podaj ilosc liczb "))
tablica = array('i', [])
a = 0
while(a<ilosc):
    liczba2 = int(input("Podaj liczbe "))
    tablica.append(liczba2)
    a+=1
tablica.reverse()
print(tablica)
'''

# Zadanie 3
'''
from array import *
import random
tablica = array('i', [])
liczbalosowana = random.randrange(-5, 5+1)
tablica.append(liczbalosowana)
try:
    file = open("result.txt", "a")
    file.write(str(tablica)+"\n")
    print("Zapisano do pliku!")
finally:
    file.close()
'''


# Zadanie 4

'''
import numpy

def wypelnijkwadratami():
    tablica = numpy.array([[],[]],int)
    tablica.resize(5,5)
    tablica[[0],[0]] = 2
    tablica[[0],[1]] = 3
    tablica[[0],[2]] = 4
    tablica[[0],[3]] = 5
    tablica[[0],[4]] = 6
    
    for a in range (0,5):
        for i in range (1,5):
            wynik = tablica[[i-1],[a]] * tablica[[i-1],[a]]
            tablica[[i],[a]] = wynik
 
    print(tablica)
    
    
wypelnijkwadratami()


'''





# Zadanie 5

'''

def histogram(plik):
    try:
        slownik = {}
        i=0
        file = open(plik, "r")
        print("Odczytano plik!")
        for linia in file:
            while(i<len(linia)): #11
                if(linia[i]==(" ")):
                    print("Pominąłem znak pusty")
                else:
                    if(linia[i] not in slownik):
                        slownik[linia[i]] = 1
                    else:
                        slownik[linia[i]] = int(slownik.get(linia[i]))+1
                i=i+1
    finally:
        file.close()

    print(slownik)

histogram("document.txt")
'''

# Zadanie 6


'''


import random
def deck():
    karty = [('2','c'),('2','d'),('2','h'),('2','s'),
        ('3','c'),('3','d'),('3','h'),('3','s'),
        ('4','c'),('4','d'),('4','h'),('4','s'),
        ('5','c'),('5','d'),('5','h'),('5','s'),
        ('6','c'),('6','d'),('6','h'),('6','s'),
        ('7','c'),('7','d'),('7','h'),('7','s'),
        ('8','c'),('8','d'),('8','h'),('8','s'),
        ('9','c'),('9','d'),('9','h'),('9','s'),
        ('10','c'),('10','d'),('10','h'),('10','s'),
        ('J','c'),('J','d'),('J','h'),('J','s'),
        ('D','c'),('D','d'),('D','h'),('D','s'),
        ('K','c'),('K','d'),('K','h'),('K','s'),
        ('A','c'),('A','d'),('A','h'),('A','s')]
    return karty
def deal(deck, n):
    
    lista = []
 
    i=0
    while(i<n):
        if(i==0):
            lista.append([deck[0],deck[1],deck[2],deck[3],deck[4]])
            i=i+1
        else:
            lista.append([deck[i*5],deck[i*5+1],deck[i*5+2],deck[i*5+3],deck[i*5+4]])
            i=i+1
    return lista
def shuffle_deck(deck):
    kartypotasowane = []
    kartypotasowane = deck
    i=0
    liczbalosowan = 100
    while(i<liczbalosowan):
        liczbalosowana1 = random.randrange(0, 51+1)
        liczbalosowana2 = random.randrange(0, 51+1)
        temp = kartypotasowane[liczbalosowana1]
        kartypotasowane[liczbalosowana1] = kartypotasowane[liczbalosowana2]
        kartypotasowane[liczbalosowana2] = temp
        i=i+1
    
    return kartypotasowane
    


print("Wywolania do testow:")

print("Karty:")
print(deck())
print("Rozdane:")
print(deal(deck(), 5))
print("Permutacja:")
print(shuffle_deck(deck()))

Talia = []    

print("Integracja:")

print("Karty:")
Talia = deck()
print(Talia)

print("Rozdane:")
print(deal(Talia, 5))

print("Permutacja:")
Talia = shuffle_deck(Talia)
print(Talia)

print("Znowu Rozdane:")
print(deal(Talia, 5))



'''
