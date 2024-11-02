# problem statement 

#1 create emplo class with first name , lastname, fullname, emploid.
#2 emplo id should be unique 
#3  create salary with methods pay salary , get salary result
#4 10000 and 20000 
#5 check employe id in the list we need to pay the salary to the empolye 
#6 pass result to get salary method e
# print all empolyee conditional statement


class Employee:
    employee_id = set()
    def __init__(self, fname, lname, employee_id,tax_percentage):
        if employee_id in Employee.employee_id:
            raise ValueError("ID must be unique")
        
        self.first_name = fname
        self.last_name = lname
        self.emp_id = employee_id
        self.tax_percentage=tax_percentage
        Employee.employee_id.add(employee_id)
        
    def __str__(self):
        return f"{self.first_name} {self.last_name} (ID:{self.emp_id} )"

class Salary:
    def __init__(self):
        self.salary = {}
    def pay_salary(self, emp, amount):
        if not isinstance(emp, Employee):
            raise ValueError("Invalid employee object")
        if (amount <= 10000 or amount >= 100000):
            raise ValueError("Salary must be between 10,000 or 1,00,000")
        
        self.salary[emp.emp_id] = amount  

    def get_salary_result(self, emp):
        if emp.emp_id in self.salary:
            if (80000 <= self.salary[emp.emp_id] <= 100000):
                return f"the salary of {emp} is {self.salary[emp.emp_id]} and is an Extraordinary Employee"
            elif (60000 <= self.salary[emp.emp_id] < 80000):
                return f"the salary of {emp} is {self.salary[emp.emp_id]} and is an Good employee"
            elif (30000 <= self.salary[emp.emp_id] < 60000):
                return f"the salary of {emp} is {self.salary[emp.emp_id]} and is an Average employee"
            else:
                return f"Please improve your performance to get more salary"
        else:
            return f" No salary available for the {emp} ID"

def main():
    emply1 = Employee("Gowri", "Ganesh", 1,10)
    emply2 = Employee("pavan", "Kumar", 2,30)
    salary = Salary()
    salary.pay_salary(emply1, 51000)
    salary.pay_salary(emply2, 80000)
    print(salary.get_salary_result(emply1))
    print(salary.get_salary_result(emply2))

if __name__ == "__main__":
    main()