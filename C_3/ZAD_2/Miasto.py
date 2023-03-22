import random

def losowanieKomp(lista):
    losowanie = random.randrange(0, len(lista))
    return losowanie

listaW = []

moja_lista = ["Warszawa", "Kraków", "Wrocław", "Łódź", "Poznań",
"Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok"]

for index in range(0, len(moja_lista)):

    print("{} Miasto: ".format(index+1) +  moja_lista.pop(losowanieKomp(moja_lista)))



