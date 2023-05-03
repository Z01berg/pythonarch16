
#     __init__: Metoda ta jest wywoływana podczas tworzenia nowego obiektu klasy i służy do inicjalizacji jego właściwości. Jest to tzw. konstruktor klasy.
#
#     __eq__: Ta metoda definiuje sposób porównywania dwóch obiektów klasy. Domyślnie Python porównuje obiekty na podstawie ich identyczności (czyli czy to są dokładnie te same obiekty w pamięci), ale można zdefiniować własne kryteria porównywania.
#
#     __str__: Ta metoda definiuje sposób konwersji obiektu na łańcuch znaków. Jest to tzw. reprezentacja w postaci łańcucha znaków.
#
#     __repr__: Ta metoda definiuje sposób reprezentowania obiektu w postaci kodu Pythona. Jest to tzw. reprezentacja w postaci kodu.
#
#     __co__: Jest to metoda używana wraz z klasami asynchronicznymi (async/await). Definiuje to obiekt wykorzystywany do asynchronicznego obliczania wartości.##

class Element:
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + " "
            current = current.nextE
        return result.strip()

    def get(self, e):
        current = self.head
        while current is not None:
            if current.data == e:
                return current
            current = current.nextE
        return None

    def delete(self, e):
        if self.head is None:
            return
        if self.head.data == e:
            self.head = self.head.nextE
            if self.head is None:
                self.tail = None
            self.size -= 1
            return
        current = self.head
        while current.nextE is not None:
            if current.nextE.data == e:
                current.nextE = current.nextE.nextE
                if current.nextE is None:
                    self.tail = current
                self.size -= 1
                return
            current = current.nextE

    def append(self, e, func=None):
        new_element = Element(e)
        if self.head is None:
            self.head = new_element
            self.tail = new_element
            self.size += 1
            return
        if func is None:
            func = lambda x, y: x >= y
        current = self.head
        previous = None
        while current is not None and func(current.data, e):
            previous = current
            current = current.nextE
        if previous is None:
            self.head = new_element
        else:
            previous.nextE = new_element
        new_element.nextE = current
        if current is None:
            self.tail = new_element
        self.size += 1
