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
        operation_label = tk.Label(self, text="Choose an operation:", bg='#ffcccc')
        operation_label.pack(pady=10)

        self.operation_var = tk.StringVar(self)
        operation_menu = tk.OptionMenu(self, self.operation_var, *operations)
        operation_menu.pack(pady=10)

# Create labels and fields for numbers
        num1_label = tk.Label(self, text="Enter first number:", bg='#ffcccc')
        num1_label.pack(pady=10)
        self.num1_entry = tk.Entry(self)
        self.num1_entry.pack(pady=10)

        num2_label = tk.Label(self, text="Enter second number:", bg='#ffcccc')
        num2_label.pack(pady=10)
        self.num2_entry = tk.Entry(self)
        self.num2_entry.pack(pady=10)

# Create label for result
        self.result_label = tk.Label(self, text="", bg='#ffcccc')
        self.result_label.pack(pady=10)

# Create calculate button
        calculate_button = tk.Button(self, text="Calculate", command=self.calculate)
        calculate_button.pack(pady=10)
   
# Define calculate method
   def calculate(self):
        try:
        # Get the selected operation and the numbers
            operation = self.operation_var.get()
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())

        # Call the calculate method from the CalculatorLogic class to perform calculation
            result = Calculator.calculate(operation, num1, num2)

            self.result_label.config(text="Result: " + str(result))

# Display error message in result label
        except ValueError as error:
            self.result_label.config(text=str(error))

        except ZeroDivisionError as error:
            self.result_label.config(text=str(error))

# Clear operation and number entry fields

