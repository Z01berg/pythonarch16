# [Zajęcia 6](ZAD_1/lab5.pdf)

- [x] [Zadanie1
Napisz klasę MyLinkedList – która będzie posortowana,wiązana oraz jednostronna.
Używając dodatkowo klasy:
class Element:
def __init__(self, data=None, nextE=None):
self.data = data
self.nextE = nextE
Klasa MyLinkedList zawiera pola:
...
self.head = None
self.tail = None
self.size = 0
z metodami:
__str__ - reprezentacja napisowa listy – wszystkie elementy listy (5%)
get(self, e) – zwraca element, (5%)
delete(self,e) – usuwa wskazany element,
(25%)
append (self, e, func=None) – dodaje elementy do listy w sposób posortowany. (25%)
func – jaki będzie warunek sortownia – określi funkcja, jeżeli None – zwykłe porównanie 2
obiektów za pomocą >=](./ZAD_1)
- [x]  [Zadanie2 (40%):
Zmodyfikować zadanie z poprzednich zajęć tak aby używała klasy Student ,MySortedList oraz aby
ocenianie przebiegało zgodnie z zasadami zaliczenia:
1 ocena za projekt – 40 pkt
3 oceny z list z zadaniami – 20 pkt każda
Oceny z prac domowych.
W zależności od średniej z prac domowych, należy zastąpić najsłabsze oceny z list od 1 do 3.
60% - jedna lista (20pkt)
70% - dwie listy (40pkt)
80% - trzy listy (60 pkt)
Ocenę końcową można wystawić tylko kiedy wszystkie oceny cząstkowe są wystawione.
Należy umożliwić przy wysyłaniu emaila podanie nowego statusu, oraz umożliwić podanie
statusów, przy których chcemy wysyłać email. E-mail można wysłać zawsze jeżeli status na to
pozwala.](./ZAD_2)



