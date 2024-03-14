class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name

    def __str__(self):
        return f'Course ID: {self.id}, Course Name: {self.name}'
