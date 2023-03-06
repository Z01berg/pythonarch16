

Zajęcia 1

Dlaczego Python?

Darmowy

Nowoczesna i czytelna składnia

Prosty na start, jednocześnie posiadający rozbudowane biblioteki oraz społeczność.

Dynamiczne typowanie nie wymaga podawania typu zmiennych

Bardzo wiele zastosowań – aplikacje webowe, data science

Wady:

Jest to język interpretowany, wolniejszy niż języki kompilowane.

Dynamiczne typowanie – może być wadą jak i zaletą – brak statycznego typowania może

powodować błędy trudne do wychwycenia.

Przed rozpoczęciem pracy, należy pobrać Pythona ze strony:

<https://www.python.org/downloads/>

Aby móc wywołać Pythona z konsoli należy dodać do zmiennej środowiskowej PAT H jego ścieżkę.

Można zrobić to podczas instalacji.

Podczas instalacji można też zmienić ścieżkę i zrezygnować z dodatkowych opcji ( dokumentacja,

moduły Tkinter, menadżer pakietów pip, czy narzędzi testowania).

Jeżeli instalacja się udała polecenie wpisane w konsoli: python --version powinna zwrócić nam

aktualną zainstalowaną wersję Pythona.





Studenci wykorzystując uczelnianego e-maila mogą uzyskać licencję na oprogramowanie JetBrains

takie jak IntelliJ Idea, czy PyCharm:

https://account.jetbrains.com/licenses

I zainstalować wersję **Professional** do celów edukacyjnych.

Po zainstalowaniu Pycharm’a należy aktywować licencję za pomocą konta

Następnie możemy utworzyć nowy projekt w Pycharm (Pure Python):





import webbrowser

if \_\_name\_\_ == '\_\_main\_\_':

print("hello world")

url = input("Podaj stronę internetową: ")

webbrowser.open(url)

Jak widać przy tworzeniu projektu utworzyliśmy nowe środowisko wirtualne (virtualenv)

Dla każdego projektu dobrym pomysłem jest utworzenie nowego środowiska wirtualnego – w celu

uniknięcia konfliktów modułów i pakietów ( np. 2 różne projekty używają tego samego modułu ale

w różnej wersji ).

Przykładowy program importuje moduł webbrowser, Sprawdza czy \_\_name\_\_ jest równe

\_\_main\_\_ , ma to na celu sprawdzenie czy plik jest uruchamiany bezpośrednio – jako skrypt, czy

poprzez import.

*https://codecouple.pl/2016/02/27/python-specjalna-zmienna-\_\_name\_\_/*

Jeżeli jest uruchamiany jako skrypt wyświetla napis „hello world”, prosi o podanie strony i otwiera

ją w przeglądarce.

Pythona można używać też za pomocą interaktywnej powłoki:





Również możemy uruchomić skrypt w wirtualnym środowisku:

W wirtualnym środowisku zainstalujemy moduł pozwalający odtworzyć mp3:

(moduł wymaga 64 bitowej biblioteki z programu vlc – libvlc.dll )

<https://get.videolan.org/vlc/3.0.18/win64/vlc-3.0.18-win64.exe>

Tworzenie wirtualnego środowiska i instalacja pakietu:





Alternatywna wersja bez VLC:

pip install playsound

from playsound import playsound

playsound('/path/file.mp3')

Git:

Pobieramy Gita ze strony: <https://gitforwindows.org/>[ ](https://gitforwindows.org/)i instalujemy z domyślnymi ustawieniami.

Zakładamy konto na githubie (https://github.com/) oraz tworzymy nowe repozytorium:

Sklonujemy repozytorium z githaba lokalnie:





git clone <https://github.com/pjagiter/pythonArchive.git>

Ustawiamy nazwę użytkownika i email w konsoli:

C:\Users\luke>git config --global user.name "user"

C:\Users\luke>git config --global user.email "<user@pjwstk.edu.pl>"

Możemy skopiować skrypt z projektu utworzonego w pycharmie (main.py)

do katalogu ze sklonowanym repozytorium.

Dodajemy pliki do repozytorium: git add .

Robimy commit dodając komentarz, np. : git commit -m "skrypt otwierajacy strone"

Zanim wrzucimy zmiany sprawdzimy, czy nie ma innych zmian w repozytorium za pomocą git pull

Następnie wrzucamy zmiany na serwer github używając git push

Po poprawnym zalogowaniu zmiany zostaną wrzucone na serwer.





Zadania:

1\. Zainstalować na swoim komputerze Python’a

2\. oraz PyCharm.

3\. Utworzyć nowe środowisko wirtualne zainstalować moduł do odtwarzania dźwięku i odtworzyć

mp3 – w skrypcie.

4\. Zmodyfikować skrypt z github tak aby pobierał archiwalne 3 wersje podanej strony internetowej

wysłać zmiany na github. ( będzie potrzebny dodatkowy moduł -requests)

#przyklad działania:

#pageurl – pobrana strona, date-data w formacie rok miesiac dzien np. 20230126

#zapytanie do api:

#http://archive.org/wayback/available?url=example.com&timestamp=20060101

url = "http://archive.org/wayback/availableurl="+pageurl+"&timestamp="+str(date)

response = requests.get(url)

d = response.json()

page = d["archived\_snapchots"]["closest"]["url"]

webbrowser.open(page)

5\. Dlaczego w Pythonie mówi się o interpreterze, a w javie o maszynie wirtualnej?

Całość - kod, polecenia z konsoli, screeny stron internetowych i odpowiedź na pytanie umieścić w

pdf na teams w przypisanym Zadaniu .

