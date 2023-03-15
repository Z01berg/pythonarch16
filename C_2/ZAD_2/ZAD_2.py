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
    wynik = int(responseA) * int(responseB)
elif responseC == "/":
    wynik = int(responseA) / int(responseB)
else:
    print("Żle wprowadzone dane!!!")

print(responseA, responseC, responseB, " = ", wynik)