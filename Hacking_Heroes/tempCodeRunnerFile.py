import json

class Person:
    """A class to represent a person with a name, age, and optional attributes."""

    def __init__(self, name: str, age: int, gender: str = None, occupation: str = None):
        """Initialize a Person instance with a name, age, and optional attributes.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            gender (str, optional): The gender of the person. Defaults to None.
            occupation (str, optional): The occupation of the person. Defaults to None.

        Raises:
            ValueError: If age is not a non-negative integer.
        """
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a non-negative integer.")
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation

    def greet(self) -> str:
        """Return a greeting message."""
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def birthday(self) -> None:
        """Increment the person's age by one year."""
        self.age += 1

    def to_json(self) -> str:
        """Serialize the person to a JSON format."""
        return json.dumps(self.__dict__)

    def __str__(self) -> str:
        """Return a string representation of the person."""
        details = f"Person(Name: {self.name}, Age: {self.age}"
        if self.gender:
            details += f", Gender: {self.gender}"
        if self.occupation:
            details += f", Occupation: {self.occupation}"
        details += ")"
        return details


def main():
    """Main function to demonstrate the Person class functionality."""
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        gender = input("Enter your gender (optional): ") or None
        occupation = input("Enter your occupation (optional): ") or None
        
        person = Person(name, age, gender, occupation)
        print(person.greet())
        
        # Simulate a birthday
        person.birthday()
        print(f"After birthday: {person}")
        print(f"JSON representation: {person.to_json()}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
