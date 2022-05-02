class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

        def add_courses(self, course_name):
            self.finished_course.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grade:
                lecturer.grade[course] += [grade]
            else:
                lecturer.grade[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade(self):
        grade_list = []
        for grade_values in self.grades.values():
            for grade_value in grade_values:
                grade_list.append(grade_value)
        result = round(sum(grade_list) / len(grade_list), 2)
        return result

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: ' \
              f'{self.avg_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \n' \
              f'Завершённые курсы: {", ".join(self.finished_courses)}'
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grade = {}

    def avg_grade(self):
         grade_list = []
         for grade_values in self.grade.values():
             for grade_value in grade_values:
                 grade_list.append(grade_value)
         result = round(sum(grade_list) / len(grade_list), 2)
         return result

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade()}"
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res


def avg_grade_all_students_of_courses(students_list, course_name):
    counter = 0
    avg_sum = 0
    for student in students_list:
        if course_name in student.grades:
            counter += len(student.grades[course_name])
            avg_sum += sum(student.grades[course_name])
    res = round((avg_sum / counter), 2)
    return res


def avg_grade_all_lecturers_of_courses(lecturers_list, course_name):
    counter = 0
    avg_sum = 0
    for lecturer in lecturers_list:
        if course_name in lecturer.grade:
            counter += len(lecturer.grade[course_name])
            avg_sum += sum(lecturer.grade[course_name])

    res = round((avg_sum / counter), 2)
    return res



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

some_student = Student('Ivan', 'Ivanov', 'male')
some_student1 = Student('Petr', 'Kuznetsov', 'male')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Git']
some_student1.courses_in_progress += ['Python', 'Git']
some_student1.finished_courses += ['Git']

some_reviewer = Reviewer('Vladimir', 'Usov')
some_reviewer1 = Reviewer('Oleg', 'Pechkin')
some_reviewer.courses_attached += ['Python']
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 8)
some_reviewer1.courses_attached += ['Git', 'Python']
some_reviewer1.rate_hw(some_student1, 'Git', 7)
some_reviewer1.rate_hw(some_student1, 'Git', 8)
print(some_student.grades, '\n')
print(some_student1.grades, '\n')

some_lecturer = Lecturer('Alexander', 'Vasiliev')
some_lecturer1 = Lecturer('Lev', 'Zaxarov')
some_lecturer.courses_attached += ['Git', 'Python']
some_lecturer1.courses_attached += ['Git', 'Python']
some_student.rate_lecturer(some_lecturer, 'Git', 5)
some_student.rate_lecturer(some_lecturer, 'Python', 8)
some_student.rate_lecturer(some_lecturer1, 'Git', 8)
some_student.rate_lecturer(some_lecturer1, 'Python', 7)
print(some_lecturer.grade, '\n')
print(some_lecturer1.grade, '\n')

print(some_reviewer, '\n')
print(some_lecturer, '\n')
print(some_student, '\n')

print(some_reviewer, '\n')
print(some_lecturer, '\n')
print(some_student, '\n')

print(some_reviewer1, '\n')
print(some_lecturer1, '\n')
print(some_student1, '\n')

print(some_student < some_student1, '\n')
print(some_lecturer < some_lecturer1, '\n')

lecturers_list = [some_lecturer, some_lecturer1]
students_list = [some_student, some_student1]

print(avg_grade_all_students_of_courses(students_list, 'Python'))
print(avg_grade_all_lecturers_of_courses(lecturers_list, 'Git'))


print(best_student.grades)
