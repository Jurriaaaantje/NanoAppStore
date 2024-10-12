from tkinter import *  # Importing all from tkinter (for GUI development)
from tkinter import ttk  # Importing ttk for themed tkinter widgets


def start_calculator():
    # Initialize the main window
    root = Tk()
    frm = ttk.Frame(root, padding=10)  # Create a frame to hold the calculator components
    frm.grid()  # Place the frame on the grid

    # Create GUI components: a label for the calculator and a display area for numbers
    ttk.Label(frm, text="Calculator:").grid(column=1, row=0)
    display = ttk.Label(frm, text="")  # Empty label to act as the calculator display
    display.grid(column=1, row=1)

    # Variables to track the calculator state
    current_input = ""  # This will hold the current number being entered
    operator = ""  # This will hold the operator (+, -, *, /)
    first_number = None  # First operand, initialized as None

    def update_display():
        """Update the calculator's display with the current expression."""
        if first_number is not None:  # Display when there's a first number, operator, and current input
            display.config(text=str(first_number) + " " + operator + " " + current_input)
        else:
            display.config(text=str(current_input))  # Display the current input alone if no first number

    def enternum(num):
        """Handle button presses for numbers, operators, and commands."""
        nonlocal current_input, operator, first_number

        if num == "C":
            # Clear all inputs when 'C' is pressed
            current_input = ""
            operator = ""
            first_number = None
        elif str(num) in "+-x:":
            # Handle operator input (+, -, x, :)
            if current_input:  # Ensure a number has been entered before setting an operator
                if first_number is None:  # Only set first number if it hasn't been set yet
                    first_number = float(current_input)  # Convert the current input to a float
                operator = str(num)  # Set the operator
                current_input = ""  # Clear the current input for the next number
        elif num == "=":
            # Handle calculation when '=' is pressed
            if current_input and operator and first_number is not None:
                try:
                    # Create an expression string (replace 'x' and ':' with '*', '/')
                    expression = str(first_number) + operator.replace('x', '*').replace(':', '/') + str(
                        float(current_input))
                    result = str(eval(expression))  # Evaluate the expression using eval
                    current_input = result  # Display the result
                    first_number = None  # Reset for the next calculation
                    operator = ""  # Reset the operator
                except Exception as e:
                    # Handle any errors in the calculation (e.g., division by zero)
                    current_input = "Error"
                    first_number = None  # Reset everything on error
                    operator = ""
        elif num == ".":
            # Ensure only one decimal point is allowed in the current input
            if "." not in current_input:
                current_input += num
        else:
            # Append a number to the current input
            current_input += str(num)

        update_display()  # Update the calculator display after every button press

    # Create buttons for digits, operators, and commands
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=0)  # Button to quit the calculator
    ttk.Button(frm, text="1", command=lambda: enternum(1)).grid(column=0, row=2)
    ttk.Button(frm, text="2", command=lambda: enternum(2)).grid(column=1, row=2)
    ttk.Button(frm, text="3", command=lambda: enternum(3)).grid(column=2, row=2)
    ttk.Button(frm, text="4", command=lambda: enternum(4)).grid(column=0, row=3)
    ttk.Button(frm, text="5", command=lambda: enternum(5)).grid(column=1, row=3)
    ttk.Button(frm, text="6", command=lambda: enternum(6)).grid(column=2, row=3)
    ttk.Button(frm, text="7", command=lambda: enternum(7)).grid(column=0, row=4)
    ttk.Button(frm, text="8", command=lambda: enternum(8)).grid(column=1, row=4)
    ttk.Button(frm, text="9", command=lambda: enternum(9)).grid(column=2, row=4)
    ttk.Button(frm, text="0", command=lambda: enternum(0)).grid(column=1, row=5)
    ttk.Button(frm, text="C", command=lambda: enternum("C")).grid(column=0, row=5)  # Clear button
    ttk.Button(frm, text=".", command=lambda: enternum(".")).grid(column=2, row=5)  # Decimal point button
    ttk.Button(frm, text="+", command=lambda: enternum("+")).grid(column=3, row=1)
    ttk.Button(frm, text="-", command=lambda: enternum("-")).grid(column=3, row=2)
    ttk.Button(frm, text="x", command=lambda: enternum("x")).grid(column=3, row=3)  # Multiplication
    ttk.Button(frm, text=":", command=lambda: enternum(":")).grid(column=3, row=4)  # Division
    ttk.Button(frm, text="=", command=lambda: enternum("=")).grid(column=3, row=5)  # Equals

    # Initialize the display with the current input
    root.title("Calculator")  # Set the window title
    update_display()  # Initially update the display
    root.mainloop()  # Start the main event loop


# Run the calculator when this script is executed
if __name__ == "__main__":
    start_calculator()
