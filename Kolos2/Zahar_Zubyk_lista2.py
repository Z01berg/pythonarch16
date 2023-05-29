import ssl
import pandas as pd
from sklearn import preprocessing

ssl._create_default_https_context = ssl._create_unverified_context

# Wczytaj dane z adresu podanego w pliku tekstowym: pliktextowy.txt
# do ramki danych.
# Użyj reszty wierszy jako nagłówków ramki danych.
# Uwaga! Zobacz która zmienna jest zmienną objaśnianą, będzie to potrzebne do dalszych zadań.

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None)

# Zadanie 1: przypisz nazwy kolumn z df w jednej linii: (2pkt)
wynik1 = df.columns.tolist()
print(wynik1)

# Zadanie 2: Wypisz liczbę wierszy oraz kolumn ramki danych w jednej linii. (2pkt)
wynik2 = f"Liczba wierszy: {df.shape[0]}, liczba kolumn: {df.shape[1]}"
print(wynik2)


# Zadanie 3: Utwórz klasę Wine na podstawie wczytanego zbioru: (3pkt)
# wszystkie zmienne objaśniające powinny być w liscie.
# Zmienna objaśniana jako odrębne pole.
# metoda __init__ powinna posiadać 2 parametry:
# listę (zmienne objaśniające) oraz liczbę(zmienna objaśniana).
# nazwy mogą być dowolne.
class Wine:
    def __init__(self, features, target):
        self.features = features
        self.target = target

    def __repr__(self):
        return f"Wine(features={self.features}, target={self.target})"


# Zadanie 4: (3pkt)
# Zapisz wszystkie dane z ramki danych do listy obiektów typu Wine.
# Nie podmieniaj listy, dodawaj elementy.
# Uwaga! zobacz w jakiej kolejności podawane są zmienne objaśniane i objąśniająca.
# Podpowiedź: zobacz w pliktextowy.txt
wineList = []
for i in range(len(df)):
    features = df.iloc[i, 1:].tolist()
    target = df.iloc[i, 0]
    wineList.append(Wine(features, target))

wynik4 = len(wineList)
print(wynik4)


# Zadanie 5: Weź ostatni element z listy i na podstawie (3pkt)
# wyniku funkcji repr utwórz nowy obiekt - eval(repr(obiekt))
# do wyniku przypisz zmienną objaśnianą z tego obiektu:
last_wine = wineList[-1]
new_wine = eval(repr(last_wine))
wynik5 = new_wine.target
print(wynik5)


# Zadanie 6: (3pkt)
# Zapisz ramkę danych do bazy SQLite nazwa bazy (dopisz swoje imię i nazwisko):
# wines_imie_nazwisko, nazwa tabeli: wines.
# Następnie wczytaj dane z tabeli wybierając z bazy danych tylko wiersze z typem wina nr 3
# i zapisz je do nowego data frame:
import sqlite3

conn = sqlite3.connect('wines_Zahar_Zubyk.db')
df.to_sql('wines', conn, if_exists='replace', index=False)

query = "SELECT * FROM wines WHERE \"TypeOf\" = 3"
df_filtered = pd.read_sql_query(query, conn)

wynik6 = df_filtered
print(wynik6.shape)


# Zadanie 7: (1pkt)
# Utwórz model regresji Logistycznej z domyślnymi ustawieniami:
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

wynik7 = model.__class__.__name__
print(wynik7)


# Zadanie 8: (3pkt)
# Dokonaj podziału ramki danych na dane objaśniające i do klasyfikacji.
# Znormalizuj dane objaśniające za pomocą:
# X = preprocessing.normalize(X)
# Wytrenuj model na wszystkich danych bez podziału na zbiór treningowy i testowy.
# Wykonaj sprawdzian krzyżowy, używając LeaveOneOut() zamiast KFold (Parametr cv)
# Podaj średnią dokładność (accuracy)

X = df.iloc[:, 1:].values
y = df.iloc[:, 0].values

X = preprocessing.normalize(X)

model.fit(X, y)

from sklearn.model_selection import cross_val_score, LeaveOneOut

accuracy = cross_val_score(model, X, y, cv=LeaveOneOut()).mean()

wynik8 = accuracy
print(wynik8)
