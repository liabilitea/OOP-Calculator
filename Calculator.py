# Define class to import later

class Calculator:
    def calculate(operation, num1, num2):
        try:
            # Addition
            if operation == '+':
                result = num1 + num2
            # Subtraction
            elif operation == '-':
                result = num1 - num2
            # Multiplication
            elif operation == '*':
                result == num1 * num2
            # Division
            elif operation == '/':
                result = num1 / num2
#Handle exceptions
            else:
            