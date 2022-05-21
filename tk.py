from tkinter import *
from tkinter import ttk
from PyDictionary import PyDictionary

root = Tk()
root.title("Python Dictionary")
root.geometry("600x400")
root.resizable(0,0)
root.config(bg="white")

s = ttk.Style(root)
s.theme_use('xpnative')

def result(*arg):
    words = text_input.get()
    label1['text'] = words

# Text input
text_input = ttk.Entry(root, width=20, font=('sitka small', 11), justify=CENTER)
# Place the input, (X,Y) Coordinates.
text_input.place(x=150,y=80)
# Action bind
text_input.bind('<Return>',result)

# Search Button.
search_btn = Button(root,text='Search',width=7,font=('sitka small',9),bg='#8c52ff', relief=FLAT, command=result)
search_btn.place(x=360,y=80)

# Output Frame
output_frame = Frame(root,bg='#ffffff')
output_frame.place(x=150,y=130,height=150,width=280)

# Lables in output Frame
label1 = Label(output_frame,font=('Arial',12,'bold'),bg='#ffffff')
label1.place(x=10,y=5)

label2 = Label(output_frame,font=('Sitak small',8,'italic'),fg='#a6a6a6',bg='#ffffff',justify=LEFT, text='2nd lable...')
label2.place(x=10,y=30)

label3 = Message(output_frame,width=250,font=('Sitak small',8,'bold'),bg='#ffffff',justify=LEFT, text='3rd Lable...')
label3.place(x=10,y=45)


root.mainloop()