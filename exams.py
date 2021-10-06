#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exams for 1st year (1st semester)

exams1 = [
    'Xu ly anh',
    'Mang may tinh',
    'Ki thuat do hoa',
    'Ly thuyet thong tin',
]

# Exams for 2nd year (3rd semester)
exams2 = [
    'Lap trinh mang',
    'Lap trinh web',
    'Co so du lieu phan tan',
    'Cac he thong dua tren tri thưc',
]

# Exams for 3rd year (5rd semester)
exams3 = [
    'Cac he thong phan tan',
    'Chuyen de he thong thong tin',
    'Kho du lieu',
    'He CSDL da phuong tien'
]

extra_exams = [
    'extra1',
    'extra2',
    'extra3',
    'extra4',
    'extra5',
    'extra6'
]

exams = exams1 + exams2 + exams3 + extra_exams

exams1_indexes = range(len(exams1))

last_index = exams1_indexes[-1]
exams2_indexes = range(last_index+1, last_index+1+len(exams2))

last_index = exams2_indexes[-1]
exams3_indexes = range(last_index+1, last_index+1+len(exams3))

last_index = exams3_indexes[-1]
extra_exams_indexes = range(last_index+1, last_index+1+len(extra_exams))
