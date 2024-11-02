# Problem Statement - Find out Even or Odd
# - Input -> Hard coded Input or Ask User?


# find_even_odd_numbers
# Check if the Numbeer is Even or Odd, which is passed as parameter i.e. numbers
def find_even_odd_numbers(numbers):
    even_numbers = []
    odd_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    return even_numbers, odd_numbers

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even, odd = find_even_odd_numbers(numbers)

print("Even numbers:", even)
print("Odd numbers:", odd)


def show_tuple_example():
    return "A", "B", "C", "D"

x,y,z,q = show_tuple_example()
print (x,y,z,q)