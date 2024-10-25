import tkinter as tk
from tkinter import font

# Function to update the expression in the entry widget
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equal_press():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""

# Function to clear the input field
def clear():
    global expression
    expression = ""
    equation.set("")

# Create the main window
if __name__ == "__main__":  # Corrected from _name_ to __name__
    root = tk.Tk()
    root.title("Stylish Calculator")

    # Global variable to store the expression
    expression = ""

    # StringVar to update the text field
    equation = tk.StringVar()

    # Set the window size and center it on the screen
    window_width = 400
    window_height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height/2 - window_height/2)
    position_right = int(screen_width/2 - window_width/2)
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    
    # Set the background color and add padding around the window
    root.configure(bg="black", padx=20, pady=20)

    # Entry widget for displaying the expression and result
    entry_font = font.Font(size=20, weight='bold')
    expression_field = tk.Entry(root, textvariable=equation, font=entry_font, bg="black", fg="white", bd=10, justify='right', relief='flat')
    expression_field.grid(columnspan=4, ipadx=8, ipady=25, pady=20)

    # Button styling
    button_font = font.Font(size=18)

    button_options = {
        'bg': 'white', 'fg': 'black', 'font': button_font, 'bd': 1, 'relief': 'flat',
        'width': 5, 'height': 2, 'highlightthickness': 0, 'activebackground': '#e0e0e0',
        'borderwidth': 0
    }

    # Create circular buttons using a frame to handle spacing
    def create_button(text, row, col, cmd=None):
        btn_frame = tk.Frame(root, bg='black', padx=10, pady=10)  # Frame to hold the button with padding
        btn_frame.grid(row=row, column=col)
        button = tk.Button(btn_frame, text=text, command=cmd, **button_options)
        button.config(width=1, height=1)  # Circle shape comes from small width and height
        button.grid(sticky="nsew", ipadx=20, ipady=20)  # Ensure a circular appearance

    # Add buttons to the calculator with updated layout
    create_button('1', 2, 0, lambda: press(1))
    create_button('2', 2, 1, lambda: press(2))
    create_button('3', 2, 2, lambda: press(3))
    create_button(' + ', 2, 3, lambda: press("+"))

    create_button('4', 3, 0, lambda: press(4))
    create_button('5', 3, 1, lambda: press(5))
    create_button('6', 3, 2, lambda: press(6))
    create_button(' - ', 3, 3, lambda: press("-"))

    create_button('7', 4, 0, lambda: press(7))
    create_button('8', 4, 1, lambda: press(8))
    create_button('9', 4, 2, lambda: press(9))
    create_button(' * ', 4, 3, lambda: press("*"))

    create_button(' C ', 5, 0, clear)
    create_button('0', 5, 1, lambda: press(0))
    create_button(' = ', 5, 2, equal_press)
    create_button(' / ', 5, 3, lambda: press("/"))

    # Run the application
    root.mainloop()
