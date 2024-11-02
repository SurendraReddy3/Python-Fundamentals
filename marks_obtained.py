# Student
#     first_name
#     last_name
#     marks_obtained 

# Exam 
#     check if the Student is Passed
#         if Passed and marks_obtained > 75 and less than 80 -> Print ("First-name passed with distinction)
#         if Passed and marks_obtained > 80 and less than 100 -> Print ("First-name passed with Top Rank)
#         if Passed and marks_obtained < 75 and > than 35 -> Print ("First-name passed with avg marks)
#         if Passed and marks_obtained < 35  -> Print ("First-name failed).

# Here if we use try catch block their is only one logic is coming for try block .If the marks <0 and >100 case only we are encountring.

class Student:
    def __init__(self,fname,lname,marks):
        self.first_name=fname
        self.last_name=lname
        self.marks_obtained=marks
    def check_pass_marks(self):
        try:
            if self.marks_obtained<0 or self.marks_obtained>100:
                raise ValueError("Please enter an value between 0-100")
            elif self.marks_obtained>35 and self.marks_obtained<=100:
                return True
            else:
                return False
        except ValueError as ve:
            print(ve)

    def evaluate_performance(self):
        if self.check_pass_marks():
            if self.marks_obtained>75 and self.marks_obtained<80:
                print(f"{self.first_name} passed with distinction")
            elif self.marks_obtained>80 and self.marks_obtained<100:
                print(f"{self.first_name} passed with top rank")
            elif self.marks_obtained>35 and self.marks_obtained<75:
                print(f"{self.first_name} passed with avg marks")
        else:
            print(f"{self.first_name} failed")


def main():
    try:
        fname=input("Enter your First name: ")
        lname=input("Enter your Last name: ")
        marks=int(input("Enter your marks: "))
        student=Student(fname,lname,marks)
        student.evaluate_performance()
    except ValueError as ve:
        print(ve)

if __name__=="__main__":
    main()
            

        
        