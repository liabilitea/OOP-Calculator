# Import modules for UI
import tkinter as tk
from tkinter import messagebox
from Calculator import Calculator

# Define CalculatorUI class to manage and customize the interface
class CalculatorUI(tk.Tk):
    def __init__(self):
    # Call method of parent class
        super().__init__()
        self.title("Calculator")
        self.geometry("300x350")
        self.configure(bg='#ffcccc')

operations = ["+", "-", "*", "/"]

# Create labels for operation and operation options 

# Create labels and fields for numbers

# Create label for result

# Create calculate button

# Define calculate method

# Get the selected operation and the numbers

# Call the calculate method from the CalculatorLogic class to perform calculation

# Display error message in result label

# Clear operation and number entry fields

