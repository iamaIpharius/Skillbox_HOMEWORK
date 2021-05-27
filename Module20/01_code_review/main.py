students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


for id_of_student, age_of_student in students.items():
    print(id_of_student, age_of_student['age'])


def super_fun(dictionary):
    interests = set()
    lenght_of_surname = 0

    for _, value in dictionary.items():
        interests = interests | set(value['interests'])
        lenght_of_surname += len(value['surname'])
    return interests, lenght_of_surname


total_inter, total_len = super_fun(students)
print(total_inter, '\n', total_len)