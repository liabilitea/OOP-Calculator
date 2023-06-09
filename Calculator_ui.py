# Import modules for UI
import tkinter as tk
from tkinter import messagebox
from Sci_cal import ScientificCalculator

# Define CalculatorUI class to manage and customize the interface
class CalculatorUI(tk.Tk):
    def __init__(self):
    # Call method of parent class
        super().__init__()
        self.title("Scientific Calculator")
        self.geometry("350x350")
        self.configure(bg='#ffcccc')

        operations = ["+", "-", "*", "/", "^", "log" ]

# Create labels for operation and operation options 
        operation_label = tk.Label(self, text="Choose an operation:", bg='#ffcccc')
        operation_label.pack(pady=10)

        self.operation_var = tk.StringVar(self)
        operation_menu = tk.OptionMenu(self, self.operation_var, *operations, command=self.log_operation)
        operation_menu.pack(pady=10)

# Create labels and fields for numbers
        num1_label = tk.Label(self, text="Enter first number:", bg='#ffcccc')
        num1_label.pack(pady=10)
        self.num1_entry = tk.Entry(self)
        self.num1_entry.pack(pady=10)

        num2_label = tk.Label(self, text="Enter second number (not applicable with log operation):", bg='#ffcccc')
        num2_label.pack(pady=10)
        self.num2_entry = tk.Entry(self)
        self.num2_entry.pack(pady=10)

# Create label for result
        self.result_label = tk.Label(self, text="", bg='#ffcccc')
        self.result_label.pack(pady=10)

# Create calculate button
        calculate_button = tk.Button(self, text="Calculate", command=self.calculate)
        calculate_button.pack(pady=10)

# Handle fields when user choose log operation
    def log_operation(self, operation):
        if operation == "log":
            self.num1_entry.delete(0, tk.END)
            self.num1_entry.insert(0, "1")
            self.num2_entry.configure(state=tk.DISABLED)
        else:
            self.num1_entry.delete(0, tk.END)
            self.num2_entry.configure(state=tk.NORMAL)
   
# Define calculate method
    def calculate(self):
        try:
        # Get the selected operation and the numbers
            operation = self.operation_var.get()
            num1 = float(self.num1_entry.get())
        
            # Create instance of SciCal Calculator
            calculator = ScientificCalculator()

        # Check if operation is log, exponent, or others
            if operation == 'log':
                result = calculator.log(num1)
            elif operation == '^':
                num2 = float(self.num2_entry.get())
                result = calculator.calculate(operation, num1, num2)
            else:
                num2 = float(self.num2_entry.get())
                result = calculator.calculate(operation, num1, num2)
        
            self.result_label.config(text="Result: " + str(result))

# Display error message in result label
        except ValueError as error:
            self.result_label.config(text=str(error))

        except ZeroDivisionError as error:
            self.result_label.config(text=str(error))

# Clear operation and number entry fields
        self.operation_var.set("")
        self.num1_entry.delete(0, 'end')
        self.num2_entry.delete(0, 'end')

# Ask user if they want to try again or exit using messagebox
        trial = tk.messagebox.askquestion("Try again?", "Do you want to try again?")
    
        # If yes, clear result label and continue
        if trial == 'yes':
            self.result_label.config(text="")
        else:
        # If no, destroy UI and exit
            self.destroy()