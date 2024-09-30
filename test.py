from tkinter import *

root = Tk()


label = Label(master= root,
              text= "Welcome to the Nano appstore!",
              background= "black",
              foreground='white',
              font=('Helvetica', 16, 'bold italic'),
              width=100,
              height=4)
label.pack()

button = Button(master= root,text= "Guess the Num",
                background= "white",
                foreground= "black",
                width=20,)
button.pack(pady=10)

root.mainloop()