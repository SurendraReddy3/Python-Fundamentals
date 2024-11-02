def main():
    print ("3. Main is called")
    print ("4. Welcome to Tech Job Solutions")
    first_number = int(input("Enter the first number"))
    second_number = int(input("Enter the second number"))
    
    add_two_numbers(first_number, second_number)



def add_two_numbers(first_number, second_number):
    print (f"Value of First Numbner is {first_number}")
    print (f"Value of Second Numbner is {second_number}")
    print (first_number + second_number)
    print (f"addation of two numbers i.e. first number {first_number} and second number {second_number} is {first_number + second_number}")
    # Addation of two Numbers is 30


def for_loop_example():
    numbers = [1, 2, 3, 4, 5]    
    print("For loop example:")
    for number in numbers:
        print(f"Numbers in the list are one by one: {number}")


def for_loop_example_with_employee():
    employees = ["Ameet", "Ishaan", "Shyam", "John"]    
    print("For loop example:")
    for employee in employees:
        print(f"Your employee is : {employee}")

def while_example():
    print("\nWhile loop example:")
    
    # while <<Condition>>==True:
    #     Loop`
    # Else 
    # Go away

    count = 0
    while count < 5:
        print(f"Count is : {count}")
        count += 1



if __name__ == "__main__":
    print ("1. Entry Point Detected.........")
    print ("2. About to Call Main")
    main()
    #for_loop_example()
    #for_loop_example_with_employee()
    while_example()
    print ("5. Program will close now")