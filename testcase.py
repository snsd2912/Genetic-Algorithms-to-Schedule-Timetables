#!/usr/bin/env python
# -*- coding: utf-8 -*-
from exams import exams, exams1_indexes, exams2_indexes, exams3_indexes, extra_exams_indexes


# Number of students for particular year
students1 = 200
students2 = 170
students3 = 130

# Maps year to list of students (each student is represented as a list of exams)
students_exams = {
    1: [list(exams1_indexes[:]) for _ in range(students1)],
    2: [list(exams2_indexes[:]) for _ in range(students2)],
    3: [list(exams3_indexes[:]) for _ in range(students3)],
}

# Introducing real life situations that some students from year 2 and 3 didn't pass
# exams from previous year

# print(students_exams[2][1])


# 20 students didn't pass 'Ly thuyet thong tin'
physics_exam = exams.index('Ly thuyet thong tin')
for i in range(50):
    students_exams[2][i].append(physics_exam)

physics_exam = exams.index('Xu ly anh')
for i in range(40):
    students_exams[2][i+100].append(physics_exam)

physics_exam = exams.index('Ki thuat do hoa')
for i in range(30):
    students_exams[2][i+100].append(physics_exam)

# 30 students didn't pass 'Co so du lieu phan tan'
physics_exam = exams.index('Co so du lieu phan tan')
for i in range(30):
    students_exams[3][i].append(physics_exam)

physics_exam = exams.index('Lap trinh web')
for i in range(20):
    students_exams[3][i+90].append(physics_exam)



extra_exams_count = len(extra_exams_indexes)
# each student has 2 extra subjects exams
for student_year in students_exams.keys():
    for student_index, student_exams_list in enumerate(students_exams[student_year]):
        first_exam_index = student_index % (extra_exams_count-1)
        second_exam_index = first_exam_index + 1

        student_exams_list.append(extra_exams_indexes[first_exam_index])
        student_exams_list.append(extra_exams_indexes[second_exam_index])

