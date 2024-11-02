# Example 1

# 1. Apply the Exception Handling in  Voter Class
# Age  = 10  ->  Minor
# Age >=18 -> You Can Vote
# Age = -1 -> Age should be a positive number
# Age = "" -> Age should not be blank

class Voter:
    def __init__(self, age):
        self.age = age
    def can_Vote(self):
        try: #defining an try block to vadliate an Voter age
            if self.age < 0:
                raise ValueError("Age should be a positive number")
            elif self.age < 18:
                raise ValueError("You are a minor")
            elif self.age >= 18:
                print("You can vote")
            elif not self.age:
                raise ValueError("Age should not be blank")
        except ValueError as e: # it is also an catch block it will catch if any exception will occur 
            print(e)
        finally:
            print("End of Program")
    
        

def main():
    try:
        age = int(input("Enter the age: "))
        voter=Voter(age)
        voter.can_Vote()
    except ValueError:
        print("Age should be an number")

if __name__=="__main__":
   main()
