from tkinter import *
import customtkinter as ct
from PIL import Image, ImageTk

my_image = ct.CTkImage(light_image=Image.open("testplot.png"),size=(30,30))

def on_pressed():
	print("pressed")

class MyFrame(ct.CTkFrame):
	def __init__(self,master,**kwargs):
		super().__init__(master,**kwargs)
		self.label = ct.CTkLabel(self)
		self.label.grid(row=0,column=0,padx=20)
		self.image = my_image

#darkmode
ct.set_appearance_mode("dark")

#colortheme
ct.set_default_color_theme("blue")

# window
root = ct.CTk()
root.frame =MyFrame(master=root) 

#window size
root.geometry('300x400')

canvas = Canvas(root,width=200,height=200)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("testplot.png").resize((200,200)))
#img.resize((200,200),resample=3,**attr)
canvas.create_image(10, 10,anchor=NW,image=img)
canvas.place(relx=0.5, rely=0.8,anchor = CENTER)
#button
mybutton = ct.CTkButton(root,text="hellooo", font=("inter",14),command = on_pressed)


#putting it in center
mybutton.place(relx=0.5,rely=0.2,anchor = CENTER)

#running it
root.mainloop()

