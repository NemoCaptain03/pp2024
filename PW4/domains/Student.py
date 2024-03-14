class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_mark(self, course_id, mark, credits):
        self.marks[course_id] = {'mark': mark, 'credits': credits}

    def calculate_gpa(self):
        if not self.marks:
            return 0

        total_credits = sum(mark_info['credits'] for mark_info in self.marks.values())
        weighted_sum = sum(mark_info['mark'] * mark_info['credits'] for mark_info in self.marks.values())

        return weighted_sum / total_credits

    def __str__(self):
        return f'Student ID: {self.id}, Student Name: {self.name}, GPA: {self.calculate_gpa():.1f}'
