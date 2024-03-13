from tkinter import *

def milesToKm():
    miles = float(milesEntry.get())
    km = miles * 1.609
    kmLabel.config(text=f"{km}")

window = Tk()
window.title("Miles to Km Calc")
window.minsize(width=200, height=300)
window.config(padx=10, pady=10)

milesEntry = Entry()

kmLabel = Label(text="0 KM")

button = Button(text="COnvert", command=milesToKm)

milesEntry.grid(row=0, column=1)
kmLabel.grid(row=1, column=1)
button.grid(row=2, column=1)

window.mainloop()
