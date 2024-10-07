def find_max_element(numbers):
    """
    Function to find the maximum element in a list.
    
    Args:
    numbers (list): List of numbers.
    
    Returns:
    int or None: The maximum element in the list, or None if the list is empty.
    """
    if not numbers:
        return None  # Handle empty list

    # Initialize max_element with the first element of the list
    max_element = numbers[0]

    # Iterate through the list to find the maximum element
    for num in numbers:
        if num > max_element:
            max_element = num

    return max_element


def get_list_from_user():
    """
    Function to get a list of numbers from the user.
    
    Returns:
    list: List of numbers entered by the user.
    """
    numbers = []
    while True:
        user_input = input("Enter a number (or type 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return numbers


def main():
    print("Program to find the maximum element in a list\n")

    # Get the list of numbers from the user
    user_list = get_list_from_user()

    # Check if the list is empty and handle accordingly
    if not user_list:
        print("The list is empty. No maximum element to find.")
        return

    # Find the maximum element in the list
    max_element = find_max_element(user_list)

    # Print the maximum element found in the list
    print("Maximum element in the list:", max_element)


if __name__ == "__main__":
    main()

