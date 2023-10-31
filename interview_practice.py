# Problem 1
#   Prompt the user for a list of numbers separated by commas. 
#   Create an algorithm that prints the amount of the given integers that are divisible by 3.
#   Example case: “4,12, 14, 6, 9, 22”

#numbers = input("Enter a list of numbers separated by commas: ")

# Define function to find numbers that are divisible by 3 and return the number of qualifying values. 
def divide(numbers):

    # result is the number of values found where num % 3 == 0.
    result = 0

    # Split string by commas and iterate through each number.
    for num in numbers.split(","):

        # Convert num to an int and check to see if divisible by 3.
        if int(num) % 3 == 0:

            # If valid, add 1 to result count.
            result += 1
    print(result)

# Test case where the given string of numbers should return 3. 
numbers = "4,12,14,6,9,22"

divide(numbers)

# Test case where the given string of numbers should return 4.
numbers = "15,12,14,6,9,22"

divide(numbers)

# Test case where the given string of numbers should return 1.
numbers = "1,-2,9"

divide(numbers)