class Voter:
    #initilzing age through default constructor.
    def __init__(self,age):
        print("1.Assiging age to age varbile in intilization method")
        self.age=age

    #defining an method for checking whether is eligible or not.if above 18 eligible he is.
    def check_age(self):
        if self.age<18:
            print("2.1 Executing if block")
            print("Your Not eligible")

        #else book if above 18 this block will execute
        else:
            print("2.2 Executing else block")
            print(f"You are eligble to vote{self.age}")
    
    def check_age1(self,age):
        if age <= 18:
            print("3.1 Executing if block")
            print("Your Not eligible")
        else:
            print(f"You are eligible to vote {age}")

#Taking age input from the user
age=int(input("Enter the age: "))
#creating an object for class
person_age=Voter(age)

#executng the age method.if you use print function you will get an additional ouput 
# "None " also will be printed.
person_age.check_age()

#executing the age1 method
person_age.check_age1(18)