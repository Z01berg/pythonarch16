import sys

a = 1000
print(id(a))

a = "tekst"
print(id(a))

print(sys.getsizeof(a))

print(type(a))
a = 100
print(type(a))
a = 100.60
print(type(a))
a = False
print(type(a))

print(type(id(a)))
print(type(id))

a = b = 5
print(id(a), id(b))

b = 2000
print(id(a), id(b))

# 1-true 0-false
print(bool(254))#tylko przy 0 false
print(bool("4565"))# ""-false

print(int("234"))
print(float("234.5"))
print(int(float("234.99")))#odcina nie zaogrągla
print(round(float("234.99")))


a = 58
b = 90

if a > b :
    print("a > b")
elif a < b :
    print("a < b")
else:
    print("a == b")
print("ZAD_1_a,b▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
a = "Python 2023"
b = "Python 2023"
c = "Python 2023"

print(a == b)
print(b == c)

print(type(a))
print(type(b))
print(type(c))

print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))

print("ZAD_1_c▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
c = "Java 11"

print(a == b)
print(b == c)

print(type(a))
print(type(b))
print(type(c))

print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))

print("ZAD_2▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")

print("Podaj pierwszą liczbę (int): ")
responseA = input()
print("Podaj drugą liczbę (int): ")
responseB = input()
print("Podaj znak (+, -, *, /): ")
responseC = input()

if responseC == "+":
    wynik = int(responseA) + int(responseB)
elif responseC == "-":
    wynik = int(responseA) - int(responseB)
elif responseC == "*":
    wynik = int(responseA) * (responseB)
elif responseC == "/":
    wynik = int(responseA) / int(responseB)
else:
    print("Żle wprowadzone dane!!!")

print(responseA, responseC, responseB, " = ", wynik)

print("ZAD_3▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")

print("Podaj pierwszą liczbę (int): ")
responseA = input()
print("Podaj drugą liczbę (int): ")
responseB = input()
print("Podaj znak (+, -, *, /): ")
responseC = input()

