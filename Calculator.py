# Define class to import later

class Calculator:
    def calculate(operation, num1, num2=None):
        try:
            # Addition
            if operation == '+':
                result = num1 + num2
            # Subtraction
            elif operation == '-':
                result = num1 - num2
            # Multiplication
            elif operation == '*':
                result = num1 * num2
            # Division
            elif operation == '/':
                result = num1 / num2
#Handle exceptions
            else:
                raise ValueError("Invalid operation selected.")
            
            return result
        
        except ValueError as error:
            raise ValueError("Error: " + str(error))
        
        except ZeroDivisionError as error:
            raise ZeroDivisionError("Error: Cannot be divided by zero.")