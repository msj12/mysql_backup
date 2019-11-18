#!/usr/bin/env python
# -*- coding: utf8 -*-

class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._name

    @age.setter
    def age(self, age):
        self._age = age

    def watch_movie(self):
        if self._age < 18:
            print(f'{self._name}正在看《熊出没》')
        else:
            print(f'{self._name}正在看《郭德纲相声集》')

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course_name):
        print(f'{self._grade}的{self.name}正在学习{course_name}')

class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course_name):
        print(f'{self._title}{self.name}正在讲{course_name}')


stu = Student('王二锤子', 16, '三年级')
stu.study('数学')
stu.watch_movie()
t = Teacher('Python', 26, '砖家')
t.teach('Python程序设计')
t.watch_movie()








