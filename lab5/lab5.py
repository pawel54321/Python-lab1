
# Zadnie 2

'''
class Student:
    def __init__(self, imie, nr_albumu):
        self.imie = imie
        self.nr_albumu = nr_albumu


Student1 = Student("Zosia", 344442)
Student2 = Student("Kasia", 355442)
Student3 = Student("Basia", 433558)

print Student1.imie
print Student2.imie
print Student3.nr_albumu
'''


#Zadanie 3

'''
class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko


class Student(Osoba):
    def __init__(self,imie,nazwisko, nr_albumu):
        Osoba.__init__(self,imie,nazwisko)
        self.nr_albumu = nr_albumu
        
    def wypisz(self):
        print ("Imie: "+self.imie,"Nazwisko: "+self.nazwisko,"Nr_albumu: "+str(self.nr_albumu))
        
Obiekt1 = Student("Zosia", "Nowak", 345342)
Obiekt1.wypisz()
Obiekt2 = Student("Malgosia", "Kowalska", 563856)
Obiekt2.wypisz()
Obiekt3 = Student("Zosia", "Nowak", 753894)
Obiekt3.wypisz()

'''


#Zadanie 4

'''


class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko


class Student(Osoba):
    def __init__(self,imie,nazwisko, nr_albumu):
        Osoba.__init__(self,imie,nazwisko)
        self.nr_albumu = nr_albumu
        
    def przedstaw_sie(self):
        print ("Czesc nazywam sie "+ self.imie +" "+ self.nazwisko + " i moj numer albumu to "+ str(self.nr_albumu))
        
        
Obiekt1 = Student("Zosia", "Nowak", 345342)
Obiekt1.przedstaw_sie()
Obiekt2 = Student("Malgosia", "Kowalska", 563856)
Obiekt2.przedstaw_sie()
Obiekt3 = Student("Zosia", "Nowak", 753894)
Obiekt3.przedstaw_sie()

'''



#Zadanie 5

'''
class Liczba:
    def __init__(self, liczba):
        self.liczba = liczba
        
    def __add__(self,other):
        return self.liczba*self.liczba+2*self.liczba*other.liczba+other.liczba
        
        
Obiekt1 = Liczba(1)

Obiekt2 = Liczba(4)

print (Obiekt1+Obiekt2)

'''

#Zadanie 6


'''

class Dog:
    count = 0  # this is a class variable
    dogs = []  # this is a class variable

    def __init__(self, name):
        self.name = name  # self.name is an instance variable
        Dog.count += 1
        Dog.dogs.append(name)

    def bark(self, n):  # this is an instance method
        print("{} says: {}".format(self.name, "woof! " * n))

    @staticmethod
    def liczba_pieskow():
          print("Liczba obiektow: "+str(Dog.count))
          for a in range(0,len(Dog.dogs)):
            print (str(a+1)+": "+Dog.dogs[a])
            

Obietk1 = Dog("Ciapek")
Obietk1.liczba_pieskow()
Obietk2 = Dog("Mirek")
Obietk2.liczba_pieskow()


'''

#Zadanie 7


'''
class Pizza:
    pineapple = False
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return self.pineapple

    def setPineapple(self, value):
        self.pineapple = value



pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.setPineapple(True)
print(pizza.pineapple_allowed)


'''







