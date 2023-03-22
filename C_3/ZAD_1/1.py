
def max (tablica):
    a = 0
    for i in range(0, len(tablica)):
        if a < int(tablica[i]):
            a = int(tablica[i])

    return a

def min (tablica):
    a = 0

    for i in range(0, len(tablica)):
        if a > int(tablica[i]):
            a = int(tablica[i])

    return a

a = input("Podaj liczby przeliczone przez przecinek (ex. 1,2,3,5...): ")
b = a.split(',')
print("Mamy tablice: {}".format(b))
print("MIN: {}".format(min(b)))
print("MAX: {}".format(max(b)))


