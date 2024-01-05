from datetime import datetime


def input_students_number():
    return int(input('Enter the number of students: '))


def input_student_info():
    student_id = input('Enter student ID: ')
    name = input('Enter student name: ')

    while True:
        dob_str = input('Enter student date of birth (YYYY-MM-DD): ')

        try:
            dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
            break
        except ValueError:
            print('Invalid date format. Please use YYYY-MM-DD.')

    return {'id': student_id, 'name': name, 'dob': dob, 'marks': {}}


def input_courses_number():
    return int(input('Enter the number of courses: '))


def input_course_info():
    course_id = input('Enter course ID: ')
    course_name = input('Enter course name: ')
    return {'id': course_id, 'name': course_name}


def input_marks(students, courses):
    student_id = input('Enter student ID: ')
    course_id = input('Enter course ID: ')
    try:
        mark = float(input('Enter the mark for the student in this course (1-20): '))
    except ValueError:
        print('Invalid mark format. Please enter a number.')
        return input_marks(students, courses)

    if 1 <= mark <= 20:
        student = next((student for student in students if student['id'] == student_id), None)
        course = next((course for course in courses if course['id'] == course_id), None)

        if student and course:
            student['marks'][course_id] = mark
            print('Mark added successfully.')
        else:
            print('Student or course not found.')
    else:
        print('Invalid mark. Please enter a mark between 1 and 20.')


def list_courses(courses):
    print('\nList of Courses:')
    for course in courses:
        print(f'Course ID: {course['id']}, Course Name: {course['name']}')


def list_students(students):
    print('\nList of Students:')
    for student in students:
        print(f'Student ID: {student['id']}, Student Name: {student['name']}')


def show_marks(students, courses):
    course_id = input('Enter course ID: ')

    course = next((c for c in courses if c['id'] == course_id), None)

    if course:
        print(f'\nMarks for Course ID {course_id} - {course['name']}:')
        for student in students:
            if 'marks' in student and course_id in student['marks']:
                print(f'Student ID: {student['id']}, Student Name: {student['name']},'
                      f'Mark: {student['marks'][course_id]}')
        else:
            print('No marks found for the given course.')
    else:
        print('Course not found.')


def main():
    students = []
    courses = []

    num_students = input_students_number()
    for _ in range(num_students):
        students.append(input_student_info())

    num_courses = input_courses_number()
    for _ in range(num_courses):
        courses.append(input_course_info())

    while True:
        print('\nOptions:')
        print('1. Input student marks')
        print('2. List courses')
        print('3. List students')
        print('4. Show student marks')
        print('5. Quit')

        choice = input('Enter your choice (1-5): ')

        if choice == '1':
            input_marks(students, courses)
        elif choice == '2':
            list_courses(courses)
        elif choice == '3':
            list_students(students)
        elif choice == '4':
            show_marks(students, courses)
        elif choice == '5':
            print('Exiting program.')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 5.')


if __name__ == '__main__':
    main()
