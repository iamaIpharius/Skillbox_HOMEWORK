import random


def sorting_students(student):
    perf_list = student.perf
    perf_avg = sum(perf_list) / len(perf_list)
    return perf_avg



class Student:
    def __init__(self, fio, group_number, perf):
        self.fio = fio
        self.group_number = group_number
        if isinstance(perf, list) and len(perf) == 5:
            self.perf = perf

students = []
for _ in range(10):
    name = input('Введите имя студента: ')
    group = input('Введите группу студента: ')
    perf_list = []
    for _ in range(5):
        grade = random.randint(1, 5)
        perf_list.append(grade)
    student = Student(name, group, perf_list)
    students.append(student)


for st in students:
    print(st.fio, st.perf, sorting_students(st))
students.sort(key=sorting_students)
print('\n')
for st in students:
    print(st.fio, st.perf, sorting_students(st))