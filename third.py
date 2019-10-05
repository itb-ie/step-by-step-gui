from tkinter import *

# create a window
window = Tk()

#add a title
window.title("This is a Title")
# resize the window
window.geometry("800x600")

# add elements

# a button
bt = Button(master=window, text="Hello Button")
bt.grid(row=0, column=0, padx=200, pady=100, columnspan=2)

# a label
lb = Label(master=window, text="Hello Label 2")
lb.grid(row=1, column=0)

# a button
bt2 = Button(master=window, text="Another Button")
bt2.grid(row=2, column=0)

# a label
lb = Label(master=window, text="Hello Label - Another column")
lb.grid(row=2, column=1)


# the main loop
window.mainloop()