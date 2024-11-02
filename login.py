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


def login():
    username = input ("Enter username : ")
    password  = input("Enter Password : ")

    if username == "Ameet" and password == "Parse":
        print ("User name and password is correct")
    else:
        print ("Either username or password is incorrect")


def user_login(username, password):
    if username == "Ameet" and password == "Parse":
        return 200
    else:
        return 401

def process_user_login():
    username = input ("Enter username : ")
    password  = input("Enter Password : ")
    login_response = user_login (username, password)
    if login_response == 200:
        print (f"{username} User is Logged in and Login Status is {login_response}")
    elif login_response == 401:
        print (f"{username} User is not Logged in and  Status is {login_response}")
    else:
        print ("Something Went Wrong......... Please try again later")

def main():    
    #process_user_login()
    #length = len("Ameet Parse")
    #print(length)
    username = input("Enter Your Email Address : ")
    if "@tjs.com" in username:
        print ("Email Address seems to be correct")
    else:
        print ("Enter correct emnail address")

if __name__ == "__main__":
    main()