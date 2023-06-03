# Import necessary modules
import math
from Calculator import Calculator

# Create new class 
class ScientificCalculator(Calculator):
    # Create method to calculate using exponent operation
    def power(self, num1, num2):
        return num1 ** num2
    
    # Create method t calculate using log operation
    def log(self, num1):
        return self.logbase(num1)
    # Use base 10 for log
    def logbase(self, num, base=10):
        return math.log(num, base)
    
# Perform other calculations using the parent class
    def calculate(operation, num1, num2=None):
        if operation == '^':
            return self.power(num1, num2)
        else:
            return super().calculate(num1, num2)