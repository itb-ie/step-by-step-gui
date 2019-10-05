from tkinter import *


def get_text():
    entered_text = et_text.get()
    lb2.config(text=entered_text)


# create a window, make it prettier, add functionality
window = Tk()

#add a title
window.title("This is a Title")

# add elements

# a label
lb = Label(master=window, text="Enter a text", font=("Helvetica", 25), fg="blue")
lb.grid(row=0, column=0, padx=30, pady=20)

# an input field
et_text = StringVar()
et = Entry(master=window, width=30, textvariable=et_text, font=("Helvetica", 25))
et.grid(row=0, column=1, padx=30, pady=20)

# anoter label to print into
lb2 = Label(master=window, text="", font=("Helvetica", 25), fg="blue")
lb2.grid(row=1, column=0, columnspan=3)

# a button
bt = Button(master=window, text="Get Text", font=("Arial", 20, "bold"), command=get_text)
bt.grid(row=0, column=2, padx=50, pady=10)

# a button
bt2 = Button(master=window, text="EXIT", font=("Arial", 30, "bold"), command=sys.exit)
bt2.grid(row=2, column=0, padx=30, pady=50, columnspan=3)

# the main loop
window.mainloop()
