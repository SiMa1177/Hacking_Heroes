def multiply_elements_in_list(elements):
    """
    Multiplies all elements in the given list and returns the product.
    
    Args:
        elements (list): A list of integers.
    
    Returns:
        int: The product of all elements in the list.
    """
    product = 1
    for element in elements:
        product *= element
    return product

def get_user_elements():
    """
    Prompts the user to input elements and returns them as a list of integers.
    
    Returns:
        list: A list of integers entered by the user.
    """
    elements = []
    print("Enter elements one by one (type 'done' to finish):")
    
    while True:
        user_input = input("Enter a number: ")
        if user_input.lower() == 'done':
            break
        try:
            number = int(user_input)
            elements.append(number)
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    return elements

def main():
    """
    Main function to execute the script.
    """
    # Print user information
    user_name = "Sakalya Mitra"
    user_id = "20MIM10056"
    print(f"{user_name}:{user_id}")
    print("\n")
    
    # Get elements from the user
    elements = get_user_elements()
    
    # Calculate the product of elements in the list
    if elements:
        product = multiply_elements_in_list(elements)
        # Print the result
        print("Multiplication of elements in the list:", product)
    else:
        print("No elements to multiply.")

if __name__ == "__main__":
    main()
