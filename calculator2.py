import tkinter as tk
import math

root = tk.Tk()
root.title("Assignment Calculator")
# root.geometry('300x400')

# Calculator Functions

def clear_input(val):
    print(val)
    str(val)
    input.delete(0,tk.END)
    input.insert(0,val)

# Button Pressed actions.
def button_pressed(x):
    # To cancle the expression.
    if x == 'ce':
        input.delete(0,tk.END)
    
    # For Sin Cos And tengent
    elif x == 'sin':
        sin = int(input.get())
        new_val = math.sin(sin)
        clear_input(new_val)

    elif x == 'cos':
        cos = int(input.get())
        new_val = math.cos(cos)
        clear_input(new_val)

    elif x == 'tan':
        tan = int(input.get())
        new_val = math.tan(tan)
        clear_input(new_val)
    
    # To insert a value.

    elif x != '=':
        input.insert(tk.END,x)

    # Evaluate the expression, Handel error.

    else:
        expression = input.get()
        try:
            value = eval(expression)        
            clear_input(value)

        except Exception as e:
            clear_input(e)

# Main input.

input = tk.Entry(root,width=30,borderwidth=2,font=('Arial',12))
input.grid(row=0,column=0,padx=10,pady=10,columnspan=5)

# Cancle Button.

ce = tk.Button(root,width=10,font=("Arial",10,'bold'), text='Ce', command= lambda : button_pressed('ce'))
ce.grid(row=0,column=4,padx=10,pady=10,ipadx=5,ipady=10)

# Buttons Frame

btn_frame = tk.Frame(root,width=40,height=100)
btn_frame.grid(row=1,columnspan=5)

# Buttons for calculator.

Buttons_text = ['7','8','9','/','*','4','5','6','-','+','1','2','3','0','=','sin','cos', 'tan','%','*']

i = j = 0

# Print all the Buttons in one frame, through loop.
for x in Buttons_text:
    b = tk.Button(btn_frame,width=5, font=('Arial',15) , text=x, command=lambda x = x : button_pressed(x))
    b.grid(row=i,column=j,ipadx=10,ipady=14)
    j += 1

    if j == 5: 
        i+= 1
        j = 0


root.mainloop()