# Write code for Login 
# Login (Request)
#   Username
#       Validation : Username must have @ Symbol
#   Password
#       Validation - Min Length should be 10 
# Login (Reponse)
#   200 - UserLogin is Succesful 
#   401 - Un Authorized
#   400 - Something Went Wrong
#   404 - Page Not Found
#   500 - Internal Server Error
def user_Validation(username,password):
    
    if len(username)>6 and '#' in password:
        if len(password)>6:
            if username=="Gowri Ganesh" and password=="Gowri123#":
                print(f"Login Successful {username}")
            else:
                print("Invalid Username or Password")
        else:
            print(" Password must be greater than 6 Charcters")
    else:
        print("Username must be greater than 6 Cha")
    
    
def user_input():
    username=input("Enter the username :")
    password=input("Enter the password :")
    response=user_Validation(username,password)
    return response

   
def main():
    user_input()
if __name__=="__main__":
    main()
