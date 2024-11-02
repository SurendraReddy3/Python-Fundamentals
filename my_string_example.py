# Problem Statement 
# 1. Ask User to Enter a String
# 2. Ask user to enter a word 
# 3. Check if word is present in the string


def process_user_input (user_string, word_to_find):
    result = user_string.find (word_to_find)
    return result


def main():
    first_string = "This is India"
    # This
    # is
    # India
    result = first_string.split()
    print (result)

# def main():
#     user_string = input("Please enter the text to conver to CAPITOL CASE:")
#     print (user_string.upper()) 
#     result  = user_string.lower()
#     print (result)

# def main():
#     user_string = input("Please enter a sentense / statement:")
#     result = user_string.count("is")
#     print (result)

# Welcome to the Tech Job Solutions
# Replace Tech by TCS
# Welcome to the TCS Job Solutions
# def main():    
#     user_string = input("Please enter a sentense / statement:")
#     string_to_replace = input ("Enter string to replace:")
#     replace_by = input ("Enter replacement word :")
#     result = user_string.replace (string_to_replace, replace_by)
#     print (result)


# def main():
#     user_string = input("Please enter a sentense / statement:")
#     word_to_find = input ("Please enter word to find in the sentense / statement:")
#     final_result = process_user_input (user_string, word_to_find)

#     if final_result == -1:
#         print (f"{user_string} does not contain word {word_to_find}")
#     else:
#         print (f"{user_string} contains word {word_to_find} at location or index at {final_result}")



# def main():
#     user_string = input ("Please enter a sentense / statement:")
#     word_to_find = input ("Please enter word to find in the sentense / statement:")    
#     result = user_string.find (word_to_find)
    
#     if result == -1:
#         print (f"{user_string} does not contain word {word_to_find}")
#     else:
#         print (f"{user_string} contains word {word_to_find} at location or index at {result}")
        



if __name__ == "__main__":
    main()
