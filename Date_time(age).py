#write an class
#define an method for printing dateofbirth
#print that by using decoratores.
from datetime import datetime
class Date:
    def __init__(self,name,dob):
        self.name=name
        self._dob=datetime.strptime(dob,'%Y-%m-%d')
    
    @property
    def age(self):
        """calculating age based on DOB"""
        today=datetime.today()
        age=today.year-self._dob.year
        if (today.month,today.day)<(self._dob.month,self._dob.day):
            age=-1
        return age
    @property
    def can_vote(self):
        """checking if person can vote or not"""
        if self.age>=18:
            return True
        else:
            return False
    
    def check_age(self):
        """By using can_vote function printing eligible or not"""
        if self.can_vote:
            print(f"You can able to Vote and your age is {self.age}")
        else:
            print(f"Your age should be atleast 18 years")

    
def main():
    name=input("Enter Name:")
    dob=input("Enter DOB(YYYY-MM-DD):")
    date=Date(name,dob)
    print(f"{date.name} is {date.age } years")
    date.check_age()

if __name__=="__main__":
    main()
    