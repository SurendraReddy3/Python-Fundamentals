
def main():
    #my_string = "This is a India, and I am in Hyderabad" # string
    #print (my_string)
    #print (repr(my_string))


    #print ("I am working on Find methond of String Class")

    #location = my_string.find("This")
    #print (location)


    # 1 = 0
    # , = 1
    # 2 = 2
    # , = 3
    # 3 = 4
    # numbers = "1,2,3,4,5"
    # print (numbers.find("3"))


    # A <> a
    # A = A
    my_string = "A,B,C,D,E" 
    print (my_string.find ("a"))



def find_word():  
    # Ask user to enter a Statement
    # Assign to the Variable user_string  
    user_string = input ("Please enter a Statment....")
    
    # print the value of variable user_string
    #print (user_string)

    user_word = input ("Enter word or charactor to find.....")
    result = user_string.find (user_word)

    if result == -1 :
        print ("Word that you mentioned does not exists in the string")
    elif result >=0 :
        print (f"Word that you entered is at postion {result} ")
    

if __name__ == "__main__":
    find_word()