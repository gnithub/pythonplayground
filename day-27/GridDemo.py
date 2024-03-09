from tkinter import *

window = Tk()
window.minsize(width=2400, height=3600)

window.config(padx=100, pady=100)

button = Button(text="Click me")

input = Entry(text="default text")

label = Label(text="Testing..")
label.config(padx=20, pady=20)

#ibutton.pack()

input.place(x=100, y=300)
label.grid(row=2, column=2)


button.grid(row=0, column=0)
#input.grid(row=1, column=1)
window.mainloop()
