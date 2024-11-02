
#1. Apply the Exception Handling in  Voter Class 
#Age  = 10  ->  Minor 
#Age ?=18 -> You Can Voter
#Age = -1 -> Age should be Positive number
#Age = "" -> Age should not be blank 

def main():
    age=int(input("enter the age"))
    try:
        if age<10:
            raise ValueError("age should be positive number")
        elif age<18:
            raise ValueError("you are a minor")
        elif age>=18:
            print("you can voter")
    except ValueError as e:
        print(e)
    finally:
        print("end of program")

    try:
        age =input("Enter the age")
        if not age:
            raise ValueError("age should be blank")
        age = int(age)
        int(age)
    except ValueError as e:
        print("a should be number")


    
if __name__=="__main__":
    main()



    





        

