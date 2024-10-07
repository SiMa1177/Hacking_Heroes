def find_minimum_element(numbers):
    """Finds the minimum element in a list of numbers.

    Args:
        numbers (list): A list of numerical values.

    Returns:
        int or float: The minimum value in the list.
    """
    if not numbers:
        raise ValueError("The list is empty. Please provide a list with at least one element.")
    
    min_element = numbers[0]  # Assume the first element is the minimum
    for number in numbers:
        if number < min_element:
            min_element = number  # Update min_element if a smaller number is found

    return min_element


def main():
    """Main function to execute the program."""
    print("Welcome to the Minimum Element Finder!")
    
    number_list = []  # Initialize an empty list to hold numbers

    # Input loop for adding elements
    while True:
        try:
            user_input = input("Enter a number (or type 'done' to finish): ")
            if user_input.lower() == 'done':
                break  # Exit loop if the user types 'done'
            number_list.append(float(user_input))  # Add the number to the list
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    try:
        min_value = find_minimum_element(number_list)
        print("The minimum element in the list is:", min_value)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
