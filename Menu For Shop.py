# import tkinter module
from tkinter import *

# make a window
window = Tk()

# specify it's size
window.geometry("700x600")

# take a image for background
bg = PhotoImage(file='bc.png')

# label it in the background
label17 = Label(window, image=bg)

# position the image as well
label17.place(x=0, y=0)


# function to calculate the
# price of all the orders
def calculate():

		# dic for storing the
	# food quantity and price
	dic = {'Tea': [e1, 30],
		'samosa': [e2, 5],
		'pizza': [e3, 150],
		'chilli_potato': [e4, 50],
		'Burger': [e5, 70],
		'Juice': [e6, 150]}
	total = 0
	for key, val in dic.items():
		if val[0].get() != "":
			total += int(val[0].get())*val[1]

	label16 = Label(window,
					text="Your Total Bill is : "+str(total),
					font="times 18")

	# position it
	label16.place(x=20, y=490)
	label16.after(1000, label16.destroy)
	window.after(1000, calculate)


label8 = Label(window,
			text="Swat Restaurant",
			font="times 28 bold")
label8.place(x=350, y=20, anchor="center")


label1 = Label(window,
			text="Menu",
			font="times 28 bold")

label1.place(x=520, y=70)

label2 = Label(window, text="Tea \
Rs 30", font="times 18")

label2.place(x=450, y=120)

label3 = Label(window, text="Samosa \
Rs 5", font="times 18")

label3.place(x=450, y=150)

label4 = Label(window, text="Pizza	 \
Rs 150", font="times 18")
label4.place(x=450, y=180)

label5 = Label(window, text="Chilli Potato \
Rs 50", font="times 18")

label5.place(x=450, y=210)

label6 = Label(window, text="Burger \
Rs 70", font="times 18")

label6.place(x=450, y=240)

label7 = Label(window, text="Juice \
Rs 35", font="times 18")

label7.place(x=450, y=270)

# billing section
label9 = Label(window, text="Select the items",
			font="times 18")
label9.place(x=115, y=70)

label10 = Label(window,
				text="Tea",
				font="times 18")
label10.place(x=20, y=120)

e1 = Entry(window)
e1.place(x=20, y=150)

label11 = Label(window, text="Samosa",
				font="times 18")
label11.place(x=20, y=200)

e2 = Entry(window)
e2.place(x=20, y=230)

label12 = Label(window, text="Pizza",
				font="times 18")
label12.place(x=20, y=280)

e3 = Entry(window)
e3.place(x=20, y=310)

label13 = Label(window,
				text="Chilli Potato",
				font="times 18")
label13.place(x=20, y=360)

e4 = Entry(window)
e4.place(x=20, y=390)

label14 = Label(window,
				text="Burger",
				font="times 18")
label14.place(x=250, y=120)

e5 = Entry(window)
e5.place(x=250, y=150)

label15 = Label(window,
				text="Juice",
				font="times 18")

label15.place(x=250, y=200)

e6 = Entry(window)
e6.place(x=250, y=230)

# execute calculate function after 1 second
window.after(1000, calculate)

# closing the main loop
window.mainloop()
