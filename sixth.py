import sys
import tkinter as tk
from tkinter.ttk import *


from ttkthemes import ThemedTk


def get_text():
    entered_text = et_text.get()
    lb2.config(text=entered_text)


# create a window, make it prettier, add functionality
window = ThemedTk(screenName="This is a title", theme="radiance")


# with ttk we need to configure styles:
style = Style()
style.configure("TButton", font=("Helvetica", 15, 'bold'), width=25)
style.configure("TLabel", font=("Arial", 25), anchor=tk.W, width=30, foreground="darkblue")
style.configure("TEntry", font=("Arial", 15), anchor=tk.W)

# a label
lb = Label(master=window, text="Enter a text")
lb.grid(row=0, column=0, padx=30, pady=20)

# an input field
et_text = tk.StringVar()
et = Entry(master=window, width=30, textvariable=et_text, font=("Helvetica", 25))
et.grid(row=0, column=1, padx=30, pady=20)

# anoter label to print into
lb2 = Label(master=window, text="")
lb2.grid(row=1, column=0, columnspan=3)

# a button
bt = Button(master=window, text="Get Text", command=get_text)
bt.grid(row=0, column=2, padx=50, pady=10)

# a button
bt2 = Button(master=window, text="EXIT", command=sys.exit)
bt2.grid(row=2, column=0, padx=30, pady=50, columnspan=3)

# the main loop
window.mainloop()
