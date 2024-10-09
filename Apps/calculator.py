from tkinter import *
from tkinter import ttk

def start_calculator():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()

    # Create GUI components
    ttk.Label(frm, text="Calculator:").grid(column=1, row=0)
    display = ttk.Label(frm, text="")
    display.grid(column=1, row=1)

    # Keep track of the current input
    current_input = ""
    operator = ""
    first_number = None  # Start with None

    def update_display():
        # Display format: "<first_number> <operator> <current_input>"
        if first_number is not None:  # Check explicitly for None
            display.config(text=str(first_number) + " " + operator + " " + current_input)
        else:
            display.config(text=str(current_input))

    def enternum(num):
        nonlocal current_input, operator, first_number
        if num == "C":
            current_input = ""
            operator = ""
            first_number = None
        elif str(num) in "+-x:":
            if current_input:  # Only allow operator if there is a number entered
                if first_number is None:
                    first_number = float(current_input)
                operator = str(num)
                current_input = ""
        elif num == "=":
            if current_input and operator and first_number is not None:
                try:
                    # Create the full expression for evaluation
                    expression = str(first_number) + operator.replace('x', '*').replace(':', '/') + str(
                        float(current_input))
                    result = str(eval(expression))  # Eval the final expression
                    current_input = result
                    first_number = None  # Reset for the next calculation
                    operator = ""  # Also reset operator
                except Exception as e:
                    current_input = "Error"
                    first_number = None  # Reset on error
                    operator = ""  # Reset operator on error
        elif num == ".":
            if "." not in current_input:  # Only allow one decimal point
                current_input += num
        else:  # Treat it as a number
            current_input += str(num)

        update_display()

    # Numeric and command buttons
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=0)
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
    ttk.Button(frm, text="C", command=lambda: enternum("C")).grid(column=0, row=5)
    ttk.Button(frm, text=".", command=lambda: enternum(".")).grid(column=2, row=5)
    ttk.Button(frm, text="+", command=lambda: enternum("+")).grid(column=3, row=1)
    ttk.Button(frm, text="-", command=lambda: enternum("-")).grid(column=3, row=2)
    ttk.Button(frm, text="x", command=lambda: enternum("x")).grid(column=3, row=3)
    ttk.Button(frm, text=":", command=lambda: enternum(":")).grid(column=3, row=4)
    ttk.Button(frm, text="=", command=lambda: enternum("=")).grid(column=3, row=5)
    # Initialize display
    root.title("Calculator")
    update_display()
    root.mainloop()

if __name__ == "__main__":
    start_calculator()