from tkinter import *

# create a window, make it prettier
window = Tk()

#add a title
window.title("This is a Title")
# resize the window
window.geometry("400x300")

# add elements

# a button
bt = Button(master=window, text="Hello Button", font=("Arial", 30, "bold"))
bt.grid(row=0, column=0, padx=30, pady=10)

# a label
lb = Label(master=window, text="Hello Label 2", font=("Helvetica", 25), fg="blue")
lb.grid(row=1, column=0, padx=30, pady=20)

# a button
bt2 = Button(master=window, text="Another Button", font=("Arial", 20, "italic"), fg="green")
bt2.grid(row=2, column=0, padx=30, pady=20)

# the main loop
window.mainloop()