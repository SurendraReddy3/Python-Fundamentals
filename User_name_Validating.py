class User:
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if type(value)==str and len(value)>=3 and len(value)<=10:
            print(f"Valid user Name: {value}")
        else:
            print("Invalid user name")
def main():
    user=User()
    user.name=input("Enter user name: ")
    
if __name__=="__main__":
    main()