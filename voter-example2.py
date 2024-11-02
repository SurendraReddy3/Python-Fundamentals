# Write Code for Voter Class. With Below Features
# Class Name - Voter -------
# self, name, address, gender, dob ------
# Properties - can_Vote, age --> Read Only 
# Method - Vote()
#     if Age > = 18 As on Current Date -> Todays Date -> Tomorrow -> Tomorrows Date
#         print ("Ameet You have Voted.... Congratulatios")
#     else
#     print ("Ameet you need to be atleast 18 as on 20-07-2024


from datetime import datetime

class Voter:
    def __init__(self, name, address, gender, dob):
        self.name = name
        self.address = address
        self.gender = gender
        self._dob = datetime.strptime(dob, '%Y-%m-%d') # Format Date Time -> mm-dd-yyyy, dd-mm-yyyy, 3rd Jan, 2024  

    @property
    def age(self):
        """Calculate age based on Date of Birth."""
        today = datetime.now() # 20-07-2024
        age = today.year - self._dob.year # 2024 - 2021 = 03 Years
        #   07, 20 < 04 < 15
        if (today.month, today.day) < (self._dob.month, self._dob.day):
            age -= 1
        return age

    @property
    def can_vote(self):
        """Check if the voter can vote based on their age."""
        
        if self.age >=18 : 
            return True
        else:
            return False 
        
        # return self.age >= 18

    def vote(self):
        """Allow the voter to vote if they are eligible."""
        if self.can_vote:
            print(f"{self.name} has successfully voted!")
        else:
            print("Cannot vote. Need to be at least 18 years old.")

    
    @property
    def status(self):
        return self._status

    @age.setter
    def status(self, value):
        self._status = value

# Example usage


def main(): # Calling the Voter Class or Main is the Caller. What is Read only Property. Whose value cannot be changed by Caller

    # Create the Instance of Voter Class i.e { Create Object}
    voter1 = Voter("Ameet Parse", "1234 Main St", "Male", "2000-04-15")
    print(f"{voter1.name}, Age: {voter1.age}, Can Vote: {voter1.can_vote}")
    voter1.vote()
    
    #voter1.age = 20
    #voter1.vote()
    #voter1.can_vote = True
    # voter1.status = "Has Already Voted"
    # print (voter1.status)




    # voter2 = Voter("Shubhangee Parse", "5678 Elm St", "Female", "2008-06-10")
    # print(f"{voter2.name}, Age: {voter2.age}, Can Vote: {voter2.can_vote}")
    # voter2.vote()

if __name__ == '__main__':
    main()
