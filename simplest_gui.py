from tkinter import *

# window
root = Tk()

#window size
root.geometry('300x400')

#button
mybutton = Button(root,text="hellooo", font=("inter",14))

#putting it in center
mybutton.place(relx=0.5,rely=0.2,anchor = CENTER)

#running it
root.mainloop()

