def main():
    try: # Include Statements that we need to execute        
        print ("This is from Main - I am inside the Try Clause or Try Block")
        # print ("This is from Main Line 2")
        a = 10
        b = 0 
        c = a/b
        print (c)
    except: # Executed when there is any Exception in Try Block
        print ("There was some error, please try after some time")
    finally: # Called Everytime when there is Exception or No Exception
        print ("Program execution is completed")



if __name__ == "__main__":
    main()


# try:
#     # Attempt to convert an input to an integer
#     num = int(input("Enter a number: "))
#     print(f"The number is {num}")
# except ValueError:
#     # Handle the case where the input is not a valid integer
#     print("That's not a valid number!")
# finally:
#     # This code runs no matter what happens above
#     print("This will execute regardless of what happens above.")


