def main():
    employee_collection=["Gowri","Ganesh","Surendhra","Pavan"]
    print("Displaying the employees list")
    for employee in employee_collection:
        print(employee)
    #now displaying with employees count
    print("\n Displaying with index numbers:")
    for index,employee in enumerate(employee_collection):
        print(f"S.NO {index+1} Employee_Name: {employee}")
    #Adding employee name into existing list
    employee_collection.append("Suresh")
    print("\n Displaying the employees list after adding new employee")
    for employee in employee_collection:
        print(employee)
    employee_collection.remove('Suresh')
    print("\n Displaying the employees list after removing employee")
    print(employee_collection)
    department_collection=['Testing','Developing','Supply Chain Mangement','Cloud']
    print("\n Displaying the departements list:")
    for department in department_collection:
        print(f'Department Name:{department}')
    #Adding department name into existing list
    department_collection.append('HR')
    for index,department in enumerate(department_collection):
        print(f"S.no {index+1} department_name {department}")
    

if __name__=="__main__":
    main()