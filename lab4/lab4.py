
#Zadanie 2
'''

x = int(input("Podaj liczbe x: "))

liczba = lambda z:z

for a in range (1,x+1):
    print(liczba(a))

'''
#Zadanie 3
'''
nums = [1, 2, 3, 5, 8, 3, 0, 7]
res = list(filter(lambda x: x > 4, nums))
print(res)
'''
# Zadanie 4
'''
def generator(x):
    tekst=""
    for i in range(len(x)):
        tekst = tekst + x[i]
        yield tekst

print(list(generator("spam")))
'''

#Zadanie 5
'''
x = int(input("Podaj x"))

def decor(func,x):
    def wrap():
        print("==================")
        print("Wynik = " + str(x+2*x))
        func()
        print("==================")
    return wrap

def print_text():
    print(str(x)+"+2*"+str(x))

decorated = decor(print_text,x)
decorated()
'''
#Zadanie 6
'''
def newton(n,k):
    if k==0 or k==n:
        return 1 
    elif k<n and k>0:
        return newton(n-1,k-1)+newton(n-1,k)
    else:
        return 0

print(newton(10,5))
'''

#Zadanie 7
'''
koszyk = set(["jajka", "chleb"])


print("Zawartosc koszyka:")
print(koszyk)

print("\'Dlugosc\' koszyka:")
print(len(koszyk))

print("Dodanie produktu do koszyka:")
koszyk.add("owoce")
print(koszyk)

print("Wyciagniecie produktu \'chleb\' z koszyka:")
koszyk.remove("chleb")
print(koszyk)

print("Wyciagniecie (pierwszego w liscie) produktu \'owoce\' z koszyka:")
koszyk.pop()
print(koszyk)
'''
