#!/usr/bin/python
# -*- coding: utf-8 -*-
PLANT_NAMES = {
            'R': 'Radishes',
            'C': 'Clover',
            'G': 'Grass',
            'V': 'Violets',
            }
STUDENTS = [
        'Alice',
        'Bob',
        'Charlie',
        'David',
        'Eve',
        'Fred',
        'Ginny',
        'Harriet',
        'Ileana',
        'Joseph',
        'Kincaid',
        'Larry',
        ]

class Garden:

    def __init__(self, diagram, students=STUDENTS):
        
        self.students = sorted(students)

        self.clusters = diagram.split('\n')

        self.belongings = {}
        for student in self.students:
            student_pos = self.students.index(student) * 2
            front_two = (self.clusters[0])[student_pos:student_pos + 2]
            back_two = (self.clusters[1])[student_pos:student_pos + 2]

            student_has = front_two + back_two

            self.belongings[student] = [PLANT_NAMES[letter]
                    for letter in student_has]

    def plants(self, student):
        return self.belongings[student]