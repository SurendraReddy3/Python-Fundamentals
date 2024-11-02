# Purpose - Differenciate Between Variable and Property 
# Variable ----> Assign the Value -----> No Validation
# Property ----> Set the Value --> Receive the Value --> Validate ---> Assign |||||||| Retrieve -> Get
class Person:

    @property # Declare a property with name as "age"
    def age(self): # GET - Assigned value from Setter will be returned
        print("Getter")
        return self._age

    @age.setter # SET
    def age(self, value):
        if value <=0:
            print("age if")
            self._age = 0
        else:
            print("else")
            self._age = value


def main():
    person = Person()
    person.age = 10
    print("Hi")
    if person.age <=0:
        print ("Age should be > 0")
    else: 
        print(person.age)


if __name__ == '__main__':
    main()
