class Student:
    _ids = set()

    def __init__(self, student_id, name, surname):
        if student_id in Student._ids:
            raise ValueError("ID must be unique")
        self.student_id = student_id
        self.name = name
        self.surname = surname
        Student._ids.add(student_id)

    def __str__(self):
        return f"{self.name} {self.surname} (ID: {self.student_id})"


class Exam:
    def __init__(self):
        self.marks = {}

    def add_marks(self, student, marks):
        if not isinstance(student, Student):
            raise ValueError("Invalid student object")
        if not (0 <= marks <= 100):
            raise ValueError("Marks must be between 0 and 100")
        self.marks[student.student_id] = marks

    def get_results(self, student):
        if student.student_id not in self.marks:
            return f"No marks available for {student.name} {student.surname}"

        marks = self.marks[student.student_id]

        if 85 <= marks <= 100:
            return f"{student.name} {student.surname} passed with excellent marks"
        elif 75 <= marks < 85:
            return f"{student.name} {student.surname} passed with distinction"
        elif 35 <= marks < 75:
            return f"{student.name} {student.surname} passed"
        else:
            return f"{student.name} {student.surname} failed"


student1 = Student(1, "Ameet", "Parse")
student2 = Student(2, "Ishaan", "Parse")

exam = Exam()
exam.add_marks(student1, 65)
exam.add_marks(student2, 95)

print(exam.get_results(student1))  
print(exam.get_results(student2)) 