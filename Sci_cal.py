# Import necessary modules
import math
from Calculator import Calculator

# Create new class 
class ScientificCalculator(Calculator):
    # Create method to calculate using exponent operation
    def power(self, num1, num2):
        return num1 ** num2
    
# Create method t calculate using log operation
    # Use base 10 for log