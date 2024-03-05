from tkinter import *


window = Tk()
window.title("My first GUI progam")
window.minsize(width=500, height=300)

lable = Label(text="", font=("Arial", 24, "bold"))

lable.pack(side="left")

def button_clicked():
   print("Button clicked")
   lable.config(text=input.get())


button = Button(text="Click me", command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()

window.mainloop()

