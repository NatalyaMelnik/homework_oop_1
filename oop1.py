class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.medium_value = []

    def rate_lec(self, lecturer, course, grade_lec):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_for_lectures:
                lecturer.grades_for_lectures[course] += [grade_lec]
            else:
                lecturer.grades_for_lectures[course] = [grade_lec]
        else:
            return 'Ошибка'

    def medium_student_grade(self, student_grades):
        for i in student_grades.values():
            medium_grade = sum(i) / len(i)
            self.medium_value = medium_grade


    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:{self.medium_value}\nКурсы в процессе изучения:{','.join(self.courses_in_progress)}\nЗавершенные курсы:{','.join(self.finished_courses)}"


    def __lt__(self, other):
        return self.medium_value < self.medium

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    # def rate_hw(self, student, course, grade):
    #     if isinstance(student,
    #                   Student) and course in self.courses_attached and course in student.courses_in_progress:
    #         if course in student.grades:
    #             student.grades[course] += [grade]
    #         else:
    #             student.grades[course] = [grade]
    #     else:
    #         return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades_for_lectures = {}
        self.medium = []



    def medium_grade_lec(self, lecturers_grades):
        for i in lecturers_grades.values():
            medium_grade = sum(i) / len(i)
            print(medium_grade)
            self.medium = medium_grade


    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.medium}"


    def __lt__(self, other):
        return self.medium < other.medium_value




class Reviewer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.name = name
        self.surname = surname


    def rate_hw(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


lecturer_1 = Lecturer('Nata', 'Mel')
lecturer_1.courses_attached += ['Python', 'Java']

lecturer_2 = Lecturer('Vasya', 'Ivanov')
lecturer_2.courses_attached += ['Java', 'Git']

student_1 = Student('Pasha', 'Dulin', 'm')
student_1.courses_in_progress += ['Java', 'Git', 'Python']
student_1.finished_courses += ['Git']

student_2 = Student('Ruoy', 'Eman', 'f')
student_2.courses_in_progress += ['Git', 'Java', 'Python']
student_2.finished_courses += ['Веб разработчик']

# student_3 = Student('Lena', 'Panina', 'f')
# student_3.courses_in_progress += ['Python']
# student_3.finished_courses += ['Основы программирования']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python', 'Java']

reviewer_2 = Reviewer('Ivan', 'Kozlov')
reviewer_2.courses_attached += ['Git', 'Java']

student_1.rate_lec(lecturer_1, 'Java', 7)
student_1.rate_lec(lecturer_1, 'Java', 9)
student_1.rate_lec(lecturer_1, 'Python', 2)
student_1.rate_lec(lecturer_1, 'Python', 9)


student_2.rate_lec(lecturer_2, 'Java', 9)
student_2.rate_lec(lecturer_2, 'Java', 8)
student_2.rate_lec(lecturer_2, 'Python', 3)
student_2.rate_lec(lecturer_2, 'Python', 5)

student_1.rate_lec(lecturer_1, 'Java', 7)
student_1.rate_lec(lecturer_1, 'Java', 9)
student_1.rate_lec(lecturer_1, 'Python', 2)
student_1.rate_lec(lecturer_1, 'Python', 9)

student_2.rate_lec(lecturer_2, 'Git', 9)
student_2.rate_lec(lecturer_2, 'Git', 8)
student_2.rate_lec(lecturer_2, 'Git', 3)
student_2.rate_lec(lecturer_2, 'Git', 5)

print(lecturer_1.grades_for_lectures)
print(lecturer_2.grades_for_lectures)


reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_1, 'Python', 7)

reviewer_2.rate_hw(student_2, 'Java', 10)
reviewer_2.rate_hw(student_2, 'Java', 7)
reviewer_2.rate_hw(student_2, 'Java', 6)
reviewer_2.rate_hw(student_2, 'Java', 4)

print(student_1.grades)
print(student_2.grades)

student_1.medium_student_grade(student_1.grades)
student_2.medium_student_grade(student_2.grades)
lecturer_1.medium_grade_lec(lecturer_1.grades_for_lectures)
lecturer_2.medium_grade_lec(lecturer_2.grades_for_lectures)

# reviewer_1 = Reviewer('Rob', 'Toresh')
# reviewer_2 = Reviewer('Dasha', 'Sokolova')
# reviewer_1.courses_attached += ['Python', 'Java']
# reviewer_2.courses_attached += ['Python', 'Java']
print(reviewer_1)
print(reviewer_2)

print(lecturer_1)
print(lecturer_2)
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']

# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)

# print(best_student.grades)
print(student_1)
print(student_2)



student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]

def medium_mark_student(info, course):
    total = []
    for student in info:
        total.append(sum(student.grades[course])/len(student.grades[course]))
        print(f"Средняя оценка за домашние задания у студентов по {course}: {sum(total) / len(total)}")

def medium_mark_lecturer(info, course):
    total = []
    for lecturer in info:
        total.append(sum(lecturer.grades_for_lectures[course]) / len(lecturer.grades_for_lectures[course]))
    print(f"Средняя оценка у лекторов за лекции по курсу {course}: {sum(total) / len(total)}")

medium_mark_student(student_list, "Git")
medium_mark_student(student_list, "Java")

medium_mark_lecturer(lecturer_list, "Python")
medium_mark_lecturer(lecturer_list, "Java")

# def medium_mark_student(student_list, course):
#     total = 0
#     counter = 0
#     for student in student_list:
#         if course in student.courses_in_progress:
#             medium_course_student = sum(student.grades[course]) / len(student.grades[course])
#             total += medium_course_student
#             counter += 1
#     if counter == 0:
#         return "Такой курс никто не изучает"
#     else:
#         return f"Средний балл по курсу '{course}': {total /counter}"
#
# medium_mark_student(student_list, 'Git')
