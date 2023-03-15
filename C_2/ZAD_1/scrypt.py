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





