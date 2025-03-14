import unittest
from unittest.mock import Mock

def function_without_return(data: list, item):
    """Appends an item to a list."""
    data.append(item)

def function_that_calls_external_service(service, message):
    """Sends a message using an external service."""
    service.send(message)

def function_that_raises_exception(value):
    """Raises an exception if the value is negative."""
    if value < 0:
        raise ValueError("Value cannot be negative")

class TestFunctionsWithoutReturn(unittest.TestCase):
    def test_function_without_return(self):
        data = []
        function_without_return(data, 1)
        self.assertEqual(data, [1])

    def test_function_that_calls_external_service(self):
        mock_service = Mock()
        function_that_calls_external_service(mock_service, "hello")
        mock_service.send.assert_called_once_with("hello")

    def test_function_that_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            function_that_raises_exception(-1)
        self.assertEqual(str(context.exception), "Value cannot be negative")

if __name__ == '__main__':
    unittest.main()