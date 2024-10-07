import unittest
from tempCodeRunnerFile import Person  # Updated import statement
from unittest.mock import patch

class TestPerson(unittest.TestCase):
    """Unit tests for the Person class."""

    def setUp(self):
        """Create an instance of Person before each test."""
        self.person = Person("John Doe", 30)

    def test_greet(self):
        """Test the greet functionality."""
        self.assertEqual(self.person.greet(), "Hello, my name is John Doe and I am 30 years old.")

    def test_birthday(self):
        """Test the birthday functionality."""
        self.person.birthday()
        self.assertEqual(self.person.age, 31)

    def test_age_validation(self):
        """Test age validation for invalid ages."""
        with self.assertRaises(ValueError):
            Person("Jane Doe", -1)

    def test_to_json(self):
        """Test JSON serialization."""
        expected_json = '{"name": "John Doe", "age": 30, "gender": null, "occupation": null}'
        self.assertEqual(self.person.to_json(), expected_json)

    @patch('tempCodeRunnerFile.Person.greet')  # Mocking the greet method
    def test_greet_mocked(self, mock_greet):
        """Test greet method with mocking."""
        mock_greet.return_value = "Mocked Greeting"
        self.assertEqual(self.person.greet(), "Mocked Greeting")

if __name__ == "__main__":
    unittest.main()
