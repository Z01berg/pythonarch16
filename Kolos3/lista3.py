#Zadanie 1 (4pkt):
#Utwórz klasę iteratora dla listy. Użyj go do wstawienia elementów listy lista1 do strina.
# elementy mają znajdować się w stringu jednym wierszu niczym nierozdzielone:
class ListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.lst):
            raise StopIteration
        value = str(self.lst[self.index])
        self.index += 1
        return value

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
wynik1 = ""

iterator = ListIterator(lista1)
for element in iterator:
    wynik1 += element

print(wynik1)

#Zadanie2: (4pkt)
#Napisz funkcję fizzbuzz(n), która używając listy składanej zwróci
#listę od 1 do n włącznie liczb lub wyrazów Fizz, Buzz, FizzBuzz, zgodnie ze standradową
#reguła gry w FizzBuzz:
#Jeśli liczba jest podzielna przez 3 i niepodzielna przez 5, zamiast liczby mamy "Fizz".
#Jeśli liczba jest podzielna przez 5 i niepodzielna przez 3, zamiast liczby mamy "Buzz".
#Jeśli liczba jest zarówno podzielna przez 3, jak i przez 5, zamiast liczby mamy "FizzBuzz".
def fizbuzz(n):
    return ['FizzBuzz' if i % 15 == 0 else 'Fizz'
            if i % 3 == 0 else 'Buzz'
            if i % 5 == 0 else
            i for i in range(1, n+1)]

wynik2 = fizbuzz(16)
print(wynik2)
#Zadanie 3 (4pkt):
#Napisz generator zwracający n wyrazów ciągu Lucasa
#do wyniku zapisz 6 element tego ciągu.
def lucas_sequence(n):
    a, b = 2, 1
    yield a
    if n > 1:
        yield b
        for _ in range(2, n):
            a, b = b, a + b
            yield b

generator = lucas_sequence(6)
wynik3 = list(generator)[-1]
print(wynik3)
#Zadanie4 (4pkt):
#Uzyj klasy napisanej na ostatnich zajęciach - wersji z iteratorem (wklej tutaj klasę)
#Do przechowywania znaków kodu javy z pliku Main.java.

class TitleReader:
    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        with open(self.filename, "r") as file:
            for line in file:
                yield line.strip()

    def __len__(self):
        count = 0
        with open(self.filename, "r") as file:
            for _ in file:
                count += 1
        return count

obiekt = "Main.java"
wynik4="wstaw w wynik4"
#następnie wstaw do niej znaki z kodu javy, które wczytasz z pliku Main.java
#ODKOMENTUJ poniższą linijkę, gdy utworzysz obiekt i dodasz do niego znaki:

wynik4 = len(obiekt)
print(wynik4)

#Zadanie 5 (4pkt):
#Napisz funkcję, która sprawdzi poprawność kodu javy, używając obiektu z poprzedniego zadania
# i uwzględniając tylko nawiasy w kodzie.
#funkcja ma zwrocic True albo False w zależności czy kod jest poprawny czy nie.

def validation(kod_o):
    stack = []

    for char in kod_o:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        elif char == ')' or char == '}' or char == ']':
            if not stack:
                return False
            opening = stack.pop()
            if (char == ')' and opening != '(') or (char == '}' and opening != '{') or (char == ']' and opening != '['):
                return False

    return len(stack) == 0 

wynik5 = validation(kod_o=obiekt)
print(wynik5)







