from tkinter import *
import math

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(number))

def button_clear():
    e.delete(0, END)

def button_operator(operator):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + operator)

def button_equal():
    try:
        expression = e.get()
        result = str(eval(expression))  # Evaluate the entered expression
        e.delete(0, END)
        e.insert(0, expression + " = " + result)
    except:
        e.delete(0, END)
        e.insert(0, "Error")
def button_percentage():  # **New function for percentage calculation**
    try:
        value = float(e.get()) / 100
        e.delete(0, END)
        e.insert(0, str(value))
    except:
        e.delete(0, END)
        e.insert(0, "Error")
def button_pi():  
    e.insert(END, str(math.pi))  # **Insert value of Pi**

def button_e():  
    e.insert(END, str(math.e))  # **Insert Euler's number**

def button_square():  
    try:
        value = float(e.get()) ** 2
        e.delete(0, END)
        e.insert(0, str(value))
    except:
        e.delete(0, END)
        e.insert(0, "Error")

def button_sqrt():  
    try:
        value = math.sqrt(float(e.get()))
        e.delete(0, END)
        e.insert(0, str(value))
    except:
        e.delete(0, END)
        e.insert(0, "Error")



root = Tk()
root.title("Calculator")
root.configure(bg="black")
root.geometry("350x600")  # **Adjusted size to fit new buttons**

e = Entry(root, width=16, borderwidth=5, fg="white", bg="black", font=("Arial", 18), justify="right")
e.grid(row=0, column=0, columnspan=4, pady=10)

button_params = {"padx": 20, "pady": 20, "fg": "white", "bg": "black", "font": ("Arial", 14)}

# Creating buttons ()
buttons = [
    Button(root, text="7", **button_params, command=lambda: button_click(7)),
    Button(root, text="8", **button_params, command=lambda: button_click(8)),
    Button(root, text="9", **button_params, command=lambda: button_click(9)),
    Button(root, text="/", **button_params, command=lambda: button_operator("/")),
    Button(root, text="4", **button_params, command=lambda: button_click(4)),
    Button(root, text="5", **button_params, command=lambda: button_click(5)),
    Button(root, text="6", **button_params, command=lambda: button_click(6)),
    Button(root, text="*", **button_params, command=lambda: button_operator("*")),
    Button(root, text="1", **button_params, command=lambda: button_click(1)),
    Button(root, text="2", **button_params, command=lambda: button_click(2)),
    Button(root, text="3", **button_params, command=lambda: button_click(3)),
    Button(root, text="-", **button_params, command=lambda: button_operator("-")),
    Button(root, text="C", **button_params, command=button_clear),
    Button(root, text="0", **button_params, command=lambda: button_click(0)),
    Button(root, text="=", **button_params, command=button_equal),
    Button(root, text="+", **button_params, command=lambda: button_operator("+")),
    Button(root, text=">", **button_params, command=lambda: button_operator(">")),
    Button(root, text="<", **button_params, command=lambda: button_operator("<")),
    Button(root, text=".", **button_params, command=lambda: button_click(".")),  # **Decimal button**
    Button(root, text="%", **button_params, command=button_percentage),  # **Percentage button**
    Button(root, text="π", **button_params, command=button_pi),  # **Pi button**
    Button(root, text="e", **button_params, command=button_e),  # **Euler's number button**

    Button(root, text="x²", **button_params, command=button_square),  # **Square button**
    Button(root, text="√x", **button_params, command=button_sqrt),  # **Square root button**


]

# Placing buttons on a grid 
row = 1
col = 0
for button in buttons:
    button.grid(row=row, column=col, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

# Add "Science Calc Coming Soon" label
Label(root, text="Science Calc Coming Soon", bg="black", fg="white", font=("Arial", 12)).grid(row=9, column=0, columnspan=4, pady=10)

# Adjust grid weights to remove spaces between buttons
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(9):  # **Increased row count for extra buttons**
    root.grid_rowconfigure(i, weight=1)



root.mainloop()
#End of project
