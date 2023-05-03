from Stos import Stos
from Student import Student
stos = Stos(2)
stos.push(1)
stos.push(2)
stos.push(3)

print(stos)

print(stos.pop())
print(stos.pop())
print(stos.pop())

print(stos)

student = Student("lukasz@gmail.com", "lukasz", "kwasniewicz")
student2 = Student("lukasz@gmail.com", "adam", "zdun")
print(student)
print(repr(student))
s2 = eval(repr(student))
print(s2)

print( student == s2)

print(Student.compareStudentsNames(student, student2))
print(Student.compareStudentsSurnames(student, student2))

def alphabeticGreater(x,y,func):
    return func(x,y)

print("alpha",alphabeticGreater(student,student2,Student.compareStudentsNames))

email, name, surname = student.getPersonalData()
print(email, name, surname)
