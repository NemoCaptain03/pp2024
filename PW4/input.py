from datetime import datetime


def input_students():
    num_students = int(input('Enter the number of students: '))
    students = []
    for _ in range(num_students):
        student_id = input('Enter student ID: ')
        name = input('Enter student name: ')
        dob_str = input('Enter student date of birth (YYYY-MM-DD): ')
        try:
            dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
        except ValueError:
            print('Invalid date format. Please use YYYY-MM-DD.')
            continue
        students.append({'id': student_id, 'name': name, 'dob': dob})
    return students


def input_courses():
    num_courses = int(input('Enter the number of courses: '))
    courses = []
    for _ in range(num_courses):
        course_id = input('Enter course ID: ')
        course_name = input('Enter course name: ')
        courses.append({'id': course_id, 'name': course_name})
    return courses


def input_marks():
    student_id = input('Enter student ID: ')
    course_id = input('Enter course ID: ')
    try:
        mark = float(input('Enter the mark for the student in this course (1-20): '))
        credits = float(input('Enter the credits for this course: '))
    except ValueError:
        print('Invalid input format. Please enter valid numbers.')
        return

    return {'student_id': student_id, 'course_id': course_id, 'mark': mark, 'credits': credits}
