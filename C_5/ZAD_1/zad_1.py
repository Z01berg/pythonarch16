import csv
import smtplib


def punktacja(number):
    if number <= 50:
        return 2
    elif number > 51 and number <= 60:
        return 3
    elif number > 71 and number <=80:
        return 4
    elif number > 81 and number <= 90:
        return 4.5
    elif number > 91 and number <= 100:
        return 5

def wczytanie_pliku(filename):
    data = {}
    with open(filename, "r") as f:
        for line in f:
            if not line.strip():  # Sprawdź, czy wiersz nie jest pusty
                continue
            row = line.strip().split(',')
            if len(row) < 4:  # Sprawdź, czy wiersz ma wystarczającą ilość pól
                continue
            data[row[0]] = {
                "imie": row[1],
                "nazwisko": row[2],
                "punkty": int(row[3]),
                "ocena": None,
                "status": ""
            }
            if len(row) >= 5:
                data[row[0]]["ocena"] = float(row[4])
            if len(row) >= 6:
                data[row[0]]["status"] = row[5]
    return data


def zapisz_do_pliku(filename, students):
    with open(filename, "w") as f:
        writer = csv.writer(f)
        for student_email, student_data in students.items():
            row = [student_email, student_data.get('imie'), student_data.get('nazwisko'), student_data.get('punkty')]
            if student_data.get('ocena') is not None:
                row.extend([student_data.get('ocena'), student_data.get('status')])
            writer.writerow(row)

def dodaj_studenta(email2):
    email = email2
    if email in students:
        print("Student o podanym adresie email już istnieje")
        return students
    imie = input("Podaj imię studenta: ")
    nazwisko = input("Podaj nazwisko studenta: ")
    punkty = int(input("Podaj liczbę uzyskanych punktów z przedmiotu: "))
    student = {"email": email, "imie": imie, "nazwisko": nazwisko, "punkty": punkty, "ocena": None, "status": ""}
    students.update({email: student})
    return students

def usun_studenta(mail):
    del students[mail]
    return students

def wyslij_email(students, email_sender, password):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_sender, password)

    for email, student in students.items():
        if student['status'] == '':
            msg = f"Subject: Wynik z przedmiotu Podstawy Programowania Python\n\nWitaj {student['imie']}, Twoja ocena z przedmiotu to {student['ocena']}.\n"
            server.sendmail(email_sender, email, msg)
            student['status'] = 'MAILED'
    server.quit()

def wystaw_oceny(students):
    for student in students.values():
        if student['status'] not in ['GRADED', 'MAILED']:
            ocena = punktacja(int(student['punkty']))
            student['ocena'] = ocena
            student['status'] = 'GRADED'



students = wczytanie_pliku("students.txt")

print(students)

dodaj_studenta('zaharzubik@gmail.com')
print(students)

wystaw_oceny(students)
print(students)

usun_studenta("adamadamski@gmail.com")
print(students)

wyslij_email(students, "poczta", "pass")
print(students)

zapisz_do_pliku("studentsu.txt", students)