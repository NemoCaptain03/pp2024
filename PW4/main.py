from input import input_students, input_courses, input_marks
from output import list_courses, list_students, show_marks


class Menu:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def run(self):
        self.students = input_students()
        self.courses = input_courses()

        while True:
            print('\nOptions:')
            print('1. Input student marks')
            print('2. List courses')
            print('3. List students')
            print('4. Show student marks')
            print('5. Quit')

            choice = input('Enter your choice (1-5): ')

            if choice == '1':
                mark = input_marks()
                student_id = mark['student_id']
                course_id = mark['course_id']
                student = next((s for s in self.students if s['id'] == student_id), None)
                course = next((c for c in self.courses if c['id'] == course_id), None)
                if student and course:
                    mark_info = {'student_id': student_id, 'course_id': course_id, 'mark': mark['mark'], 'credits': mark['credits']}
                    self.marks.append(mark_info)
                    print('Mark added successfully.')
                else:
                    print('Student or course not found.')
            elif choice == '2':
                list_courses(self.courses)
            elif choice == '3':
                list_students(self.students)
            elif choice == '4':
                show_marks(self.marks)
            elif choice == '5':
                print('Exiting program.')
                break
            else:
                print('Invalid choice. Please enter a number between 1 and 5.')


if __name__ == '__main__':
    menu = Menu()
    menu.run()
