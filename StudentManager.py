class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, dob, gender, address):
        """Add a new student to the list."""
        student = {
            'name': name,
            'age': age,
            'dob': dob,
            'gender': gender,
            'address': address
        }
        self.students.append(student)

    def get_student(self, name):
        """Retrieve a student's information by name."""
        for student in self.students:
            if student['name'] == name:
                return student
        return None  # Return None if no student found

    def get_all_students(self):
        """Retrieve all students' information."""
        return self.students

# Example usage:
manager = StudentManager()
manager.add_student(name="Ameet Parse", age=47, dob="03/03/1976", gender= "Male", address="HYD")
manager.add_student('Ishaan Parse', 22, '1997-05-12', 'Female', '5678 Oak St')

print(manager.get_student('Parse'))  # Retrieve specific student
#print(manager.get_all_students())       # Retrieve all students
