from datetime import datetime
import math
import numpy as np


class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_mark(self, course_id, mark, credits):
        self.marks[course_id] = {'mark': math.floor(mark * 10) / 10, 'credits': credits}

    def calculate_gpa(self):
        if not self.marks:
            return 0

        mark_credits = np.array([(mark_info['mark'], mark_info['credits']) for mark_info in self.marks.values()], dtype=object)
        total_credits = np.sum(mark_credits[:, 1])
        weighted_sum = np.sum(mark_credits[:, 0] * mark_credits[:, 1])

        return weighted_sum / total_credits

    def __str__(self):
        return f'Student ID: {self.id}, Student Name: {self.name}, GPA: {self.calculate_gpa():.1f}'


class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name

    def __str__(self):
        return f'Course ID: {self.id}, Course Name: {self.name}'


class Menu:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        num_students = int(input('Enter the number of students: '))
        for _ in range(num_students):
            student_id = input('Enter student ID: ')
            name = input('Enter student name: ')
            dob_str = input('Enter student date of birth (YYYY-MM-DD): ')
            try:
                dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
            except ValueError:
                print('Invalid date format. Please use YYYY-MM-DD.')
                continue
            student = Student(student_id, name, dob)
            self.students.append(student)

    def input_courses(self):
        num_courses = int(input('Enter the number of courses: '))
        for _ in range(num_courses):
            course_id = input('Enter course ID: ')
            course_name = input('Enter course name: ')
            self.courses.append(Course(course_id, course_name))

    def input_marks(self):
        student_id = input('Enter student ID: ')
        course_id = input('Enter course ID: ')
        try:
            mark = float(input('Enter the mark for the student in this course (1-20): '))
            credits = float(input('Enter the credits for this course: '))
        except ValueError:
            print('Invalid input format. Please enter valid numbers.')
            return

        student = next((s for s in self.students if s.id == student_id), None)
        course = next((c for c in self.courses if c.id == course_id), None)

        if student and course:
            student.add_mark(course_id, mark, credits)
            print('Mark added successfully.')
        else:
            print('Student or course not found.')

    def list_courses(self):
        print('\nList of Courses:')
        for course in self.courses:
            print(course)

    def list_students(self):
        print('\nList of Students:')
        for student in self.students:
            print(student)

    def show_marks(self):
        course_id = input('Enter course ID: ')
        course = next((c for c in self.courses if c.id == course_id), None)

        if course:
            print(f'\nMarks for Course ID {course_id} - {course.name}:')
            for student in self.students:
                if course_id in student.marks:
                    mark_info = student.marks[course_id]
                    print(f'{student}, Mark: {mark_info["mark"]}, Credits: {mark_info["credits"]}')
            else:
                print('No marks found for the given course.')
        else:
            print('Course not found.')

    def run(self):
        self.input_students()
        self.input_courses()

        while True:
            print('\nOptions:')
            print('1. Input student marks')
            print('2. List courses')
            print('3. List students')
            print('4. Show student marks')
            print('5. Quit')

            choice = input('Enter your choice (1-5): ')

            if choice == '1':
                self.input_marks()
            elif choice == '2':
                self.list_courses()
            elif choice == '3':
                self.list_students()
            elif choice == '4':
                self.show_marks()
            elif choice == '5':
                print('Exiting program.')
                break
            else:
                print('Invalid choice. Please enter a number between 1 and 5.')


if __name__ == '__main__':
    menu = Menu()
    menu.run()
