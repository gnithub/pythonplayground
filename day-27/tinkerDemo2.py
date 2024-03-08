from tkinter import *

window = Tk()
window.title("Test window 2")
window.minsize(width=2400, height=3600)

text = Text(width=30, height=6)

text.insert(END, "This is the text area")

text.pack()


listbox = Listbox(height=3)
fruits = ["Mango", "grapes", "Papaya", "Banana"]

for fruit in fruits:
    listbox.insert(fruits.index(fruit), fruit)



listbox.pack()
window.mainloop()

