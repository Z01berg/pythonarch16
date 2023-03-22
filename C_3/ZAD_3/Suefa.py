import random
import getpass

def Wypisz (history, player1, player2):
    punktacja = punkty1(history), '/', punkty2(history)
    wynik = "hi"
    if punkty1(history) > punkty2(history):
        wynik = "Wygrał {}".format(player1)
    elif punkty1(history) == punkty2(history):
        wynik = "{} DRAW {}".format(player1, player2)
    else:
        wynik = "Wygrał {}".format(player2)

    print("Wynik: {}\nRachunek: {}".format(wynik, punktacja))
def skip():
    for i in range(1, 15):
        if i < 5:
            print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
        elif i < 10:
            print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        elif i < 14:
            print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
        else:
            print()
def ktoWygra (input1, input2, a, b):

    if (input1 == "1" and input2 == "2") or (input1 == "2" and input2 == "3") or (input1 == "3" and input2 == "1"):
        wynik = ("1 Wygrał {}".format(a))
        return wynik
    elif (input2 == "1" and input1 == "2") or (input2 == "2" and input1 == "3") or (input2 == "3" and input1 == "1"):
        wynik = ("2 Wygrał {}".format(b))
        return wynik
    elif input1 == input2:
        wynik = "3 Draw"
        return wynik
    else:
        wynik = "restart"
        return wynik

def losowanieKomp():
    losowanie = str(random.randrange(1, 4))
    return losowanie

def punkty1(history):
    a = 0

    for i in range(0, len(history)):
        if i % 2 == 0:
            b = int(history[i][0])
            i += 2
            if b == 1:
                a += 1

    return a

def punkty2(history):
    a = 0

    for i in range(0, len(history)):
        if i % 2 == 0:
            b = int(history[i][0])
            i += 2
            if b == 2:
                a += 1

    return a


iRund = int(input("Podaj ilość rund: \n"))

wybor = input("Gracz VS Gracz (2) lub Gracz VS AI (1): \n")

if wybor == "2":

    wybor = input("local (1) czy get pass (2)")
    if wybor == "2":
        print("Gracz 2 jako domyślny GetPass")

        player1 = input("Nazwa gracza 1: \n")
        player2 = getpass.getpass('Nazwa gracza 2: \n')

        history = []

        while iRund > 0:
            print("Runda gracza {}".format(player1))
            aa = input("Papier - 1\n" + "Kamien - 2\n" + "Nozyce - 3\n")

            skip()

            print("Runda gracza {}".format(player2))
            bb = getpass.getpass('Papier - 1\n" + "Kamien - 2\n" + "Nozyce - 3\n')

            cc = ktoWygra(aa, bb, player1, player2)

            if cc == "restart":
                iRund += 1

            history.append(aa)
            history.append(bb)
            history.append(cc)
            history.append("Round {}".format(iRund))

            iRund -= 1

            skip()
        print(history)
        Wypisz(history, player1, player2)

    else:
        player1 = input("Nazwa gracza 1: \n")
        player2 = input("Nazwa gracza 2: \n")

        history = []


        while iRund > 0:
            print("Runda gracza {}".format(player1))
            aa = input("Papier - 1\n"+"Kamien - 2\n"+"Nozyce - 3\n")

            skip()

            print("Runda gracza {}".format(player2))
            bb = input("Papier - 1\n"+"Kamien - 2\n"+"Nozyce - 3\n")

            cc = ktoWygra(aa, bb, player1, player2)

            if cc == "restart":
                iRund += 1

            history.append(aa)
            history.append(bb)
            history.append(cc)
            history.append("Round {}".format(iRund))

            iRund -= 1

            skip()
        print(history)
        Wypisz(history, player1, player2)


if wybor == "1":
    player1 = input("Nazwa gracza 1: \n")
    player2 = "AI"
    history = []

    while iRund > 0:
        print("Runda gracza {}".format(player1))
        aa = input("Papier - 1\n" + "Kamien - 2\n" + "Nozyce - 3\n")

        skip()

        print("Runda gracza {}".format(player2))
        bb = losowanieKomp()
        print(bb)

        cc = ktoWygra(aa, bb, player1, player2)

        if cc == "restart":
            iRund += 1

        history.append(aa)
        history.append(bb)
        history.append(cc)
        history.append("Round {}".format(iRund))

        iRund -= 1

        skip()

    print(history)
    print(Wypisz(history, player1 ,player2))


