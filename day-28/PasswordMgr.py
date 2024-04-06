from tkinter import *


window = Tk()
window.title("Password manager")

window.config(padx=20, pady=20)

#canvas = Canvas(width=200, height=200)

#logo_img = PhotoImage(file="pass.png")
#canvas.create_image(100,100, logo_img)
#canvas.grid(row=0, column=1)

websiteLabel = Label(text="website")
userLabel = Label(text="Username")
password = Label(text="Password")

websiteLabel.grid(row=1, column=0)
userLabel.grid(row=2, column=0)
password.grid(row=3, column=0)

websiteEntry = Entry(width=35)
userEntry = Entry(width=35)
passwordEntry = Entry(width=21)

websiteEntry.grid(row=1, column=1)
userEntry.grid(row=2, column=1)
passwordEntry.grid(row=3, column=1)

button = Button(text="Generate", width=60)

button.grid(row=4, column=0, columnspan=3)


window.mainloop()

