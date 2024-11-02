#defining an method to divide list of numbers
def divide_list(numbers):
    #creating two empty lists
    even_list = []
    odd_list = []
    # iterating each number in list
    for num in numbers:
        #checking conidition even or not
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    return even_list, odd_list


# defining an main function
def main():
    # list of numbers
    numbers = [1,2,3,4,5,6,7,12]
    # calling the function
    even_list, odd_list = divide_list(numbers)
    # printing the output
    print("Even numbers List: ",even_list)
    print("Odd Numbers List: ",odd_list)

#entry point we are defining
if __name__ == "__main__":
    main()