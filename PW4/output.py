def list_courses(courses):
    print('\nList of Courses:')
    for course in courses:
        print(f'Course ID: {course["id"]}, Course Name: {course["name"]}')


def list_students(students):
    print('\nList of Students:')
    for student in students:
        print(f'Student ID: {student["id"]}, Student Name: {student["name"]}, Date of Birth: {student["dob"]}')


def show_marks(marks):
    if not marks:
        print('No marks found for the given course.')
        return
    course_id = marks[0]['course_id']
    print(f'\nMarks for Course ID {course_id}:')
    for mark in marks:
        print(f'Student ID: {mark["student_id"]}, Mark: {mark["mark"]}, Credits: {mark["credits"]}')
